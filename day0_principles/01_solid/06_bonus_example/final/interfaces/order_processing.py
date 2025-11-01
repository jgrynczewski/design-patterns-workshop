"""Interfejsy dla przetwarzania zamówień (ISP)"""
from abc import ABC, abstractmethod


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
