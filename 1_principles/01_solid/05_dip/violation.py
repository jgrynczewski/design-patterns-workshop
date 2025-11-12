"""
Dependency Inversion Principle VIOLATION
Zależność od konkretnych implementacji
"""


# Konkretna klasa (implementacja)
class EmailSender:
    def send(self, message):
        return f"Email: {message}"


class NotificationService:
    def __init__(self, sender: EmailSender):  # ❌ Konkretny typ, programowanie przez implementację
        self.sender = sender

    def notify(self, message):
        return self.sender.send(message)


# PROBLEM: Jak dodać SMS? Muszę modyfikować NotificationService

if __name__ == "__main__":
    service = NotificationService(EmailSender())
    print(service.notify("Hello"))  # Email: Hello

    # Nie można łatwo zmienić na SMS bez modyfikacji klasy NotificationService (przynajmniej w teorii)
