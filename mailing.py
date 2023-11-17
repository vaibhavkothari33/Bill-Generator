import smtplib

sender_email = "contact.vaibhavkothari@gmail.com"
receiver_email = "vaibhavkothari50@gmail.com"
password = "milv kxvw cvaj ovev"

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
