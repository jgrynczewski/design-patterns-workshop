"""
SOLID Evolving Example - Step 5: ISP FIXED
Segregacja interfejsów na małe, skupione interfejsy
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


class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, total):
        return self.strategy.calculate(total)


# LSP classes
class Customer:
    def get_status(self):
        return "active"


class ActiveCustomer(Customer):
    def get_discount_rate(self):
        return 0.05


class PremiumCustomer(ActiveCustomer):
    def get_discount_rate(self):
        return 0.10


# === ISP SOLUTION — małe, skupione interfejsy ===

class Validatable(ABC):
    """Tylko walidacja"""

    @abstractmethod
    def validate_order(self):
        pass


class DiscountCalculable(ABC):
    """Tylko obliczanie rabatów"""

    @abstractmethod
    def calculate_discount(self):
        pass


class Persistable(ABC):
    """Tylko zapis do bazy"""

    @abstractmethod
    def save_to_database(self):
        pass


class Notifiable(ABC):
    """Tylko powiadomienia"""

    @abstractmethod
    def send_confirmation(self):
        pass


class Payable(ABC):
    """Tylko płatności"""

    @abstractmethod
    def process_payment(self):
        pass


# Implementacje — każda wybiera tylko potrzebne interfejsy

class SimpleOrderValidator(Validatable):
    """ISP ✅ - implementuje tylko to czego potrzebuje"""

    def validate_order(self):
        return True


class SimpleDiscountCalculator(DiscountCalculable):
    """ISP ✅ - implementuje tylko to czego potrzebuje"""

    def calculate_discount(self):
        return 0.05


class OrderPersister(Persistable):
    """ISP ✅ - implementuje tylko to czego potrzebuje"""

    def save_to_database(self):
        print("Saving to database")


class EmailNotifier(Notifiable):
    """ISP ✅ - implementuje tylko to czego potrzebuje"""

    def send_confirmation(self):
        print("Sending email confirmation")


class CreditCardProcessor(Payable):
    """ISP ✅ - implementuje tylko to czego potrzebuje"""

    def process_payment(self):
        print("Processing credit card payment")


# Jeśli potrzebujesz wielu funkcji, implementujesz wiele interfejsów
class FullOrderHandler(Validatable, Persistable, Notifiable):
    """ISP ✅ - implementuje tylko te interfejsy których potrzebuje"""

    def validate_order(self):
        return True

    def save_to_database(self):
        print("Full handler: saving to database")

    def send_confirmation(self):
        print("Full handler: sending confirmation")

    # Nie musi implementować DiscountCalculable ani Payable!


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


if __name__ == "__main__":
    processor = OrderProcessor(PremiumDiscount())
    processor.process_order([{"price": 100}], "test@example.com")

    # ISP w działaniu — każda klasa implementuje tylko potrzebne interfejsy
    validator = SimpleOrderValidator()
    calculator = SimpleDiscountCalculator()
    persister = OrderPersister()
    notifier = EmailNotifier()
    payment_processor = CreditCardProcessor()

    validator.validate_order()
    persister.save_to_database()
    notifier.send_confirmation()
    # Każda klasa ma tylko metody, których potrzebuje!

    print("\n=== SRP + OCP + LSP + ISP FIXED ===")
    print("✅ SRP: Każda klasa ma jedną odpowiedzialność")
    print("✅ OCP: Nowe rabaty = nowe klasy")
    print("✅ LSP: Wszystkie subklasy można bezpiecznie zastąpić")
    print("✅ ISP: Małe, skupione interfejsy")
    print("❌ DIP: Nadal concrete dependencies")
