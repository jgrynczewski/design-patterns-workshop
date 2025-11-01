"""
Single Responsibility Principle VIOLATION
Klasa z wieloma odpowiedzialnościami
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Odpowiedzialność 1: Dane użytkownika
    def get_name(self):
        return self.name

    # Odpowiedzialność 2: Walidacja email
    def validate_email(self):
        return "@" in self.email

    # Odpowiedzialność 3: Operacje bazodanowe
    def save_to_db(self):
        print(f"Saving {self.name} to database")

    # Odpowiedzialność 4: Wysyłanie email
    def send_email(self, message):
        print(f"Sending email to {self.email}: {message}")

# PROBLEM: User ma 4 powody do zmiany:
# 1. Zmiana danych user
# 2. Zmiana reguł walidacji
# 3. Zmiana bazy danych
# 4. Zmiana sposobu wysyłania email
