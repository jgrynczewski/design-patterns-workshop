"""Główny procesor zamówień"""
from interfaces.order_processing import Validatable, DiscountCalculable, Persistable, Notifiable, Payable
from domain.customer import Customer


class OrderProcessor:
    """Czysta implementacja używająca wszystkich zasad SOLID"""

    def __init__(self,
                 validator: Validatable,
                 discount_calculator: DiscountCalculable,
                 persistence: Persistable,
                 notifier: Notifiable,
                 payment_processor: Payable):
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
        if customer.can_receive_discount():
            strategy = customer.get_discount_strategy()
            total += strategy.calculate_discount(100)
    return total
