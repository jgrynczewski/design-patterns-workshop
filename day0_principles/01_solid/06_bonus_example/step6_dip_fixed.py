"""
SOLID Evolving Example — Step 6: DIP FIXED
Finalna wersja z wszystkimi zasadami SOLID zastosowanymi poprawnie
"""

from abc import ABC, abstractmethod


# === DIP SOLUTION - Abstrakcje ===
class DatabaseInterface(ABC):
  @abstractmethod
  def save_order(self, order_data): pass


class EmailInterface(ABC):
  @abstractmethod
  def send_email(self, email, message): pass


# === Concrete implementations ===
class MySQLDatabase(DatabaseInterface):
  def save_order(self, order_data):
      print(f"MySQL: Saving order to database")


class SMTPEmailer(EmailInterface):
  def send_email(self, email, message):
      print(f"SMTP: Sending email to {email}")


class PostgreSQLDatabase(DatabaseInterface):
  def save_order(self, order_data):
      print(f"PostgreSQL: Saving order to database")


class SendGridEmailer(EmailInterface):
  def send_email(self, email, message):
      print(f"SendGrid: Sending email to {email}")


# === ISP SOLUTION - Małe interfejsy ===
class Validatable(ABC):
  @abstractmethod
  def validate_order(self, items, email): pass


class DiscountCalculable(ABC):
  @abstractmethod
  def calculate_discount(self, total): pass


class Persistable(ABC):
  @abstractmethod
  def save_to_database(self, order_data): pass


class Notifiable(ABC):
  @abstractmethod
  def send_confirmation(self, email, message): pass


class Payable(ABC):
  @abstractmethod
  def process_payment(self, amount): pass


# === SRP SOLUTION — Osobne odpowiedzialności ===
class OrderValidator(Validatable):
  def validate_order(self, items, email):
      if not items:
          return False, "No items"
      if "@" not in email:
          return False, "Invalid email"
      return True, "Valid"


class DiscountCalculator(DiscountCalculable):
  def __init__(self, strategy):
      self.strategy = strategy

  def calculate_discount(self, total):
      return self.strategy.calculate_discount(total)


class OrderPersistence(Persistable):
  def __init__(self, database: DatabaseInterface):  # DIP — zależy od abstrakcji
      self.database = database

  def save_to_database(self, order_data):
      self.database.save_order(order_data)


class EmailNotifier(Notifiable):
  def __init__(self, emailer: EmailInterface):  # DIP — zależy od abstrakcji
      self.emailer = emailer

  def send_confirmation(self, email, message):
      self.emailer.send_email(email, message)


class PaymentProcessor(Payable):
  def process_payment(self, amount):
      print(f"Processing payment: ${amount}")
      return True


# === OCP SOLUTION - Strategy pattern ===
class DiscountStrategy(ABC):
  @abstractmethod
  def calculate_discount(self, total): pass


class RegularCustomerDiscount(DiscountStrategy):
  def calculate_discount(self, total):
      return total * 0.05


class PremiumCustomerDiscount(DiscountStrategy):
  def calculate_discount(self, total):
      return total * 0.10


class VIPCustomerDiscount(DiscountStrategy):
  def calculate_discount(self, total):
      return total * 0.15


class StudentCustomerDiscount(DiscountStrategy):  # Łatwe dodawanie nowych typów
  def calculate_discount(self, total):
      return total * 0.20


# === LSP SOLUTION - Poprawna hierarchia ===
class Customer(ABC):
  @abstractmethod
  def get_discount_strategy(self): pass

  @abstractmethod
  def can_receive_discount(self): pass


class ActiveCustomer(Customer):
  def can_receive_discount(self):
      return True


class RegularCustomer(ActiveCustomer):
  def get_discount_strategy(self):
      return RegularCustomerDiscount()


class PremiumCustomer(ActiveCustomer):
  def get_discount_strategy(self):
      return PremiumCustomerDiscount()


class VIPCustomer(ActiveCustomer):
  def get_discount_strategy(self):
      return VIPCustomerDiscount()


class BlockedCustomer(Customer):
  def get_discount_strategy(self):
      return RegularCustomerDiscount()  # Ma strategię, ale nie może jej użyć

  def can_receive_discount(self):
      return False  # Jasny kontrakt — bez wyjątków


# === Główny procesor z dependency injection ===
class OrderProcessor:
  """Czysta implementacja używająca wszystkich zasad SOLID"""

  def __init__(self,
               validator: Validatable,
               discount_calculator: DiscountCalculable,
               persistence: Persistable,
               notifier: Notifiable,
               payment_processor: Payable):
      # DIP - wszystkie zależności jako abstrakcje
      self.validator = validator
      self.discount_calculator = discount_calculator
      self.persistence = persistence
      self.notifier = notifier
      self.payment_processor = payment_processor

  def process_order(self, customer: Customer, items, email):
      # SRP — każdy komponent ma jedną odpowiedzialność
      is_valid, message = self.validator.validate_order(items, email)
      if not is_valid:
          return False, message

      total = sum(item["price"] for item in items)

      # LSP — wszystkie typy Customer działają jednakowo
      if customer.can_receive_discount():
          strategy = customer.get_discount_strategy()
          self.discount_calculator.strategy = strategy
          discount = self.discount_calculator.calculate_discount(total)
          final_total = total - discount
      else:
          final_total = total

      # Delegacja do wyspecjalizowanych komponentów
      order_data = {"total": final_total, "email": email}
      self.persistence.save_to_database(order_data)
      self.notifier.send_confirmation(email, f"Order confirmed: ${final_total}")

      if not self.payment_processor.process_payment(final_total):
          return False, "Payment failed"

      return True, "Order processed successfully"


def calculate_total_discount(customers: list):
  """Funkcja demonstrująca LSP compliance"""
  total = 0
  for customer in customers:
      if customer.can_receive_discount():  # Bezpieczne sprawdzenie
          strategy = customer.get_discount_strategy()
          total += strategy.calculate_discount(100)  # Przykładowa kalkulacja
  return total


if __name__ == "__main__":
    # === DIP w akcji — łatwe przełączanie implementacji ===

    # Konfiguracja 1: MySQL + SMTP
    mysql_db = MySQLDatabase()
    smtp_emailer = SMTPEmailer()

    # Konfiguracja 2: PostgreSQL + SendGrid
    postgres_db = PostgreSQLDatabase()
    sendgrid_emailer = SendGridEmailer()

    # Wybór konfiguracji
    database = mysql_db  # lub postgres_db
    emailer = smtp_emailer  # lub sendgrid_emailer

    # Tworzenie komponentów ze wstrzykniętymi zależnościami
    validator = OrderValidator()
    discount_calc = DiscountCalculator(RegularCustomerDiscount())
    persistence = OrderPersistence(database)  # DIP — wstrzyknięta abstrakcja
    notifier = EmailNotifier(emailer)  # DIP — wstrzyknięta abstrakcja
    payment = PaymentProcessor()

    # Główny procesor z dependency injection
    processor = OrderProcessor(
      validator=validator,
      discount_calculator=discount_calc,
      persistence=persistence,
      notifier=notifier,
      payment_processor=payment
    )

    # Wszystkie zasady SOLID w akcji
    premium_customer = PremiumCustomer()
    success, message = processor.process_order(
      premium_customer,
      [{"price": 100}],
      "test@example.com"
    )
    print(f"Result: {success}, {message}")

    # LSP compliance — wszystkie typy Customer działają
    customers_list = [RegularCustomer(), PremiumCustomer(), BlockedCustomer()]
    total_discount = calculate_total_discount(customers_list)
    print(f"Total available discount: ${total_discount}")

    print("\n=== WSZYSTKIE ZASADY SOLID ZASTOSOWANE ===")
    print("✅ SRP: Każda klasa ma jedną, jasną odpowiedzialność")
    print("✅ OCP: Nowe typy klientów przez strategy pattern")
    print("✅ LSP: Wszystkie typy Customer działają jednakowo")
    print("✅ ISP: Małe, wyspecjalizowane interfejsy")
    print("✅ DIP: Zależności od abstrakcji, nie konkretnych klas")
    print("\n🎉 Kod jest łatwy w utrzymaniu, rozszerzaniu i testowaniu!")
