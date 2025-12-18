import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(name, email, phone, company, interest, message):
    try:
        subject = f"New Contact Form Submission — {name}"

        html_body = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />

            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    background: #f3f4f6;
                    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                }}

                .email-wrapper {{
                    width: 100%;
                    padding: 40px 0;
                    display: flex;
                    justify-content: center;
                }}

                .email-container {{
                    max-width: 650px;
                    background: #ffffff;
                    border-radius: 14px;
                    box-shadow: 0 6px 25px rgba(0,0,0,0.12);
                    overflow: hidden;
                }}

                .header {{
                    background: linear-gradient(135deg, #003366, #006699);
                    padding: 35px 20px;
                    text-align: center;
                    color: white;
                }}

                .logo {{
                    width: 85px;
                    margin-bottom: 10px;
                }}

                .title {{
                    font-size: 26px;
                    font-weight: 700;
                }}

                .content {{
                    padding: 30px 40px;
                }}

                .section-title {{
                    font-size: 20px;
                    font-weight: 600;
                    margin-bottom: 20px;
                    color: #003366;
                }}

                .field-label {{
                    font-size: 14px;
                    font-weight: 600;
                    color: #003366;
                    margin-bottom: 6px;
                }}

                .input-box {{
                    background: #f9fafb;
                    border: 1px solid #d1d5db;
                    border-radius: 10px;
                    padding: 12px 14px;
                    font-size: 15px;
                    color: #374151;
                    margin-bottom: 18px;
                }}

                .message-box {{
                    background: #f9fafb;
                    border: 1px solid #d1d5db;
                    border-radius: 10px;
                    padding: 14px 16px;
                    font-size: 15px;
                    line-height: 1.6;
                    white-space: pre-line;
                    margin-bottom: 30px;
                }}

                .reply-btn {{
                    display: inline-block;
                    padding: 12px 25px;
                    background: #006699;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 15px;
                    font-weight: 600;
                }}

                .footer {{
                    padding: 18px;
                    background: #f3f4f6;
                    text-align: center;
                    font-size: 13px;
                    color: #6b7280;
                }}
            </style>
        </head>

        <body>
            <div class="email-wrapper">
                <div class="email-container">

                    <div class="header">
                        <img class="logo"
                             src="https://media.licdn.com/dms/image/v2/C4E0BAQFt8Yg0I2Yg_A/company-logo_200_200/company-logo_200_200/0/1630612154098?e=2147483647&v=beta&t=yCct1z1c0mhIZeL7uXIcwDQyqe73K0-ZK5VnhWe_3rI"
                             alt="Elicius Logo" />
                        <div class="title">New Contact Form Submission</div>
                    </div>

                    <div class="content">
                        <div class="section-title">Contact Details</div>

                        <div class="field-label">Name</div>
                        <div class="input-box">{name}</div>

                        <div class="field-label">Email</div>
                        <div class="input-box">{email}</div>

                        <div class="field-label">Phone</div>
                        <div class="input-box">{phone}</div>

                        <div class="field-label">Company</div>
                        <div class="input-box">{company}</div>

                        <div class="field-label">Area of Interest</div>
                        <div class="input-box">{interest}</div>

                        <div class="section-title">Message</div>
                        <div class="message-box">{message}</div>

                        <a class="reply-btn" href="mailto:{email}">
                            Reply to {name}
                        </a>
                    </div>

                    <div class="footer">
                        © 2025 Elicius Energy · All Rights Reserved<br/>
                        Automated message from website contact form
                    </div>

                </div>
            </div>
        </body>
        </html>
        """

        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER
        msg["Subject"] = subject
        msg.attach(MIMEText(html_body, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
        server.quit()

        return True

    except Exception as e:
        print("SMTP ERROR:", e)
        raise e
