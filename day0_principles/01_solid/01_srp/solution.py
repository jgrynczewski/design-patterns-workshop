"""
Single Responsibility Principle SOLUTION
Każda klasa ma jedną odpowiedzialność
"""


class User:
    """Tylko dane użytkownika"""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name


class EmailValidator:
    """Tylko walidacja email"""

    def validate(self, email):
        return "@" in email


class UserRepository:
    """Tylko operacje bazodanowe"""

    def save(self, user):
        print(f"Saving {user.name} to database")


class EmailService:
    """Tylko wysyłanie email"""

    def send(self, email, message):
        print(f"Sending email to {email}: {message}")

# ROZWIĄZANIE: Każda klasa ma jeden powód do zmiany
