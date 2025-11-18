"""
Adapter Pattern - Payment Systems Integration

>>> # Test PayPal adapter
>>> paypal_service = PayPalService()
>>> adapter = PayPalAdapter(paypal_service)
>>> result = adapter.process_payment(100.50, "USD")
>>> result["status"]
'success'
>>> len(result["transaction_id"]) > 0
True

>>> # Test Stripe adapter
>>> stripe_service = StripeService()
>>> adapter = StripeAdapter(stripe_service)
>>> result = adapter.process_payment(50.00, "EUR")
>>> result["status"]
'success'

>>> # Test Przelewy24 adapter
>>> p24_service = Przelewy24Service()
>>> adapter = Przelewy24Adapter(p24_service)
>>> result = adapter.process_payment(200.00, "PLN")
>>> result["status"]
'success'
"""

from abc import ABC, abstractmethod
import uuid
import random


# Mock External APIs - GOTOWE (nie modyfikuj)
# Te klasy symulują zewnętrzne API płatności - każde ma INNY interfejs

class PayPalService:
    """
    Mock PayPal API - GOTOWE

    Interfejs: make_payment(amount_cents: int, currency: str)
    Zwraca: {"payment_id": str, "status_code": int}
    """
    def make_payment(self, amount_cents: int, currency: str) -> dict:
        return {
            "payment_id": f"PAYPAL_{random.randint(1000, 9999)}",
            "status_code": 200 if amount_cents > 0 else 400
        }


class StripeService:
    """
    Mock Stripe API - GOTOWE

    Interfejs: charge(amount: float, currency: str, source: str)
    Zwraca: {"id": str, "paid": bool, "amount": float}
    """
    def charge(self, amount: float, currency: str, source: str = "card_token") -> dict:
        return {
            "id": f"ch_{uuid.uuid4().hex[:8]}",
            "paid": amount > 0,
            "amount": amount
        }


class Przelewy24Service:
    """
    Mock Przelewy24 API - GOTOWE

    Interfejs: create_transaction(amount: float, currency: str, merchant_id: str)
    Zwraca: {"transactionId": int, "success": bool}
    """
    def create_transaction(self, amount: float, currency: str, merchant_id: str = "12345") -> dict:
        return {
            "transactionId": random.randint(100000, 999999),
            "success": amount > 0 and currency == "PLN"
        }


# Target Interface - GOTOWE (nie modyfikuj)

class PaymentProcessor(ABC):
    """
    Wspólny interfejs dla wszystkich systemów płatności - GOTOWE

    To jest Target interface - wszystkie adaptery muszą go implementować.
    """

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> dict:
        """
        Przetwórz płatność i zwróć standardową odpowiedź

        Args:
            amount: Kwota płatności
            currency: Waluta (USD, EUR, PLN)

        Returns:
            dict: {"status": "success/failed", "transaction_id": "..."}
        """
        pass


# TODO: Zaimplementuj PayPalAdapter
# Dziedziczy po PaymentProcessor
# Kompozycja: zawiera PayPalService
# Metoda process_payment():
#   - Konwertuje parametry (amount → amount_cents)
#   - Wywołuje paypal_service.make_payment()
#   - Standaryzuje odpowiedź ({"status": ..., "transaction_id": ...})

class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_service: PayPalService):
        self.paypal_service = paypal_service

    def process_payment(self, amount: float, currency: str) -> dict:
        # Konwersja parametrów - PayPal wymaga kwoty w centach
        amount_cents = int(amount * 100)

        # Wywołanie API zewnętrznego serwisu
        response = self.paypal_service.make_payment(amount_cents, currency)

        # Standaryzacja odpowiedzi do wspólnego formatu
        if response["status_code"] == 200:
            return {"status": "success", "transaction_id": response["payment_id"]}
        else:
            return {"status": "failed", "transaction_id": None}


# TODO: Zaimplementuj StripeAdapter
# Dziedziczy po PaymentProcessor
# Kompozycja: zawiera StripeService
# Metoda process_payment():
#   - Wywołuje stripe_service.charge()
#   - Standaryzuje odpowiedź ({"status": ..., "transaction_id": ...})

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_service: StripeService):
        self.stripe_service = stripe_service

    def process_payment(self, amount: float, currency: str) -> dict:
        # Wywołanie API zewnętrznego serwisu
        response = self.stripe_service.charge(amount, currency)

        # Standaryzacja odpowiedzi do wspólnego formatu
        if response["paid"]:
            return {"status": "success", "transaction_id": response["id"]}
        else:
            return {"status": "failed", "transaction_id": None}


# TODO: Zaimplementuj Przelewy24Adapter
# Dziedziczy po PaymentProcessor
# Kompozycja: zawiera Przelewy24Service
# Metoda process_payment():
#   - Wywołuje p24_service.create_transaction()
#   - Standaryzuje odpowiedź ({"status": ..., "transaction_id": ...})

class Przelewy24Adapter(PaymentProcessor):
    def __init__(self, p24_service: Przelewy24Service):
        self.p24_service = p24_service

    def process_payment(self, amount: float, currency: str) -> dict:
        # Wywołanie API zewnętrznego serwisu
        response = self.p24_service.create_transaction(amount, currency)

        # Standaryzacja odpowiedzi do wspólnego formatu
        if response["success"]:
            return {"status": "success", "transaction_id": str(response["transactionId"])}
        else:
            return {"status": "failed", "transaction_id": None}


# Przykład użycia
if __name__ == "__main__":
    # Klient używa tylko interfejsu PaymentProcessor
    paypal = PayPalAdapter(PayPalService())
    stripe = StripeAdapter(StripeService())
    p24 = Przelewy24Adapter(Przelewy24Service())

    # Ten sam interfejs dla wszystkich!
    print(paypal.process_payment(100.50, "USD"))
    print(stripe.process_payment(50.00, "EUR"))
    print(p24.process_payment(200.00, "PLN"))
