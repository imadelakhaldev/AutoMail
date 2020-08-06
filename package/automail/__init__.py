# Imad Elakhal | Smartest Programmer Who Has Ever Lived.

import smtplib
from email.message import EmailMessage


class AutoMail:
    def __init__(self, hostname, port_num, username, password):
        self.message = EmailMessage()
        print("######### STARTING AUTOMAIL #########")
        try:
            self.driver = smtplib.SMTP_SSL(host=hostname, port=port_num)
            print("SMTP driver created successfully.")
            self.driver.ehlo()
            print("Successful SMTP driver identification.")
            self.driver.login(user=username, password=password)
            print("Successful login to SMTP driver.")
        except Exception as ex:
            print("Unable to initialize AutoMail.")
            print(ex)

    def check_status(self):
        try:
            if self.driver.noop()[0] == 250:
                print("SMTP driver is operating.")
                return True
            else:
                print("SMTP driver is not operating.")
                return False
        except Exception as ex:
            print("Unable to check SMTP driver status.")
            print(ex)
            return False

    def reconnect(self, hostname, port_num, username, password):
        try:
            self.driver = smtplib.SMTP_SSL(host=hostname, port=port_num)
            print("SMTP driver re-created successfully.")
            self.driver.ehlo()
            print("Successful SMTP driver re-identification.")
            self.driver.login(user=username, password=password)
            print("Successful re-login to SMTP driver.")
        except Exception as ex:
            print("Unable to re-connect AutoMail.")
            print(ex)

    def add_message(self, subject, content, html=None):
        try:
            self.message["Subject"] = subject
            self.message.set_content(content)
            if html is not None:
                self.message.add_alternative(html, subtype="html")
            print("Message template added.")
        except Exception as ex:
            print("Unable to add message template.")
            print(ex)

    def add_attachment(self, full_path):
        try:
            with open(full_path, "rb") as f:
                file_data = f.read()
                file_name = f.name
                self.message.add_attachment(file_data, maintype="application",
                                            subtype="octet-stream", filename=file_name)
                print("Attachment added to current message template.")
        except Exception as ex:
            print("Unable to add attachment to current message template.")
            print(ex)

    def send_message(self, sender, receiver):
        if self.check_status():
            try:
                self.driver.send_message(msg=self.message, from_addr=sender, to_addrs=receiver)
                print("Message has been sent successfully")
            except Exception as ex:
                print("Unable to send message.")
                print(ex)
        else:
            print("Unable to send message.")

    def send_messages(self, sender, receivers):
        try:
            for address in receivers:
                self.send_message(sender=sender, receiver=address)
            print("Bulk messages sent successfully.")
        except Exception as ex:
            print("Unable to send bulk messages.")
            print(ex)
