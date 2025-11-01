"""
Testy dla Bridge Pattern - Payment Platform Abstraction
"""

import pytest
from starter import (
    Platform, WebPlatform, MobilePlatform, APIPlatform,
    PaymentGateway, PayPalGateway, StripeGateway
)


class TestPlatforms:
    """Testy konkretnych platform"""

    def test_web_platform_implementation(self):
        """Test implementacji Web Platform"""
        platform = WebPlatform()

        # Test authentication
        auth = platform.authenticate()
        assert auth == "web_session_cookie"

        # Test fee rate
        fee_rate = platform.get_platform_fee_rate()
        assert fee_rate == 0.02  # 2%

    def test_mobile_platform_implementation(self):
        """Test implementacji Mobile Platform"""
        platform = MobilePlatform()

        # Test authentication
        auth = platform.authenticate()
        assert auth == "biometric_auth_token"

        # Test fee rate
        fee_rate = platform.get_platform_fee_rate()
        assert fee_rate == 0.015  # 1.5%

    def test_api_platform_implementation(self):
        """Test implementacji API Platform"""
        platform = APIPlatform()

        # Test authentication
        auth = platform.authenticate()
        assert auth == "api_bearer_token"

        # Test fee rate
        fee_rate = platform.get_platform_fee_rate()
        assert fee_rate == 0.01  # 1%

    def test_platform_request_response_cycle(self):
        """Test cyklu request-response dla każdej platformy"""
        platforms = [
            (WebPlatform(), "web_transaction_id", "processed"),
            (MobilePlatform(), "mobile_payment_id", "success"),
            (APIPlatform(), "api_ref_id", "completed")
        ]

        for platform, id_field, status_field in platforms:
            # Test send_request
            test_data = {"amount": 100.0, "currency": "USD"}
            response = platform.send_request(test_data)

            assert isinstance(response, dict)
            assert id_field in response
            assert status_field in response
            assert response[status_field] is True

            # Test handle_response
            final_result = platform.handle_response(response)
            assert isinstance(final_result, dict)
            assert "status" in final_result
            assert "transaction_id" in final_result
            assert final_result["status"] == "success"


class TestPaymentGateways:
    """Testy payment gateways z różnymi platformami"""

    def test_paypal_gateway_with_web_platform(self):
        """Test PayPal gateway z Web platform"""
        platform = WebPlatform()
        gateway = PayPalGateway(platform)

        result = gateway.process_payment(100.0, "USD")

        assert isinstance(result, dict)
        assert "status" in result
        assert "transaction_id" in result
        assert "provider" in result
        assert result["status"] == "success"
        assert result["provider"] == "paypal"
        assert len(result["transaction_id"]) > 0

    def test_stripe_gateway_with_mobile_platform(self):
        """Test Stripe gateway z Mobile platform"""
        platform = MobilePlatform()
        gateway = StripeGateway(platform)

        result = gateway.process_payment(50.0, "EUR")

        assert isinstance(result, dict)
        assert "status" in result
        assert "transaction_id" in result
        assert "provider" in result
        assert result["status"] == "success"
        assert result["provider"] == "stripe"

    def test_paypal_gateway_with_api_platform(self):
        """Test PayPal gateway z API platform"""
        platform = APIPlatform()
        gateway = PayPalGateway(platform)

        result = gateway.process_payment(200.0, "PLN")

        assert result["status"] == "success"
        assert result["provider"] == "paypal"

    def test_stripe_gateway_with_web_platform(self):
        """Test Stripe gateway z Web platform"""
        platform = WebPlatform()
        gateway = StripeGateway(platform)

        result = gateway.process_payment(75.0, "GBP")

        assert result["status"] == "success"
        assert result["provider"] == "stripe"


class TestBridgePattern:
    """Testy wzorca Bridge - różne kombinacje gateway + platform"""

    def test_same_gateway_different_platforms(self):
        """Test tego samego gateway na różnych platformach"""
        platforms = [WebPlatform(), MobilePlatform(), APIPlatform()]
        results = []

        for platform in platforms:
            gateway = PayPalGateway(platform)
            result = gateway.process_payment(100.0, "USD")
            results.append(result)

        # Wszystkie powinny być successful
        for result in results:
            assert result["status"] == "success"
            assert result["provider"] == "paypal"

        # Transaction IDs powinny być różne (platform-specific)
        transaction_ids = [r["transaction_id"] for r in results]
        assert len(set(transaction_ids)) == len(transaction_ids)

    def test_different_gateways_same_platform(self):
        """Test różnych gateway na tej samej platformie"""
        platform = WebPlatform()

        paypal_result = PayPalGateway(platform).process_payment(100.0, "USD")
        stripe_result = StripeGateway(platform).process_payment(100.0, "USD")

        # Oba powinny być successful
        assert paypal_result["status"] == "success"
        assert stripe_result["status"] == "success"

        # Providers powinny być różne
        assert paypal_result["provider"] == "paypal"
        assert stripe_result["provider"] == "stripe"

        # Transaction IDs powinny być różne
        assert paypal_result["transaction_id"] != stripe_result["transaction_id"]

    def test_fees_calculation_different_platforms(self):
        """Test kalkulacji fees dla różnych platform"""
        amount = 100.0
        platforms_and_expected_fees = [
            (WebPlatform(), 2.0),  # 2%
            (MobilePlatform(), 1.5),  # 1.5%
            (APIPlatform(), 1.0)  # 1%
        ]

        for platform, expected_fee in platforms_and_expected_fees:
            gateway = PayPalGateway(platform)
            actual_fee = gateway.get_fees(amount)
            assert actual_fee == expected_fee


class TestPlatformAbstraction:
    """Testy abstrakcji Platform"""

    def test_all_platforms_implement_interface(self):
        """Test że wszystkie platformy implementują Platform interface"""
        platforms = [WebPlatform(), MobilePlatform(), APIPlatform()]

        for platform in platforms:
            assert isinstance(platform, Platform)

            # Test że wszystkie wymagane metody są dostępne
            assert hasattr(platform, 'authenticate')
            assert hasattr(platform, 'send_request')
            assert hasattr(platform, 'handle_response')
            assert hasattr(platform, 'get_platform_fee_rate')

    def test_platform_specific_behavior(self):
        """Test że każda platforma ma unikalne zachowanie"""
        platforms = [WebPlatform(), MobilePlatform(), APIPlatform()]

        # Test unikalnych auth methods
        auth_methods = [p.authenticate() for p in platforms]
        assert len(set(auth_methods)) == 3

        # Test unikalnych fee rates
        fee_rates = [p.get_platform_fee_rate() for p in platforms]
        assert len(set(fee_rates)) == 3


class TestGatewayAbstraction:
    """Testy abstrakcji PaymentGateway"""

    def test_gateway_holds_platform_reference(self):
        """Test że gateway trzyma referencję do platform (Bridge!)"""
        platform = WebPlatform()
        gateway = PayPalGateway(platform)

        # Gateway powinien mieć dostęp do platform
        assert hasattr(gateway, 'platform')
        assert gateway.platform == platform

    def test_gateway_delegates_to_platform(self):
        """Test że gateway deleguje operacje do platform"""
        platform = WebPlatform()
        gateway = PayPalGateway(platform)

        # Fees calculation should delegate to platform
        fees = gateway.get_fees(100.0)
        expected_fees = platform.get_platform_fee_rate() * 100.0
        assert fees == expected_fees


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
