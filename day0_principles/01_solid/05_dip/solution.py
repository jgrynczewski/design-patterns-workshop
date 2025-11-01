"""
Dependency Inversion Principle SOLUTION
Zależność od abstrakcji, a nie od konkretnych implementacji
"""

import abc

# Abstrakcja
class MessageSender(abc.ABC):
    @abc.abstractmethod
    def send(self, message):
        pass


# Konkretna klasa (implementacja) I
class EmailSender(MessageSender):
    def send(self, message):
        return f"Email: {message}"


class NotificationService:
    def __init__(self, sender: MessageSender):  # ✅ programowanie przez abstrakcję
        self.sender = sender

    def notify(self, message):
        return self.sender.send(message)


# ROZWIĄZANIE: Zależy od abstrakcji, łatwo dodawać nowe typy

# Konkretna klasa (implementacja) II
class SMSSender(MessageSender):
    def send(self, message):
        return f"SMS: {message}"


if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SMSSender())

    print(email_service.notify("Hello"))  # Email: Hello
    print(sms_service.notify("Hello"))  # SMS: Hello

    # Nowe typy bez modyfikacji NotificationService!
