
---

# Stay-Active-Local Application Documentation

## Overview
Stay-Active-Local is a community-driven application designed to create and manage local sporting events. It allows users to create events, join events, and manage event details. This application uses PyQt5 for the frontend and Firebase for backend services including authentication, database, and storage.

## Initial Setup

### Prerequisites
Before running the application, you must have Python 3 installed on your system. You will also need to install PyQt5 and Firebase Python SDKs. Use the following commands to install them:

```sh
pip install PyQt5 pyrebase firebase-admin
```

### Firebase Configuration
1. Create a Firebase project via the Firebase Console.
2. Under Project settings, locate your web app's Firebase configuration object.
3. Generate a new private key from the Service accounts tab in your project settings. This will be your Firebase Admin SDK key.

### Application Configuration
After obtaining the Firebase configuration object and the Admin SDK JSON file, you will need to integrate them into the application:

- **Firebase Configuration**: Insert your Firebase configuration object into the appropriate place in your application code.
  
- **Admin SDK JSON File**: Use the path to your downloaded JSON file in the application to initialize your Firebase admin SDK.

## Features and User Roles

### Users
- **Regular Users**: Can search for and join events, view event details, and cancel their participation.
- **Event Hosts**: Can create events, edit or update events, cancel events, and send out email notifications to participants.

### Functionality
- **User Authentication**: Sign up and log in functionality using Firebase Authentication.
- **Event Management**: Users can create and manage the details of the events they host.
- **Real-Time Data**: Utilizes Firebase Firestore for real-time data management and synchronization.
- **Email Notifications**: Supports sending email notifications to event participants for updates or cancellations.

## Running the Application
To start the application, navigate to the directory containing the application files and execute the main script:

```sh
python main.py
```

## Contributing and Support
For any issues, questions, or contributions, please refer to the repository's issues section or contact the repository maintainers.

