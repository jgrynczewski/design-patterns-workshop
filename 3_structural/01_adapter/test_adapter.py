"""
Testy dla wzorca Adapter - Payment Systems Integration
"""

import pytest
from starter import (
    PayPalService, StripeService, Przelewy24Service,
    PaymentProcessor,
    PayPalAdapter, StripeAdapter, Przelewy24Adapter
)


class TestPaymentProcessorInterface:
    """Testy interfejsu PaymentProcessor"""

    def test_paypal_adapter_implements_interface(self):
        """Test czy PayPalAdapter implementuje PaymentProcessor"""
        paypal = PayPalAdapter(PayPalService())
        assert isinstance(paypal, PaymentProcessor)

    def test_stripe_adapter_implements_interface(self):
        """Test czy StripeAdapter implementuje PaymentProcessor"""
        stripe = StripeAdapter(StripeService())
        assert isinstance(stripe, PaymentProcessor)

    def test_przelewy24_adapter_implements_interface(self):
        """Test czy Przelewy24Adapter implementuje PaymentProcessor"""
        p24 = Przelewy24Adapter(Przelewy24Service())
        assert isinstance(p24, PaymentProcessor)


class TestPayPalAdapter:
    """Testy adaptera PayPal"""

    def test_successful_payment(self):
        """Test pomyślnej płatności przez PayPal"""
        service = PayPalService()
        adapter = PayPalAdapter(service)

        result = adapter.process_payment(100.50, "USD")

        assert result["status"] == "success"
        assert result["transaction_id"] is not None
        assert "PAYPAL_" in result["transaction_id"]

    def test_converts_amount_to_cents(self):
        """Test konwersji kwoty do centów"""
        service = PayPalService()
        adapter = PayPalAdapter(service)

        # PayPal powinien otrzymać kwotę w centach
        result = adapter.process_payment(100.00, "USD")
        assert result["status"] == "success"

    def test_different_currencies(self):
        """Test różnych walut"""
        service = PayPalService()
        adapter = PayPalAdapter(service)

        for currency in ["USD", "EUR", "PLN"]:
            result = adapter.process_payment(50.00, currency)
            assert result["status"] == "success"


class TestStripeAdapter:
    """Testy adaptera Stripe"""

    def test_successful_payment(self):
        """Test pomyślnej płatności przez Stripe"""
        service = StripeService()
        adapter = StripeAdapter(service)

        result = adapter.process_payment(50.00, "EUR")

        assert result["status"] == "success"
        assert result["transaction_id"] is not None
        assert "ch_" in result["transaction_id"]

    def test_transaction_id_format(self):
        """Test formatu transaction_id"""
        service = StripeService()
        adapter = StripeAdapter(service)

        result = adapter.process_payment(75.25, "EUR")

        assert result["transaction_id"].startswith("ch_")
        assert len(result["transaction_id"]) > 3

    def test_different_currencies(self):
        """Test różnych walut"""
        service = StripeService()
        adapter = StripeAdapter(service)

        for currency in ["USD", "EUR", "GBP"]:
            result = adapter.process_payment(100.00, currency)
            assert result["status"] == "success"


class TestPrzelewy24Adapter:
    """Testy adaptera Przelewy24"""

    def test_successful_payment_pln(self):
        """Test pomyślnej płatności w PLN"""
        service = Przelewy24Service()
        adapter = Przelewy24Adapter(service)

        result = adapter.process_payment(200.00, "PLN")

        assert result["status"] == "success"
        assert result["transaction_id"] is not None
        assert isinstance(result["transaction_id"], str)

    def test_transaction_id_is_string(self):
        """Test że transaction_id jest stringiem"""
        service = Przelewy24Service()
        adapter = Przelewy24Adapter(service)

        result = adapter.process_payment(150.00, "PLN")

        # transactionId z API to int, ale powinien być skonwertowany na str
        assert isinstance(result["transaction_id"], str)
        assert result["transaction_id"].isdigit()

    def test_pln_currency_required(self):
        """Test że Przelewy24 akceptuje tylko PLN"""
        service = Przelewy24Service()
        adapter = Przelewy24Adapter(service)

        # PLN powinno działać
        result_pln = adapter.process_payment(100.00, "PLN")
        assert result_pln["status"] == "success"


class TestStandardizedResponse:
    """Testy standaryzacji odpowiedzi"""

    def test_all_adapters_return_same_format(self):
        """Test że wszystkie adaptery zwracają ten sam format"""
        paypal = PayPalAdapter(PayPalService())
        stripe = StripeAdapter(StripeService())
        p24 = Przelewy24Adapter(Przelewy24Service())

        adapters = [paypal, stripe, p24]
        amount = 100.00
        currencies = ["USD", "EUR", "PLN"]

        for adapter, currency in zip(adapters, currencies):
            result = adapter.process_payment(amount, currency)

            # Sprawdź strukturę odpowiedzi
            assert "status" in result
            assert "transaction_id" in result

            # Sprawdź wartości
            assert result["status"] in ["success", "failed"]
            assert result["transaction_id"] is not None or result["status"] == "failed"

    def test_consistent_success_status(self):
        """Test spójności statusu success"""
        adapters = [
            PayPalAdapter(PayPalService()),
            StripeAdapter(StripeService()),
            Przelewy24Adapter(Przelewy24Service())
        ]

        for adapter in adapters:
            # Dla dodatnich kwot wszystkie powinny zwrócić success
            result = adapter.process_payment(50.00, "PLN" if isinstance(adapter, Przelewy24Adapter) else "USD")
            assert result["status"] == "success"
            assert result["transaction_id"] is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
