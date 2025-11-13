# Problem bez wzorca Adapter
# Pokazuje chaos z bezpośrednim używaniem różnych API płatności

import random
import uuid


# Mock External APIs (do demonstracji)
class PayPalService:
    """Mock PayPal API - oczekuje kwoty w centach"""
    def make_payment(self, amount_cents: int, currency: str) -> dict:
        return {
            "payment_id": f"PAYPAL_{random.randint(1000, 9999)}",
            "status_code": 200 if amount_cents > 0 else 400
        }


class StripeService:
    """Mock Stripe API - zwraca obiekt charge"""
    def charge(self, amount: float, currency: str, source: str = "card_token") -> dict:
        return {
            "id": f"ch_{uuid.uuid4().hex[:8]}",
            "paid": amount > 0,
            "amount": amount
        }


class Przelewy24Service:
    """Mock Przelewy24 API - polski system płatności"""
    def create_transaction(self, amount: float, currency: str, merchant_id: str = "12345") -> dict:
        return {
            "transactionId": random.randint(100000, 999999),
            "success": amount > 0 and currency == "PLN"
        }


# ❌ PROBLEM: Wszystkie systemy płatności obsługiwane przez if/elif
class PaymentManager:
    """
    Manager płatności BEZ wzorca Adapter

    Problem: Każdy system płatności ma INNY interfejs i wymaga INNEJ logiki
    """

    def __init__(self):
        self.paypal = PayPalService()
        self.stripe = StripeService()
        self.p24 = Przelewy24Service()

    def process_payment(self, provider: str, amount: float, currency: str) -> dict:
        """❌ Wszystkie systemy płatności w jednym miejscu z if/elif"""

        if provider == "paypal":
            # PayPal wymaga kwoty w centach
            amount_cents = int(amount * 100)
            response = self.paypal.make_payment(amount_cents, currency)
            # Konwersja odpowiedzi PayPal
            if response["status_code"] == 200:
                return {"status": "success", "transaction_id": response["payment_id"]}
            else:
                return {"status": "failed", "transaction_id": None}

        elif provider == "stripe":
            # Stripe zwraca inny format odpowiedzi
            response = self.stripe.charge(amount, currency)
            # Konwersja odpowiedzi Stripe
            if response["paid"]:
                return {"status": "success", "transaction_id": response["id"]}
            else:
                return {"status": "failed", "transaction_id": None}

        elif provider == "przelewy24":
            # Przelewy24 ma jeszcze inny format
            response = self.p24.create_transaction(amount, currency)
            # Konwersja odpowiedzi Przelewy24
            if response["success"]:
                return {"status": "success", "transaction_id": str(response["transactionId"])}
            else:
                return {"status": "failed", "transaction_id": None}

        else:
            return {"status": "failed", "transaction_id": None}


# ❌ Przykład użycia
if __name__ == "__main__":
    manager = PaymentManager()

    # Działa, ale kod jest nieelastyczny
    result = manager.process_payment("paypal", 100.50, "USD")
    print(f"PayPal: {result['status']}")

    result = manager.process_payment("stripe", 50.00, "EUR")
    print(f"Stripe: {result['status']}")

    # ❌ Chcę dodać nowy system płatności (Apple Pay)?
    # Muszę EDYTOWAĆ metodę process_payment() (dodać elif)

    # ❌ Chcę testować tylko logikę PayPal w izolacji?
    # Muszę testować całą klasę PaymentManager

    # ❌ Każdy system ma inną logikę konwersji w tym samym miejscu
    # Trudne do utrzymania i rozszerzania


"""
Jakie problemy rozwiązuje Adapter?

1. ❌ Naruszenie Open/Closed Principle
   - Dodanie nowego systemu płatności wymaga EDYCJI process_payment()
   - Nie można rozszerzyć bez modyfikacji

2. ❌ Niekompatybilne interfejsy w jednym miejscu
   - PayPal: make_payment(amount_cents, currency) → status_code
   - Stripe: charge(amount, currency) → paid
   - Przelewy24: create_transaction(amount, currency) → success
   - Wszystkie wymagają różnej konwersji w jednej metodzie

3. ❌ Trudne testowanie
   - Testowanie każdego systemu wymaga testowania całej klasy
   - Nie można testować logiki konwersji w izolacji
   - Mocki wymagają patchowania całej metody

4. ❌ Naruszenie Single Responsibility Principle
   - PaymentManager odpowiada za zarządzanie płatnościami
   - PaymentManager zawiera logikę konwersji dla 3 różnych systemów
   - Zmiana w konwersji PayPal może zepsuć Stripe

5. ❌ Duplikacja struktury
   - Każdy elif ma podobną strukturę (call API, check status, convert)
   - Wspólny wzorzec powielony w każdej gałęzi

Jak Adapter to rozwiązuje?
1. Każdy system w osobnej klasie adaptera (PayPalAdapter, StripeAdapter, Przelewy24Adapter)
2. Każdy adapter implementuje PaymentProcessor interface
3. PaymentManager używa tylko interface, nie zna konkretnych systemów
4. Nowy system = nowy adapter, zero zmian w PaymentManager
"""
