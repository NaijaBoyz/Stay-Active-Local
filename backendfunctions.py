import json
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase configuration from JSON file
config_path = r"C:\Users\James\Desktop\StayActive\firebase_config.json"
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

# Initialize Pyrebase with the loaded config
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()  # This initializes the auth object for Firebase Authentication

# Initialize Firestore with your private key
cred = credentials.Certificate(r"C:\Users\James\Desktop\StayActive\stay-active-local-firebase-adminsdk-q7ijl-1adfaf9109.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # This initializes the Firestore client

# Function to sign up a new user
def sign_up_user(email, password, name, preferred_sport, age):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        data = {"Name": name, "Email": email, "PreferredSport": preferred_sport, "Age": age}
        db.collection('Users').document(user["localId"]).set(data)
        return True, "Successfully created user account with uid: " + user["localId"]
    except Exception as e:
        # Attempt to parse error message
        try:
            error_json = json.loads(e.args[1])
            error_message = error_json['error']['message']
        except (IndexError, KeyError, json.JSONDecodeError):
            error_message = str(e)

        return False, "Failed to create user account: " + error_message


# Function to log in a user
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return True, "Successfully logged in with uid: " + user["localId"]
    except Exception as e:
        # Attempt to parse error message
        try:
            error_json = json.loads(e.args[1])
            error_message = error_json['error']['message']
        except (IndexError, KeyError, json.JSONDecodeError):
            error_message = str(e)

        return False, "Failed to login: " + error_message


# Function to create an event
def create_event(user_id, event_name, location, size_of_party, date_time, cost, sport, description, age_requirement):
    # Function body
    event_data = {
        "Event Name": event_name,
        "Location": location,
        "SizeOfParty": size_of_party,
        "DateTime": date_time,
        "Cost": cost,
        "Sport": sport,
        "Description": description,
        "EventCreatorID": user_id,
        "AgeRequirement": age_requirement
    }
    # Add the event data to Firestore and extract the DocumentReference
    _, event_ref = db.collection('Events').add(event_data)
    print("Event created with ID:", event_ref.id)
    return event_ref.id

# Function to add an attendee to an event
def add_attendee_to_event(event_id, user_id):
    # Adding an attendee to the EventAttendees subcollection in Firestore
    db.collection('Events').document(event_id).collection('EventAttendees').add({'UserID': user_id})
    print(f"User {user_id} added as an attendee to event {event_id}")


def get_all_events():
    events = []
    try:
        # Fetch all documents in the Events collection
        docs = db.collection('Events').get()
        for doc in docs:
            event = doc.to_dict()
            event['id'] = doc.id  # Add the document ID to the event data
            events.append(event)
        return events
    except Exception as e:
        print("Error getting documents: ", str(e))
        return []

def get_user_events(user_id):
    events = []
    try:
        # Fetch events where the user is the creator
        docs = db.collection('Events').where(field_path='EventCreatorID', op_string='==', value=user_id).get()

        for doc in docs:
            event = doc.to_dict()
            event['id'] = doc.id
            events.append(event)
        return events
    except Exception as e:
        print("Error getting user events: ", str(e))
        return []
    
def get_user_name_by_id(user_id):
    user_ref = db.collection('Users').document(user_id).get()
    if user_ref.exists:
        user = user_ref.to_dict()
        return user.get('Name', 'Unknown User')  # Return the user's name or a default value
    else:
        return 'Unknown User'
    

def search_events(search_query):
    events = []
    try:
        # Fetch all events
        event_docs = db.collection('Events').get()
        # Loop through each event and fetch the host's name
        for event_doc in event_docs:
            event = event_doc.to_dict()
            # Fetch the host's name
            user_ref = db.collection('Users').document(event["EventCreatorID"]).get()
            user_name = user_ref.to_dict().get('Name', '') if user_ref.exists else 'Unknown'
            event['Host Name'] = user_name
            # Check if search_query is in the event details or host's name
            if search_query.lower() in json.dumps(event).lower() or search_query.lower() in user_name.lower():
                event['id'] = event_doc.id
                events.append(event)
        return events
    except Exception as e:
        print("Error searching for events: ", str(e))
        return []


# Main function to demonstrate usage
def main():
    # Test user details
    test_email = "j@j.com"
    test_password = "123456"
    test_name = "Test User"
    test_preferred_sport = "Basketball"
    test_age = 25

    # Sign up a new user
    #sign_up_user(test_email, test_password, test_name, test_preferred_sport, test_age)

    # Login the user
    user = login_user(test_email, test_password)
    if user:
        user_id = user['localId']

        # Create a new event
        event_id = create_event(
            event_name= "Brian Soccer match",
            user_id=user_id,
            location="Central Park",
            size_of_party=50,
            date_time="2023-12-01T10:00:00",
            cost=5.00,
            sport="Soccer",
            description="Fun soccer event",
            age_requirement=18
        )

        # Add the same user as an attendee to the event
        add_attendee_to_event(event_id, user_id)

"""
if __name__ == '__main__':
    main()
"""