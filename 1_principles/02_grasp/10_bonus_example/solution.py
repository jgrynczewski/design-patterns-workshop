"""
GRASP Bonus Example - Clean Solution
E-commerce system stosujący wszystkie zasady GRASP
"""

from abc import ABC, abstractmethod


# Domain Models
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    # Information Expert - CartItem zna swoje dane
    def get_total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    # Creator - Cart tworzy CartItem (zawiera items)
    def add_product(self, product_id, quantity, price):
        item = CartItem(product_id, quantity, price)
        self.items.append(item)

    # Information Expert - Cart ma items, więc oblicza total
    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)


# Polymorphism - Strategy pattern zamiast if/else
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"PayPal payment: ${amount}"


class StripePayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Stripe payment: ${amount}"


# Protected Variations - Interface chroni przed zmianami
class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, user_id, total):
        pass


class EmailService(ABC):
    @abstractmethod
    def send_confirmation(self, user_id):
        pass


# Pure Fabrications - Technical concerns
class DatabaseOrderRepository(OrderRepository):
    def save_order(self, user_id, total):
        print(f"INSERT INTO orders VALUES({user_id}, {total})")


class SendGridEmailService(EmailService):
    def send_confirmation(self, user_id):
        print(f"Sending confirmation email to user {user_id}")


# Indirection - Adapter for external payment APIs
class PaymentGateway:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        return self.payment_method.process_payment(amount)


# Controller - Orchestrates the checkout use case
class CheckoutController:
    def __init__(self, order_repo: OrderRepository, email_service: EmailService):
        self.order_repo = order_repo
        self.email_service = email_service

    # High Cohesion - tylko checkout logic
    def process_checkout(self, cart: ShoppingCart, user_id: int,
                         payment_gateway: PaymentGateway):
        total = cart.calculate_total()

        # Delegate to appropriate services
        payment_result = payment_gateway.process(total)
        self.order_repo.save_order(user_id, total)
        self.email_service.send_confirmation(user_id)

        return payment_result


# Low Coupling - Minimal dependencies, uses abstractions
class ECommerceService:
    def __init__(self, checkout_controller: CheckoutController):
        self.checkout_controller = checkout_controller

    def complete_purchase(self, cart: ShoppingCart, user_id: int,
                          payment_method: PaymentMethod):
        payment_gateway = PaymentGateway(payment_method)
        return self.checkout_controller.process_checkout(cart, user_id, payment_gateway)


if __name__ == "__main__":
    # Setup dependencies (Dependency Injection)
    order_repo = DatabaseOrderRepository()
    email_service = SendGridEmailService()
    checkout_controller = CheckoutController(order_repo, email_service)
    ecommerce_service = ECommerceService(checkout_controller)

    # Create cart and add items
    cart = ShoppingCart()
    cart.add_product(1, 2, 10.00)
    cart.add_product(2, 1, 25.00)

    # Process with different payment methods
    paypal = PayPalPayment()
    stripe = StripePayment()

    result1 = ecommerce_service.complete_purchase(cart, 123, paypal)
    result2 = ecommerce_service.complete_purchase(cart, 456, stripe)

    print(result1)
    print(result2)
    print("✅ Wszystkie zasady GRASP zastosowane poprawnie!")
    print("✅ Każda klasa ma jedną, spójną odpowiedzialność")
    print("✅ Łatwe testowanie, rozszerzanie i utrzymanie")
