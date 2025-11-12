"""
SOLID Evolving Example - Step 1: ALL VIOLATIONS
OrderProcessor łamiący wszystkie zasady SOLID
"""

from abc import ABC, abstractmethod


# konkretne implementacje
class MySQLDatabase:
    def save_order(self, order_data):
        print(f"MySQL: Saving order to database")


class SMTPEmailer:
    def send_email(self, email, message):
        print(f"SMTP: Sending email to {email}")


# === ISP VIOLATION - fat interface ===
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


class SimpleOrderValidator(OrderHandler):
    """Chce tylko walidować, ale musi implementować wszystko!"""

    def validate_order(self): return True

    def calculate_discount(self): raise NotImplementedError("Don't need this!")

    def save_to_database(self): raise NotImplementedError("Don't need this!")

    def send_confirmation(self): raise NotImplementedError("Don't need this!")

    def process_payment(self): raise NotImplementedError("Don't need this!")


class Customer:
    def get_discount(self):
        return 0.05


class PremiumCustomer(Customer):
    def get_discount(self):
        return 0.10


# === LSP VIOLATION - podklasa łamie kontrakt ===
class BlockedCustomer(Customer):
    def get_discount(self):
        raise Exception("Blocked customers cannot get discounts!")  # Łamie LSP!


class OrderProcessor:
    """Klasa łamiąca SRP, OCP, DIP"""

    def __init__(self):
        # DIP VIOLATION — zależy od konkretnych klas
        self.database = MySQLDatabase()
        self.emailer = SMTPEmailer()

    def process_order(self, customer_type, items, email):
        # SRP VIOLATION — jedna metoda robi wszystko:
        # walidację, rabaty, zapis, email, płatności

        # Walidacja
        if not items:
            return False
        if "@" not in email:
            return False

        # OCP VIOLATION — if/else chain, nowy typ = modyfikacja kodu
        total = sum(item["price"] for item in items)

        if customer_type == "regular":
            discount = 0.05
        elif customer_type == "premium":
            discount = 0.10
        elif customer_type == "vip":
            discount = 0.15
        # Jak dodać "student"? Muszę modyfikować ten kod!
        else:
            discount = 0

        final_total = total * (1 - discount)

        # Zapis do bazy
        self.database.save_order({"total": final_total, "email": email})

        # Wysyłanie email
        self.emailer.send_email(email, f"Order confirmed: ${final_total}")

        # Przetwarzanie płatności
        print(f"Processing payment: ${final_total}")

        return True


def calculate_total_discount(customers: list):
    """Funkcja pokazująca LSP violation"""
    total = 0
    for customer in customers:
        total += customer.get_discount()  # Crash dla BlockedCustomer!
    return total


if __name__ == "__main__":
    processor = OrderProcessor()

    # SRP + OCP + DIP violations w action
    processor.process_order("premium", [{"price": 100}], "test@example.com")

    # LSP violation
    customers_list = [Customer(), PremiumCustomer(), BlockedCustomer()]
    try:
        total_discount = calculate_total_discount(customers_list)
    except Exception as e:
        print(f"LSP violation: {e}")

    # ISP violation
    validator = SimpleOrderValidator()
    try:
        validator.calculate_discount()  # Zmuszony do implementacji!
    except NotImplementedError as e:
        print(f"ISP violation: {e}")

    print("\n=== VIOLATIONS SUMMARY ===")
    print("❌ SRP: OrderProcessor robi walidację + rabaty + DB + email + płatności")
    print("❌ OCP: Nowy typ klienta = modyfikacja if/else w process_order")
    print("❌ LSP: BlockedCustomer.get_discount() łamie kontrakt Customer")
    print("❌ ISP: OrderHandler zmusza do implementacji niepotrzebnych metod")
    print("❌ DIP: OrderProcessor zależy od MySQLDatabase i SMTPEmailer")
