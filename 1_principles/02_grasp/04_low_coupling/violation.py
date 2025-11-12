"""
Low Coupling Violation
Klasa zależy od wielu konkretnych implementacji (high coupling)
"""


class Database:
    def save(self, data):
        print("Saving to MySQL database")


class SMTPEmailer:
    def send(self, email, message):
        print(f"SMTP: Sending {message} to {email}")


class FileLogger:
    def log(self, message):
        print(f"File: {message}")


class PayPalGateway:
    def charge(self, amount):
        print(f"PayPal: Charging ${amount}")


class SMSService:
    def send_sms(self, phone, message):
        print(f"SMS to {phone}: {message}")


class OrderProcessor:  # PROBLEM: High coupling — zna 5 konkretnych klas
    def __init__(self):
        self.db = Database()  # Konkretna klasa
        self.email = SMTPEmailer()  # Konkretna klasa
        self.logger = FileLogger()  # Konkretna klasa
        self.payment = PayPalGateway()  # Konkretna klasa
        self.sms = SMSService()  # Konkretna klasa
        # 5 dependencies = bardzo high coupling

    def process(self, order):
        # Używa wszystkich dependencies
        self.logger.log(f"Processing order {order['id']}")
        self.db.save(order)
        self.payment.charge(order['total'])
        self.email.send(order['email'], "Order confirmed")
        self.sms.send_sms(order['phone'], "Order confirmed")

        # Dodanie nowej funkcjonalności = modyfikacja tej klasy
        return True


if __name__ == "__main__":
    processor = OrderProcessor()

    order = {
        'id': 123,
        'total': 100,
        'email': 'test@example.com',
        'phone': '+1234567890'
    }

    processor.process(order)

    print("❌ OrderProcessor zależy od 5 konkretnych klas")
    print("❌ Trudne testowanie - nie można mock dependencies")
    print("❌ Trudne zmiany - każda nowa funkcjonalność wymaga modyfikacji")
