"""
SOLID Evolving Example - Step 3: OCP FIXED
Dodanie Strategy Pattern dla rabatów
"""

from abc import ABC, abstractmethod


# Konkretne implementacje (nadal łamią DIP)
class MySQLDatabase:
    def save_order(self, order_data):
        print(f"MySQL: Saving order to database")


class SMTPEmailer:
    def send_email(self, email, message):
        print(f"SMTP: Sending email to {email}")


# SRP classes (z poprzedniego kroku)
class OrderValidator:
    def validate(self, items, email):
        if not items:
            return False, "No items"
        if "@" not in email:
            return False, "Invalid email"
        return True, "Valid"


class PaymentProcessor:
    def process(self, amount):
        print(f"Processing payment: ${amount}")
        return True


class OrderRepository:
    def __init__(self):
        self.database = MySQLDatabase()

    def save(self, order_data):
        self.database.save_order(order_data)


class NotificationService:
    def __init__(self):
        self.emailer = SMTPEmailer()

    def send_confirmation(self, email, message):
        self.emailer.send_email(email, message)


# === OCP SOLUTION - Strategy Pattern ===

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, total):
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, total):
        return total * 0.05


class PremiumDiscount(DiscountStrategy):
    def calculate(self, total):
        return total * 0.10


class VIPDiscount(DiscountStrategy):
    def calculate(self, total):
        return total * 0.15


# Nowy typ - bez modyfikacji istniejącego kodu!
class StudentDiscount(DiscountStrategy):
    def calculate(self, total):
        return total * 0.20


class DiscountCalculator:
    """OCP ✅ - otwarta na rozszerzenia, zamknięta na modyfikacje"""

    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, total):
        return self.strategy.calculate(total)


class OrderProcessor:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.validator = OrderValidator()
        self.calculator = DiscountCalculator(discount_strategy)
        self.payment = PaymentProcessor()
        self.repository = OrderRepository()
        self.notifications = NotificationService()

    def process_order(self, items, email):
        # Walidacja
        is_valid, message = self.validator.validate(items, email)
        if not is_valid:
            return False, message

        # Obliczenia
        total = sum(item["price"] for item in items)
        discount = self.calculator.calculate(total)
        final_total = total - discount

        # Reszta bez zmian
        self.repository.save({"total": final_total, "email": email})

        if not self.payment.process(final_total):
            return False, "Payment failed"

        self.notifications.send_confirmation(email, f"Order confirmed: ${final_total}")

        return True, "Order processed"


# Pozostałe violations (LSP, ISP, DIP)
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
    # Różne strategie rabatów
    regular_processor = OrderProcessor(RegularDiscount())
    premium_processor = OrderProcessor(PremiumDiscount())
    student_processor = OrderProcessor(StudentDiscount())  # Nowy typ!

    items = [{"price": 100}]

    regular_processor.process_order(items, "regular@example.com")
    premium_processor.process_order(items, "premium@example.com")
    student_processor.process_order(items, "student@example.com")

    print("\n=== SRP + OCP FIXED ===")
    print("✅ SRP: Każda klasa ma jedną odpowiedzialność")
    print("✅ OCP: Nowe rabaty = nowe klasy, bez modyfikacji")
    print("❌ LSP: Nadal BlockedCustomer łamie kontrakt")
    print("❌ ISP: Nadal fat interface OrderHandler")
    print("❌ DIP: Nadal concrete dependencies")
