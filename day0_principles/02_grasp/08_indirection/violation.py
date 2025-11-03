"""
Indirection Violation - GRASP
Bezpośrednie dependency na external systems
"""

import requests


class OrderService:
    def __init__(self):
        # PROBLEM: Bezpośrednia dependency na PayPal API
        self.payment_api_url = "https://api.paypal.com/v1/payments"
        self.api_key = "pk_test_12345"

    def process_order(self, order):
        # PROBLEM: OrderService zna PayPal API szczegóły
        payment_data = {
            "amount": order.total,
            "currency": "USD",
            "card_number": order.card_number,
            "api_key": self.api_key
        }

        # Bezpośrednie wywołanie external API
        response = requests.post(self.payment_api_url, json=payment_data)

        if response.status_code == 200:
            order.status = "paid"
            return "Payment successful"
        else:
            order.status = "failed"
            return "Payment failed"
        # Co się stanie gdy PayPal zmieni API?


class Order:
    def __init__(self, total, card_number):
        self.total = total
        self.card_number = card_number
        self.status = "pending"


if __name__ == "__main__":
    order = Order(100.00, "4111111111111111")
    service = OrderService()

    # Symulacja - bez prawdziwego API call
    print(f"Order status: {order.status}")
    print("❌ OrderService bezpośrednio zależy od PayPal API")
    print("❌ Zmiana na Stripe wymaga modyfikacji OrderService")
