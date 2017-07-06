import smtplib
from email.mime.text import MIMEText
import os


class Actions:

    @staticmethod
    def send(name, phone, email, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        username = os.environ["EMAIL_USER"]
        pwd = os.environ["EMAIL_PWD"]
        server.login(username, pwd)
        msg = MIMEText(Actions.contact_message(name, phone, email, message))
        msg['Subject'] = 'New contact'
        msg['From'] = email
        msg['To'] = username

        # Send the message via our own SMTP server.
        server.send_message(msg)
        server.quit()

    @staticmethod
    def contact_message(name, phone, email, message):
        new_contact = "You have received a new contact! Here are the details: \n \n"
        new_contact += "Message: " + message + '\n \n'
        new_contact += "Name: " + name + '\n'
        new_contact += "Phone: " + phone + '\n'
        new_contact += "Email: " + email + '\n'
        return new_contact
