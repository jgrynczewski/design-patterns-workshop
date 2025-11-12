"""
Indirection Solution - GRASP
Abstraction layer między components
"""

from abc import ABC, abstractmethod


# Indirection layer - interface
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount, card_number):
        pass


# Concrete adapter dla PayPal
class PayPalAdapter(PaymentGateway):
    def __init__(self):
        self.api_url = "https://api.paypal.com/v1/payments"
        self.api_key = "pk_test_12345"

    def process_payment(self, amount, card_number):
        # PayPal specific implementation
        payment_data = {
            "amount": amount,
            "currency": "USD",
            "card_number": card_number,
            "api_key": self.api_key
        }
        # requests.post(self.api_url, json=payment_data)
        return f"PayPal payment: ${amount}"


# Nowy adapter - zero zmian w OrderService
class StripeAdapter(PaymentGateway):
    def __init__(self):
        self.api_key = "sk_test_67890"

    def process_payment(self, amount, card_number):
        # Stripe specific implementation
        charge_data = {
            "amount": int(amount * 100),  # Stripe używa centów
            "source": card_number,
            "currency": "usd"
        }
        # stripe.Charge.create(**charge_data)
        return f"Stripe payment: ${amount}"


class OrderService:
    def __init__(self, payment_gateway: PaymentGateway):
        # Dependency na abstrakcję, nie na konkretną implementację
        self.payment_gateway = payment_gateway

    def process_order(self, order):
        # Nie zna szczegółów PayPal/Stripe API
        result = self.payment_gateway.process_payment(order.total, order.card_number)

        if "payment:" in result:
            order.status = "paid"
            return "Payment successful"
        else:
            order.status = "failed"
            return "Payment failed"


class Order:
    def __init__(self, total, card_number):
        self.total = total
        self.card_number = card_number
        self.status = "pending"


if __name__ == "__main__":
    order = Order(100.00, "4111111111111111")

    # Można łatwo przełączać między gateway'ami
    paypal_gateway = PayPalAdapter()
    stripe_gateway = StripeAdapter()

    # OrderService nie wie z którym API pracuje
    service_paypal = OrderService(paypal_gateway)
    service_stripe = OrderService(stripe_gateway)

    print(service_paypal.process_order(order))
    print(service_stripe.process_order(Order(200.00, "4222222222222222")))
    print("✅ OrderService oddzielony od external APIs przez indirection")
