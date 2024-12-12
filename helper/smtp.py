import smtplib
from email.mime.text import MIMEText

class SMTP:
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.username = 'washing.well.oop@gmail.com'
        self.password = 'idll zmsq ekcp vdoy'
        self.from_email = 'washing.well.oop@gmail.com'
        self.subject = '🌪Your Laundry is Ready for Pickup!'

    def sendMail(self, name, to_email):
        message = f"Hello {name},\n\nYour laundry is ready! All your items have been washed and are ready for pickup. Thank you for using our service!"
        msg = MIMEText(message)
        msg['Subject'] = self.subject
        msg['From'] = self.from_email
        msg['To'] = to_email

        # Connect to the SMTP server and send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.from_email, to_email, msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print(f'Failed to send email: {e}')
