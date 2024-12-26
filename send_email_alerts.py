import smtplib
from email.mime.text import MIMEText
from config import *

def send_email_alerts(alerts):
    # Email Configuration
    sender_email = EMAIL_ADDR
    receiver_email = EMAIL_ADDR
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = EMAIL_PSWD

    if alerts:
        # Create email content
        message = MIMEText("\n".join(alerts))
        message["Subject"] = "Risk Management Alert"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)

        print("Alerts sent!")

# test_alerts = ["AAPL: VaR exceeds loss threshold!", "MSFT: Leverage too high!"]
# send_email_alerts(test_alerts)