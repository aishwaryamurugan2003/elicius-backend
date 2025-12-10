import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# def send_email(name, email, phone, company, message):

#     subject = f"New Contact Form Message from {name}"

#     body = f"""
# Name: {name}
# Email: {email}
# Phone: {phone}
# Company: {company}

# Message:
# {message}
# """

#     msg = MIMEMultipart()
#     msg["From"] = EMAIL_USER
#     msg["To"] = EMAIL_USER    # Sends email to YOUR inbox
#     msg["Subject"] = subject
#     msg.attach(MIMEText(body, "plain"))

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(EMAIL_USER, EMAIL_PASSWORD)
#     server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
#     server.quit()

#     return True

def send_email(name, email, phone, company, message):
    try:
        subject = f"New Contact Form Message from {name}"

        body = f"""
Name: {name}
Email: {email}
Phone: {phone}
Company: {company}

Message:
{message}
"""

        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        print("Connecting to SMTP...")  # debug

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        print("Login success!")  # debug

        server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
        server.quit()

        print("Email sent!")  # debug

        return True

    except Exception as e:
        print("SMTP ERROR:", e)   # <---- VERY IMPORTANT
        raise e
