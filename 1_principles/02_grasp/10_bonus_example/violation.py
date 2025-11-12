"""
GRASP Bonus Example - Multiple Violations
E-commerce system łamiący wszystkie zasady GRASP
"""

import requests


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCartManager:
    def __init__(self):
        self.cart_items = []
        self.db_connection = "mysql://localhost/shop"  # Low Coupling violation
        self.payment_api = "https://api.paypal.com"  # Low Coupling violation

    # Creator violation - kto powinien tworzyć CartItem?
    def add_product(self, product_id, quantity, price):
        item = CartItem(product_id, quantity, price)  # CartManager tworzy CartItem?
        self.cart_items.append(item)

    # Information Expert violation - kto ma informacje o items?
    def calculate_total(self):
        total = 0
        for item in self.cart_items:
            total += item.price * item.quantity  # Manager oblicza zamiast Cart
        return total

    # High Cohesion violation - zbyt wiele odpowiedzialności
    def process_checkout(self, user_id, payment_type):
        total = self.calculate_total()

        # Polymorphism violation - if/else zamiast polimorfizmu
        if payment_type == "paypal":
            result = self._process_paypal(total)
        elif payment_type == "stripe":
            result = self._process_stripe(total)
        else:
            raise ValueError("Unsupported payment")

        # Pure Fabrication violation - domain object z DB logic
        self._save_to_database(user_id, total)

        # Protected Variations violation - bezpośrednie API calls
        self._send_confirmation_email(user_id)

        return result

    def _process_paypal(self, amount):
        # Indirection violation - bezpośrednie dependency na PayPal
        response = requests.post(f"{self.payment_api}/charge",
                                 json={"amount": amount})
        return response.json()

    def _process_stripe(self, amount):
        response = requests.post("https://api.stripe.com/charges",
                                 json={"amount": amount * 100})
        return response.json()

    def _save_to_database(self, user_id, total):
        # Domain object nie powinien znać DB
        print(f"INSERT INTO orders VALUES({user_id}, {total})")

    def _send_confirmation_email(self, user_id):
        # Bezpośrednie dependency na email API
        requests.post("https://api.sendgrid.com/mail",
                      json={"to": f"user{user_id}@example.com"})


class CartItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price


if __name__ == "__main__":
    cart = ShoppingCartManager()
    cart.add_product(1, 2, 10.00)
    cart.add_product(2, 1, 25.00)

    print(f"Total: ${cart.calculate_total()}")
    print("❌ WSZYSTKIE zasady GRASP naruszone w jednej klasie!")
    print("❌ ShoppingCartManager robi za dużo i zna za dużo")
