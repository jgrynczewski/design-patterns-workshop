"""
Polymorphism Solution - GRASP
Polimorfizm zamiast if/else statements
"""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class CreditCard(PaymentMethod):
    def process(self, amount):
        return f"Credit card payment: ${amount}"


class PayPal(PaymentMethod):
    def process(self, amount):
        return f"PayPal payment: ${amount}"


class BankTransfer(PaymentMethod):
    def process(self, amount):
        return f"Bank transfer: ${amount}"


class Cryptocurrency(PaymentMethod):  # Nowy typ - zero zmian w PaymentProcessor
    def process(self, amount):
        return f"Crypto payment: ${amount}"


class PaymentProcessor:
    def process_payment(self, method: PaymentMethod, amount):
        return method.process(amount)  # Polimorfizm - nie trzeba znać konkretnego typu


if __name__ == "__main__":
    processor = PaymentProcessor()

    credit_card = CreditCard()
    paypal = PayPal()
    crypto = Cryptocurrency()

    print(processor.process_payment(credit_card, 100))
    print(processor.process_payment(paypal, 200))
    print(processor.process_payment(crypto, 300))
    print("✅ Nowe typy płatności bez modyfikacji PaymentProcessor")
