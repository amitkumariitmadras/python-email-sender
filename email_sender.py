import smtplib
from email.mime.text import MIMEText
from credentials import *

def send_email(subject, message, sender_email, sender_password, recipient_email, smtp_server, smtp_port):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        print("Sending email: ", sender_email, "Sender Password: ", sender_password)
        server.login(sender_email, sender_password)
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        server.send_message(msg)
        server.quit()
        print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print(f"Error: Email could not be sent. {e}")

if __name__ == '__main__':
    recipient_email = input("Please enter the recipient's email address: ")
    recipient_name = input("Please enter the name of recipient: ")

    subject = 'Happy Birthday {recipient_name}!'

    message_template = """
    <html>
        <body>
            <h1 style="color: #2E8B57;">Happy Birthday, {name} bro!</h1>
            <p>Dear <b>{name}</b>,</p>
            <p>Wishing you a day filled with love, laughter, and joy. Here's to another year of fantastic adventures!</p>
            <p>Enjoy your special day to the fullest!</p>
            <br>
            <p>Best wishes,</p>
            <p><i>Your Friend</i></p>
        </body>
    </html>
    """

    message = message_template.format(name=recipient_name)
    send_email(subject, message, sender_email, sender_password, recipient_email, smtp_server, smtp_port)


# yatharthsingh1504@gmail.com
# hey how are you doing
# bro this is email from business account
