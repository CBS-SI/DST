import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

SENDER = os.getenv("SENDER")
PASS = os.getenv("PASS")
RECEIVERS = os.getenv("RECEIVERS")


def send_welcome_emails(sender=SENDER,
                        password=PASS,
                        receivers=RECEIVERS):

    smtp_server = "smtp.office365.com"
    smtp_port = 587

    try:
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)

        # Send email to each recipient
        for recipient_email in email_list:
            # Create message
            message = MIMEMultipart()
            message["From"] = sender
            message["To"] = receivers
            message["Subject"] = "Welcome Message"

            # Add body to email
            body = "Welcome aboard!"
            message.attach(MIMEText(body, "plain"))

            # Send email
            server.send_message(message)
            print(f"Welcome email sent successfully to {recipient_email}")

        # Close the SMTP server
        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")



send_welcome_emails(sender=SENDER,
                        password=PASS,
                        receivers=RECEIVERS)
