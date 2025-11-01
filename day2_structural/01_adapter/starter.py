# %% About
# - Name: Adapter - Payment Systems Integration
# - Difficulty: easy
# - Lines: 15
# - Minutes: 12
# - Focus: Adapter pattern core concept

# %% Description
"""
Implementuj wzorzec Adapter do integracji różnych systemów płatności
z jednym wspólnym interfejsem w systemie e-commerce.

Zadanie: Stwórz adaptery dla PayPal, Stripe i Przelewy24 APIs
"""

# %% Hints
# - Każdy adapter implementuje PaymentProcessor interface
# - PayPal wymaga kwoty w centach (amount * 100)
# - Generuj transaction_id używając uuid lub random
# - Obsłuż różne formaty response z external APIs

# %% Doctests
"""
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

# %% Imports
from abc import ABC, abstractmethod
import uuid
import random


# %% Mock External APIs (już gotowe - nie modyfikuj)

class PayPalService:
    """Mock PayPal API - expects amount in cents"""

    def make_payment(self, amount_cents: int, currency: str) -> dict:
        return {
            "payment_id": f"PAYPAL_{random.randint(1000, 9999)}",
            "status_code": 200 if amount_cents > 0 else 400
        }


class StripeService:
    """Mock Stripe API - returns charge object"""

    def charge(self, amount: float, currency: str, source: str = "card_token") -> dict:
        return {
            "id": f"ch_{uuid.uuid4().hex[:8]}",
            "paid": amount > 0,
            "amount": amount
        }


class Przelewy24Service:
    """Mock Przelewy24 API - Polish payment system"""

    def create_transaction(self, amount: float, currency: str, merchant_id: str = "12345") -> dict:
        return {
            "transactionId": random.randint(100000, 999999),
            "success": amount > 0 and currency == "PLN"
        }


# %% TODO: Implement PaymentProcessor Interface

class PaymentProcessor(ABC):
    """Common interface for all payment systems"""

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> dict:
        """
        Process payment and return standardized response

        Returns:
            dict: {"status": "success/failed", "transaction_id": "..."}
        """
        pass


# %% TODO: Implement PayPal Adapter

class PayPalAdapter:
    """Adapter for PayPal payment system"""

    def __init__(self, paypal_service: PayPalService):
        # TODO: Store the paypal service
        pass

    def process_payment(self, amount: float, currency: str) -> dict:
        """Convert PayPal API response to standard format"""
        # TODO:
        # 1. Convert amount to cents (multiply by 100)
        # 2. Call paypal_service.make_payment()
        # 3. Convert response to standard format
        # 4. Return {"status": "success/failed", "transaction_id": "..."}
        pass


# %% TODO: Implement Stripe Adapter

class StripeAdapter:
    """Adapter for Stripe payment system"""

    def __init__(self, stripe_service: StripeService):
        # TODO: Store the stripe service
        pass

    def process_payment(self, amount: float, currency: str) -> dict:
        """Convert Stripe API response to standard format"""
        # TODO:
        # 1. Call stripe_service.charge()
        # 2. Check if payment was successful (paid == True)
        # 3. Convert response to standard format
        # 4. Return {"status": "success/failed", "transaction_id": "..."}
        pass


# %% TODO: Implement Przelewy24 Adapter

class Przelewy24Adapter:
    """Adapter for Przelewy24 payment system"""

    def __init__(self, p24_service: Przelewy24Service):
        # TODO: Store the p24 service
        pass

    def process_payment(self, amount: float, currency: str) -> dict:
        """Convert Przelewy24 API response to standard format"""
        # TODO:
        # 1. Call p24_service.create_transaction()
        # 2. Check if transaction was successful
        # 3. Convert response to standard format
        # 4. Return {"status": "success/failed", "transaction_id": "..."}
        pass


# %% Factory Function (Optional Enhancement)

def get_payment_processor(provider: str, service_instance) -> PaymentProcessor:
    """Factory function to get appropriate payment processor"""
    # TODO: Return appropriate adapter based on provider name
    # This is optional - implement if you have extra time
    pass
