import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver_address, subject, body):
    # Sender and receiver details
    sender_address = 'your_email@gmail.com'
    sender_password = 'your_password'

    # Setup MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    # Body of the email
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_password)  # login with mail_id and password

    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print(f'Mail Sent to {receiver_address}')

# Example usage
send_email("receiver@example.com", "Welcome to Stay Active Local!", "Thank you for signing up for our app. Stay active and connected!")


