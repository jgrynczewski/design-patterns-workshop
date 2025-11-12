"""Konkretne implementacje przetwarzania zamówień"""
from interfaces.order_processing import Validatable, DiscountCalculable, Persistable, Notifiable, Payable
from interfaces.database import DatabaseInterface
from interfaces.email import EmailInterface


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
    def __init__(self, database: DatabaseInterface):
        self.database = database

    def save_to_database(self, order_data):
        self.database.save_order(order_data)


class EmailNotifier(Notifiable):
    def __init__(self, emailer: EmailInterface):
        self.emailer = emailer

    def send_confirmation(self, email, message):
        self.emailer.send_email(email, message)


class PaymentProcessor(Payable):
    def process_payment(self, amount):
        print(f"Processing payment: ${amount}")
        return True
