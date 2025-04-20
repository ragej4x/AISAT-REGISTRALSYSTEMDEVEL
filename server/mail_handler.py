import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

sender_email = "devtestragejax@gmail.com"
app_password = "gwii vzon zglx ghfe"



class Generatecode():
    def __init__(self, email, attempt=0):
        self.code = f"{random.randint(0, 9999):04d}"
        self.email = email

    def get_code(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "AISAT Password Recovery"
        message["From"] = sender_email
        message["To"] = self.email

        text = "test\n code"
        html = f"""
        <html>
        <body>
            <p>your code {self.code} <i>test</i>
            </p>
        </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)


        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, self.email, message.as_string())
            print(f" emil sent to : {self.email}")
            return self.code
        except Exception as e:
            print(" Error sending email:", e)
