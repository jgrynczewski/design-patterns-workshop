"""Konkretne implementacje emaili"""
from interfaces.email import EmailInterface


class SMTPEmailer(EmailInterface):
    def send_email(self, email, message):
        print(f"SMTP: Sending email to {email}")


class SendGridEmailer(EmailInterface):
    def send_email(self, email, message):
        print(f"SendGrid: Sending email to {email}")
