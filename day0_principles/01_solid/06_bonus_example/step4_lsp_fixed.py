"""
SOLID Evolving Example - Step 4: LSP FIXED
Poprawna hierarchia klas Customer
"""

from abc import ABC, abstractmethod


# Konkretne implementacje (nadal łamią DIP)
class MySQLDatabase:
    def save_order(self, order_data):
        print(f"MySQL: Saving order to database")


class SMTPEmailer:
    def send_email(self, email, message):
        print(f"SMTP: Sending email to {email}")


# SRP classes
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


# OCP classes
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


class StudentDiscount(DiscountStrategy):
    def calculate(self, total):
        return total * 0.20


class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, total):
        return self.strategy.calculate(total)


# === LSP SOLUTION - poprawna hierarchia Customer ===

class Customer:
    """Bazowa klasa dla wszystkich klientów"""

    def get_status(self):
        return "active"


class ActiveCustomer(Customer):
    """Klient, który może otrzymywać rabaty"""

    def get_discount_rate(self):
        return 0.05

    def get_status(self):
        return "active"


class PremiumCustomer(ActiveCustomer):
    """Premium customer może zastąpić ActiveCustomer"""

    def get_discount_rate(self):
        return 0.10


class BlockedCustomer(Customer):
    """Zablokowany klient - nie dziedziczy po ActiveCustomer!"""

    def get_status(self):
        return "blocked"

    def is_allowed_to_order(self):
        return False


def calculate_total_discount(active_customers):
    """LSP ✅ - działa dla wszystkich ActiveCustomer"""
    total = 0
    for customer in active_customers:
        total += customer.get_discount_rate()  # Bezpieczne!
    return total


def get_customer_statuses(customers):
    """LSP ✅ - działa dla wszystkich Customer"""
    statuses = []
    for customer in customers:
        statuses.append(customer.get_status())  # Bezpieczne!
    return statuses


class OrderProcessor:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.validator = OrderValidator()
        self.calculator = DiscountCalculator(discount_strategy)
        self.payment = PaymentProcessor()
        self.repository = OrderRepository()
        self.notifications = NotificationService()

    def process_order(self, items, email):
        is_valid, message = self.validator.validate(items, email)
        if not is_valid:
            return False, message

        total = sum(item["price"] for item in items)
        discount = self.calculator.calculate(total)
        final_total = total - discount

        self.repository.save({"total": final_total, "email": email})

        if not self.payment.process(final_total):
            return False, "Payment failed"

        self.notifications.send_confirmation(email, f"Order confirmed: ${final_total}")

        return True, "Order processed"


# Pozostałe violations (ISP, DIP)
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


if __name__ == "__main__":
    processor = OrderProcessor(PremiumDiscount())
    processor.process_order([{"price": 100}], "test@example.com")

    # LSP w działaniu
    all_customers = [Customer(), ActiveCustomer(), PremiumCustomer(), BlockedCustomer()]
    statuses = get_customer_statuses(all_customers)  # Działa dla wszystkich!
    print(f"Customer statuses: {statuses}")

    active_customers = [ActiveCustomer(), PremiumCustomer()]  # Tylko active
    total_discount = calculate_total_discount(active_customers)  # Bezpieczne!
    print(f"Total discount rate: {total_discount}")

    print("\n=== SRP + OCP + LSP FIXED ===")
    print("✅ SRP: Każda klasa ma jedną odpowiedzialność")
    print("✅ OCP: Nowe rabaty = nowe klasy")
    print("✅ LSP: Wszystkie subklasy można bezpiecznie zastąpić")
    print("❌ ISP: Nadal fat interface OrderHandler")
    print("❌ DIP: Nadal concrete dependencies")
