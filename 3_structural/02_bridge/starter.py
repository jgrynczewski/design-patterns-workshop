# %% About
# - Name: Bridge - Payment Platform Abstraction
# - Difficulty: medium
# - Lines: 20
# - Minutes: 15
# - Focus: Bridge pattern - separating abstraction from implementation

# %% Description
"""
Implementuj wzorzec Bridge do oddzielenia abstrakcji systemu płatności
od implementacji konkretnej platformy (web/mobile/API).

Zadanie: Stwórz PaymentGateway (abstrakcja) i Platform (implementacja)
"""

# %% Hints
# - PaymentGateway zawiera referencję do Platform
# - Platform definiuje interface dla platform-specific operacji
# - Gateway deleguje operacje do Platform
# - Każda platforma ma inne fees i authentication

# %% Doctests
"""
>>> # Test PayPal na platformie Web
>>> web_platform = WebPlatform()
>>> paypal_web = PayPalGateway(web_platform)
>>> result = paypal_web.process_payment(100.0, "USD")
>>> result["status"]
'success'
>>> paypal_web.get_fees(100.0)
2.0

>>> # Test Stripe na platformie Mobile
>>> mobile_platform = MobilePlatform()
>>> stripe_mobile = StripeGateway(mobile_platform)
>>> result = stripe_mobile.process_payment(50.0, "EUR")
>>> result["status"]
'success'
>>> stripe_mobile.get_fees(50.0)
0.75

>>> # Test PayPal na platformie API
>>> api_platform = APIPlatform()
>>> paypal_api = PayPalGateway(api_platform)
>>> paypal_api.get_fees(200.0)
2.0
"""

# %% Imports
from abc import ABC, abstractmethod
import uuid


# %% TODO: Implement Platform Interface (Implementor)

class Platform(ABC):
    """Interface dla platform-specific implementacji"""

    @abstractmethod
    def authenticate(self) -> str:
        """Wykonaj authentication specyficzne dla platformy"""
        pass

    @abstractmethod
    def send_request(self, data: dict) -> dict:
        """Wyślij request używając platform-specific protokołu"""
        pass

    @abstractmethod
    def handle_response(self, response: dict) -> dict:
        """Obsłuż response w sposób specyficzny dla platformy"""
        pass

    @abstractmethod
    def get_platform_fee_rate(self) -> float:
        """Zwróć platform-specific fee rate (jako decimal)"""
        pass


# %% TODO: Implement Concrete Platforms

class WebPlatform:
    """Implementacja dla platformy webowej"""

    def authenticate(self) -> str:
        """Web authentication przez cookies"""
        # TODO: Zwróć "web_session_cookie"
        pass

    def send_request(self, data: dict) -> dict:
        """HTTP request dla web"""
        # TODO:
        # 1. Symuluj wysłanie HTTP request
        # 2. Zwróć response z web_transaction_id
        # 3. Format: {"web_transaction_id": "WEB_xxx", "processed": True}
        pass

    def handle_response(self, response: dict) -> dict:
        """Obsłuż web response"""
        # TODO:
        # 1. Sprawdź czy response["processed"] == True
        # 2. Zwróć standardowy format z transaction_id z response
        pass

    def get_platform_fee_rate(self) -> float:
        """Web platform fee: 2%"""
        # TODO: Zwróć 0.02 (2%)
        pass


class MobilePlatform:
    """Implementacja dla platformy mobilnej"""

    def authenticate(self) -> str:
        """Mobile authentication przez biometrics"""
        # TODO: Zwróć "biometric_auth_token"
        pass

    def send_request(self, data: dict) -> dict:
        """Mobile API request"""
        # TODO:
        # 1. Symuluj mobile API call
        # 2. Zwróć response z mobile_payment_id
        # 3. Format: {"mobile_payment_id": "MOB_xxx", "success": True}
        pass

    def handle_response(self, response: dict) -> dict:
        """Obsłuż mobile response"""
        # TODO:
        # 1. Sprawdź czy response["success"] == True
        # 2. Zwróć standardowy format z transaction_id z response
        pass

    def get_platform_fee_rate(self) -> float:
        """Mobile platform fee: 1.5%"""
        # TODO: Zwróć 0.015 (1.5%)
        pass


class APIPlatform:
    """Implementacja dla platformy API"""

    def authenticate(self) -> str:
        """API authentication przez token"""
        # TODO: Zwróć "api_bearer_token"
        pass

    def send_request(self, data: dict) -> dict:
        """Direct API call"""
        # TODO:
        # 1. Symuluj API call
        # 2. Zwróć response z api_ref_id
        # 3. Format: {"api_ref_id": "API_xxx", "completed": True}
        pass

    def handle_response(self, response: dict) -> dict:
        """Obsłuż API response"""
        # TODO:
        # 1. Sprawdź czy response["completed"] == True
        # 2. Zwróć standardowy format z transaction_id z response
        pass

    def get_platform_fee_rate(self) -> float:
        """API platform fee: 1%"""
        # TODO: Zwróć 0.01 (1%)
        pass


# %% TODO: Implement Payment Gateway Abstraction

class PaymentGateway(ABC):
    """Abstrakcja dla payment gateway"""

    def __init__(self, platform: Platform):
        """Inicjalizuj gateway z konkretną platformą (Bridge!)"""
        # TODO: Zapisz platform
        pass

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> dict:
        """Przetworz płatność używając bridge do platform"""
        pass

    def get_fees(self, amount: float) -> float:
        """Oblicz fees na podstawie platformy"""
        # TODO:
        # 1. Pobierz platform fee rate z self.platform
        # 2. Zwróć amount * fee_rate
        pass


# %% TODO: Implement Concrete Gateways

class PayPalGateway:
    """PayPal gateway używający różnych platform przez Bridge"""

    def __init__(self, platform: Platform):
        # TODO: Zapisz platform (Bridge connection!)
        pass

    def process_payment(self, amount: float, currency: str) -> dict:
        """Przetworz płatność PayPal przez platformę"""
        # TODO:
        # 1. Wykonaj authentication przez platform
        # 2. Przygotuj PayPal-specific data: {"provider": "paypal", "amount": ..., "currency": ...}
        # 3. Wyślij request przez platform
        # 4. Obsłuż response przez platform
        # 5. Zwróć {"status": "success/failed", "transaction_id": "...", "provider": "paypal"}
        pass


class StripeGateway:
    """Stripe gateway używający różnych platform przez Bridge"""

    def __init__(self, platform: Platform):
        # TODO: Zapisz platform (Bridge connection!)
        pass

    def process_payment(self, amount: float, currency: str) -> dict:
        """Przetworz płatność Stripe przez platformę"""
        # TODO:
        # 1. Wykonaj authentication przez platform
        # 2. Przygotuj Stripe-specific data: {"provider": "stripe", "amount": ..., "currency": ...}
        # 3. Wyślij request przez platform
        # 4. Obsłuż response przez platform
        # 5. Zwróć {"status": "success/failed", "transaction_id": "...", "provider": "stripe"}
        pass
