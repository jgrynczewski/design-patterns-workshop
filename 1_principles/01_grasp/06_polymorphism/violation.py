"""
Polymorphism Violation - GRASP
Używanie if/else zamiast polimorfizmu do obsługi wariantów
"""


class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        # PROBLEM: Type checking zamiast polimorfizmu
        if payment_type == "credit_card":
            return self._process_credit_card(amount)
        elif payment_type == "paypal":
            return self._process_paypal(amount)
        elif payment_type == "bank_transfer":
            return self._process_bank_transfer(amount)
        else:
            raise ValueError("Unsupported payment type")
        # Każdy nowy typ = modyfikacja tej metody

    def _process_credit_card(self, amount):
        return f"Credit card payment: ${amount}"

    def _process_paypal(self, amount):
        return f"PayPal payment: ${amount}"

    def _process_bank_transfer(self, amount):
        return f"Bank transfer: ${amount}"


if __name__ == "__main__":
    processor = PaymentProcessor()
    print(processor.process_payment("credit_card", 100))
    print(processor.process_payment("paypal", 200))
    print("❌ Dodanie 'cryptocurrency' wymaga modyfikacji PaymentProcessor")
