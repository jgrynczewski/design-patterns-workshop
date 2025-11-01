"""
Testy dla Facade Pattern - Order Processing System
"""

import pytest
from starter import (
    InventoryService, PaymentService, ShippingService, NotificationService,
    OrderFacade, calculate_total
)


class TestSubsystems:
    """Testy podsystemów (sprawdzenie że działają poprawnie)"""

    def test_inventory_service(self):
        """Test serwisu magazynowego"""
        inventory = InventoryService()

        # Test sprawdzania stock
        items_available = [{"name": "Laptop", "quantity": 2}]
        assert inventory.check_stock(items_available) is True

        items_unavailable = [{"name": "Laptop", "quantity": 10}]
        assert inventory.check_stock(items_unavailable) is False

        # Test rezerwacji
        initial_stock = inventory.stock["Laptop"]
        assert inventory.reserve_items(items_available) is True
        assert inventory.stock["Laptop"] == initial_stock - 2

    def test_payment_service(self):
        """Test serwisu płatności"""
        payment = PaymentService()
        customer = {"name": "Test User", "email": "test@example.com"}

        # Test pomyślnej płatności
        result = payment.process_payment(customer, 1000.0)
        assert result["success"] is True
        assert result["transaction_id"] is not None

        # Test nieudanej płatności (> 5000)
        result = payment.process_payment(customer, 6000.0)
        assert result["success"] is False
        assert result["transaction_id"] is None

    def test_shipping_service(self):
        """Test serwisu dostaw"""
        shipping = ShippingService()
        customer = {"name": "Test User", "email": "test@example.com"}

        # Test pomyślnej dostawy
        items_small = [{"name": "Item", "quantity": 2}]
        result = shipping.arrange_delivery(customer, items_small)
        assert result["success"] is True
        assert result["tracking_number"] is not None

        # Test nieudanej dostawy (> 5 items)
        items_large = [{"name": "Item", "quantity": 6}]
        result = shipping.arrange_delivery(customer, items_large)
        assert result["success"] is False
        assert result["tracking_number"] is None

    def test_notification_service(self):
        """Test serwisu powiadomień"""
        notifications = NotificationService()
        customer = {"name": "Test User", "email": "test@example.com"}
        order_details = {"order_id": "TEST123", "total": 100.0}

        # Powiadomienia zawsze się udają
        result = notifications.send_confirmation(customer, order_details)
        assert result is True


class TestOrderFacade:
    """Testy głównego Facade"""

    def test_facade_initialization(self):
        """Test inicjalizacji facade"""
        facade = OrderFacade()

        # Facade powinien mieć wszystkie podsystemy
        assert hasattr(facade, 'inventory')
        assert hasattr(facade, 'payment')
        assert hasattr(facade, 'shipping')
        assert hasattr(facade, 'notifications')

    def test_successful_order(self):
        """Test pomyślnego złożenia zamówienia"""
        facade = OrderFacade()
        customer = {"name": "Jan Kowalski", "email": "jan@example.com"}
        items = [
            {"name": "Laptop", "price": 1000.0, "quantity": 1},
            {"name": "Phone", "price": 500.0, "quantity": 1}
        ]

        result = facade.place_order(customer, items)

        assert result["success"] is True
        assert len(result["order_id"]) > 0
        assert "ORDER_" in result["order_id"]
        assert "successfully" in result["message"].lower()

    def test_order_out_of_stock(self):
        """Test zamówienia gdy brak stock"""
        facade = OrderFacade()
        customer = {"name": "Test User", "email": "test@example.com"}

        # Próba zamówienia więcej niż dostępne
        items = [{"name": "Laptop", "price": 1000.0, "quantity": 10}]

        result = facade.place_order(customer, items)

        assert result["success"] is False
        assert result["order_id"] == ""
        assert "stock" in result["message"].lower()

    def test_order_payment_failure(self):
        """Test zamówienia gdy płatność się nie powiedzie"""
        facade = OrderFacade()
        customer = {"name": "Rich User", "email": "rich@example.com"}

        # Zamówienie za dużo (> 5000) - payment failure
        items = [{"name": "Laptop", "price": 6000.0, "quantity": 1}]

        result = facade.place_order(customer, items)

        assert result["success"] is False
        assert result["order_id"] == ""
        assert "payment" in result["message"].lower()

    def test_order_shipping_failure(self):
        """Test zamówienia gdy shipping się nie powiedzie"""
        facade = OrderFacade()
        customer = {"name": "Bulk Buyer", "email": "bulk@example.com"}

        # Zamówienie za dużo items (> 5 quantity) - shipping failure
        items = [{"name": "Phone", "price": 500.0, "quantity": 6}]

        result = facade.place_order(customer, items)

        assert result["success"] is False
        assert result["order_id"] == ""
        assert "shipping" in result["message"].lower()

    def test_order_with_multiple_items(self):
        """Test zamówienia z wieloma produktami"""
        facade = OrderFacade()
        customer = {"name": "Multi Buyer", "email": "multi@example.com"}
        items = [
            {"name": "Phone", "price": 800.0, "quantity": 1},
            {"name": "Tablet", "price": 400.0, "quantity": 2},
            {"name": "Monitor", "price": 300.0, "quantity": 1}
        ]

        result = facade.place_order(customer, items)

        assert result["success"] is True
        assert len(result["order_id"]) > 0


class TestFacadePattern:
    """Testy wzorca Facade"""

    def test_facade_simplifies_complex_workflow(self):
        """Test że facade upraszcza złożony workflow"""
        facade = OrderFacade()

        # Jeden prosty wywołanie zamiast wielu kroków
        customer = {"name": "Simple User", "email": "simple@example.com"}
        items = [{"name": "Tablet", "price": 400.0, "quantity": 1}]

        result = facade.place_order(customer, items)

        # Facade powinien obsłużyć cały proces
        assert isinstance(result, dict)
        assert "success" in result
        assert "order_id" in result
        assert "message" in result

    def test_facade_encapsulates_subsystem_complexity(self):
        """Test że facade enkapsuluje złożoność podsystemów"""
        facade = OrderFacade()

        # Użytkownik nie musi znać podsystemów
        customer = {"name": "Unaware User", "email": "unaware@example.com"}
        items = [{"name": "Monitor", "price": 250.0, "quantity": 1}]

        # Jeden wywołanie obsługuje wszystkie podsystemy
        result = facade.place_order(customer, items)

        # Wynik jest spójny niezależnie od internal complexity
        assert result["success"] in [True, False]
        if result["success"]:
            assert len(result["order_id"]) > 0
        else:
            assert len(result["message"]) > 0

    def test_facade_provides_unified_interface(self):
        """Test że facade zapewnia zunifikowany interfejs"""
        facade = OrderFacade()

        # Ten sam interfejs dla różnych scenariuszy
        test_cases = [
            # Successful order
            {
                "customer": {"name": "User1", "email": "user1@example.com"},
                "items": [{"name": "Phone", "price": 500.0, "quantity": 1}]
            },
            # Failed order (out of stock)
            {
                "customer": {"name": "User2", "email": "user2@example.com"},
                "items": [{"name": "Laptop", "price": 1000.0, "quantity": 20}]
            }
        ]

        for case in test_cases:
            result = facade.place_order(case["customer"], case["items"])

            # Wszystkie wyniki mają ten sam format
            assert isinstance(result, dict)
            assert set(result.keys()) == {"success", "order_id", "message"}
            assert isinstance(result["success"], bool)
            assert isinstance(result["order_id"], str)
            assert isinstance(result["message"], str)


class TestErrorHandling:
    """Testy obsługi błędów"""

    def test_facade_handles_subsystem_failures_gracefully(self):
        """Test że facade gracefully obsługuje błędy podsystemów"""
        facade = OrderFacade()
        customer = {"name": "Error Test", "email": "error@example.com"}

        # Test różnych scenariuszy błędów
        error_scenarios = [
            # Out of stock
            [{"name": "NonExistent", "price": 100.0, "quantity": 1}],
            # Payment too high
            [{"name": "Laptop", "price": 10000.0, "quantity": 1}],
            # Too many items for shipping
            [{"name": "Phone", "price": 500.0, "quantity": 10}]
        ]

        for items in error_scenarios:
            result = facade.place_order(customer, items)

            # Wszystkie błędy są gracefully handled
            assert result["success"] is False
            assert result["order_id"] == ""
            assert len(result["message"]) > 0

    def test_facade_rollback_on_failure(self):
        """Test rollback gdy proces się nie powiedzie"""
        facade = OrderFacade()
        customer = {"name": "Rollback Test", "email": "rollback@example.com"}

        # Scenariusz: stock OK, payment OK, shipping FAIL
        items = [{"name": "Phone", "price": 500.0, "quantity": 8}]  # Za dużo dla shipping

        # Sprawdź initial stock
        initial_stock = facade.inventory.stock.get("Phone", 0)

        result = facade.place_order(customer, items)

        # Order powinien się nie udać
        assert result["success"] is False

        # Stock powinien być przywrócony (rollback)
        # Sprawdź czy stock nie został trwale zmieniony
        # (to może wymagać dodatkowej implementacji rollback)


class TestHelperFunctions:
    """Testy helper functions (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_calculate_total(self):
        """Test funkcji obliczającej total"""
        items = [
            {"name": "Item1", "price": 100.0, "quantity": 2},
            {"name": "Item2", "price": 50.0, "quantity": 3}
        ]

        total = calculate_total(items)
        expected = (100.0 * 2) + (50.0 * 3)  # 350.0
        assert total == expected

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_get_order_status(self):
        """Test pobierania statusu zamówienia"""
        facade = OrderFacade()

        # Najpierw złóż zamówienie
        customer = {"name": "Status Test", "email": "status@example.com"}
        items = [{"name": "Laptop", "price": 1000.0, "quantity": 1}]
        result = facade.place_order(customer, items)

        if result["success"]:
            order_id = result["order_id"]
            status = facade.get_order_status(order_id)
            assert isinstance(status, dict)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
