import smtplib

sender_email = "senderid@gmail.com"
receiver_email = "reciverid@gmail.com"
password = "Enter your passward"

message = """\
Subject: Test Email

This is a test email from Python.
"""

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully.")
except Exception as e:
    print(f"Error: {e}")
