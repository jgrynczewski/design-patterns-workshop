"""
SOLID Evolving Example — Step 2: SRP FIXED
Rozdzielenie odpowiedzialności na osobne klasy
"""

from abc import ABC, abstractmethod


# Konkretne implementacje (nadal łamią DIP)
class MySQLDatabase:
    def save_order(self, order_data):
        print(f"MySQL: Saving order to database")


class SMTPEmailer:
    def send_email(self, email, message):
        print(f"SMTP: Sending email to {email}")


# === SRP SOLUTION — każda klasa ma jedną odpowiedzialność ===

class OrderValidator:
    """Odpowiedzialność: tylko walidacja"""

    def validate(self, items, email):
        if not items:
            return False, "No items"
        if "@" not in email:
            return False, "Invalid email"
        return True, "Valid"


class DiscountCalculator:
    """Odpowiedzialność: tylko obliczanie rabatów"""

    def calculate(self, customer_type, total):
        if customer_type == "regular":
            return total * 0.05
        elif customer_type == "premium":
            return total * 0.10
        elif customer_type == "vip":
            return total * 0.15
        return 0


class PaymentProcessor:
    """Odpowiedzialność: tylko płatności"""

    def process(self, amount):
        print(f"Processing payment: ${amount}")
        return True


class OrderRepository:
    """Odpowiedzialność: tylko zapis zamówień"""

    def __init__(self):
        self.database = MySQLDatabase()  # Nadal DIP violation

    def save(self, order_data):
        self.database.save_order(order_data)


class NotificationService:
    """Odpowiedzialność: tylko powiadomienia"""

    def __init__(self):
        self.emailer = SMTPEmailer()  # Nadal DIP violation

    def send_confirmation(self, email, message):
        self.emailer.send_email(email, message)


class OrderProcessor:
    """Teraz tylko orkiestruje - SRP ✅"""

    def __init__(self):
        self.validator = OrderValidator()
        self.calculator = DiscountCalculator()
        self.payment = PaymentProcessor()
        self.repository = OrderRepository()
        self.notifications = NotificationService()

    def process_order(self, customer_type, items, email):
        # Walidacja
        is_valid, message = self.validator.validate(items, email)
        if not is_valid:
            return False, message

        # Obliczenia
        total = sum(item["price"] for item in items)
        discount = self.calculator.calculate(customer_type, total)
        final_total = total - discount

        # Zapis
        self.repository.save({"total": final_total, "email": email})

        # Płatność
        if not self.payment.process(final_total):
            return False, "Payment failed"

        # Powiadomienie
        self.notifications.send_confirmation(email, f"Order confirmed: ${final_total}")

        return True, "Order processed"


# Pozostałe violations (OCP, LSP, ISP, DIP) nadal istnieją
class OrderHandler(ABC):
    @abstractmethod
    def validate_order(self): pass

    @abstractmethod
    def calculate_discount(self): pass

    @abstractmethod
    def save_to_database(self): pass

    @abstractmethod
    def send_confirmation(self): pass

    @abstractmethod
    def process_payment(self): pass


class Customer:
    def get_discount(self):
        return 0.05


class BlockedCustomer(Customer):
    def get_discount(self):
        raise Exception("Blocked customers cannot get discounts!")


if __name__ == "__main__":
    processor = OrderProcessor()

    success, message = processor.process_order("premium", [{"price": 100}], "test@example.com")
    print(f"Result: {success}, {message}")

    print("\n=== SRP FIXED ===")
    print("✅ SRP: Każda klasa ma jedną odpowiedzialność")
    print("❌ OCP: Nadal if/else w DiscountCalculator")
    print("❌ LSP: Nadal BlockedCustomer łamie kontrakt")
    print("❌ ISP: Nadal fat interface OrderHandler")
    print("❌ DIP: Nadal concrete dependencies")
