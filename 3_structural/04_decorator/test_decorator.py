"""
Testy dla Decorator Pattern - Discount System
"""

import pytest
from starter import (
    Product, BaseProduct, DiscountDecorator,
    PercentageDiscount, FixedAmountDiscount, FreeShipping,
    create_black_friday_deal
)


class TestBaseProduct:
    """Testy podstawowego produktu"""

    def test_base_product_creation(self):
        """Test tworzenia podstawowego produktu"""
        product = BaseProduct("Gaming Laptop", 1500.0)

        assert product.name == "Gaming Laptop"
        assert product.price == 1500.0

    def test_base_product_implements_interface(self):
        """Test że BaseProduct implementuje Product interface"""
        product = BaseProduct("Phone", 800.0)
        assert isinstance(product, Product)

    def test_base_product_get_price(self):
        """Test pobierania ceny podstawowego produktu"""
        product = BaseProduct("Tablet", 400.0)
        assert product.get_price() == 400.0

    def test_base_product_get_description(self):
        """Test pobierania opisu podstawowego produktu"""
        product = BaseProduct("Headphones", 200.0)
        assert product.get_description() == "Headphones"


class TestDiscountDecorator:
    """Testy bazowego dekoratora"""

    def test_discount_decorator_creation(self):
        """Test tworzenia bazowego dekoratora"""
        product = BaseProduct("Mouse", 50.0)
        decorator = DiscountDecorator(product)

        assert decorator.product == product

    def test_discount_decorator_implements_interface(self):
        """Test że DiscountDecorator implementuje Product interface"""
        product = BaseProduct("Keyboard", 100.0)
        decorator = DiscountDecorator(product)
        assert isinstance(decorator, Product)

    def test_discount_decorator_delegates_calls(self):
        """Test że bazowy dekorator deleguje wywołania"""
        product = BaseProduct("Monitor", 300.0)
        decorator = DiscountDecorator(product)

        # Powinien delegować bez zmian
        assert decorator.get_price() == 300.0
        assert decorator.get_description() == "Monitor"


class TestPercentageDiscount:
    """Testy rabatu procentowego"""

    def test_percentage_discount_creation(self):
        """Test tworzenia rabatu procentowego"""
        product = BaseProduct("Laptop", 1000.0)
        discount = PercentageDiscount(product, 10)

        assert discount.product == product
        assert discount.percentage == 10

    def test_percentage_discount_calculation(self):
        """Test kalkulacji rabatu procentowego"""
        product = BaseProduct("Phone", 800.0)
        discount = PercentageDiscount(product, 15)

        # 15% off z 800 = 680
        assert discount.get_price() == 680.0

    def test_percentage_discount_description(self):
        """Test opisu z rabatem procentowym"""
        product = BaseProduct("Tablet", 500.0)
        discount = PercentageDiscount(product, 20)

        description = discount.get_description()
        assert "Tablet" in description
        assert "20% off" in description

    def test_percentage_discount_edge_cases(self):
        """Test przypadków brzegowych rabatu procentowego"""
        product = BaseProduct("Item", 100.0)

        # 0% rabat
        no_discount = PercentageDiscount(product, 0)
        assert no_discount.get_price() == 100.0

        # 100% rabat
        full_discount = PercentageDiscount(product, 100)
        assert full_discount.get_price() == 0.0


class TestFixedAmountDiscount:
    """Testy rabatu kwotowego"""

    def test_fixed_amount_discount_creation(self):
        """Test tworzenia rabatu kwotowego"""
        product = BaseProduct("Laptop", 1200.0)
        discount = FixedAmountDiscount(product, 100)

        assert discount.product == product
        assert discount.amount == 100

    def test_fixed_amount_discount_calculation(self):
        """Test kalkulacji rabatu kwotowego"""
        product = BaseProduct("Phone", 600.0)
        discount = FixedAmountDiscount(product, 50)

        # $50 off z $600 = $550
        assert discount.get_price() == 550.0

    def test_fixed_amount_discount_description(self):
        """Test opisu z rabatem kwotowym"""
        product = BaseProduct("Headphones", 150.0)
        discount = FixedAmountDiscount(product, 25)

        description = discount.get_description()
        assert "Headphones" in description
        assert "$25 off" in description

    def test_fixed_amount_discount_no_negative_price(self):
        """Test że cena nie może być ujemna"""
        product = BaseProduct("Cheap Item", 30.0)
        discount = FixedAmountDiscount(product, 50)

        # Rabat większy niż cena - cena powinna być 0
        assert discount.get_price() == 0.0


class TestFreeShipping:
    """Testy darmowej dostawy"""

    def test_free_shipping_creation(self):
        """Test tworzenia darmowej dostawy"""
        product = BaseProduct("Book", 25.0)
        shipping = FreeShipping(product)

        assert shipping.product == product

    def test_free_shipping_price_unchanged(self):
        """Test że darmowa dostawa nie zmienia ceny"""
        product = BaseProduct("DVD", 15.0)
        shipping = FreeShipping(product)

        assert shipping.get_price() == 15.0

    def test_free_shipping_description(self):
        """Test opisu z darmową dostawą"""
        product = BaseProduct("Game", 60.0)
        shipping = FreeShipping(product)

        description = shipping.get_description()
        assert "Game" in description
        assert "Free Shipping" in description


class TestDecoratorStacking:
    """Testy stackowania decoratorów"""

    def test_two_decorators_stacking(self):
        """Test stackowania dwóch decoratorów"""
        product = BaseProduct("Laptop", 1000.0)

        # 10% off, potem $50 off
        step1 = PercentageDiscount(product, 10)  # $900
        step2 = FixedAmountDiscount(step1, 50)  # $850

        assert step2.get_price() == 850.0

    def test_three_decorators_stacking(self):
        """Test stackowania trzech decoratorów"""
        product = BaseProduct("Phone", 800.0)

        # 15% off -> $680, potem $30 off -> $650, potem free shipping
        step1 = PercentageDiscount(product, 15)
        step2 = FixedAmountDiscount(step1, 30)
        step3 = FreeShipping(step2)

        assert step3.get_price() == 650.0

        description = step3.get_description()
        assert "Phone" in description
        assert "15% off" in description
        assert "$30 off" in description
        assert "Free Shipping" in description

    def test_multiple_same_type_decorators(self):
        """Test stackowania tego samego typu decoratorów"""
        product = BaseProduct("Item", 1000.0)

        # Dwa rabaty procentowe: 10% potem 20%
        step1 = PercentageDiscount(product, 10)  # $900
        step2 = PercentageDiscount(step1, 20)  # $720 (20% z $900)

        assert step2.get_price() == 720.0

    def test_complex_stacking_scenario(self):
        """Test złożonego scenariusza stackowania"""
        product = BaseProduct("Gaming Setup", 2000.0)

        # Black Friday mega deal
        step1 = PercentageDiscount(product, 25)  # 25% off -> $1500
        step2 = FixedAmountDiscount(step1, 100)  # $100 off -> $1400
        step3 = PercentageDiscount(step2, 5)  # Extra 5% off -> $1330
        step4 = FreeShipping(step3)  # Free shipping

        assert step4.get_price() == 1330.0

        description = step4.get_description()
        assert all(text in description for text in [
            "Gaming Setup", "25% off", "$100 off", "5% off", "Free Shipping"
        ])

    def test_order_of_operations_matters(self):
        """Test że kolejność decoratorów ma znaczenie"""
        product = BaseProduct("Item", 1000.0)

        # Scenariusz A: Procent potem kwota
        scenario_a1 = PercentageDiscount(product, 10)  # $900
        scenario_a2 = FixedAmountDiscount(scenario_a1, 100)  # $800

        # Scenariusz B: Kwota potem procent
        scenario_b1 = FixedAmountDiscount(product, 100)  # $900
        scenario_b2 = PercentageDiscount(scenario_b1, 10)  # $810

        assert scenario_a2.get_price() == 800.0
        assert scenario_b2.get_price() == 810.0
        assert scenario_a2.get_price() != scenario_b2.get_price()


class TestDecoratorPattern:
    """Testy wzorca Decorator"""

    def test_decorator_composition(self):
        """Test kompozycji decoratorów"""
        product = BaseProduct("Test Product", 100.0)
        decorated = PercentageDiscount(product, 10)

        # Decorator powinien przechowywać referencję do produktu
        assert hasattr(decorated, 'product')
        assert decorated.product == product

    def test_transparent_interface(self):
        """Test przezroczystego interfejsu"""
        base_product = BaseProduct("Item", 200.0)
        decorated_product = PercentageDiscount(base_product, 15)

        # Oba powinny mieć ten sam interfejs
        for product in [base_product, decorated_product]:
            assert hasattr(product, 'get_price')
            assert hasattr(product, 'get_description')
            assert callable(product.get_price)
            assert callable(product.get_description)

    def test_runtime_flexibility(self):
        """Test elastyczności w runtime"""
        product = BaseProduct("Flexible Item", 500.0)

        # Możemy dynamicznie wybierać dekoratory
        decorators = [
            lambda p: PercentageDiscount(p, 10),
            lambda p: FixedAmountDiscount(p, 25),
            lambda p: FreeShipping(p)
        ]

        # Zastosuj wszystkie dekoratory
        result = product
        for decorator_func in decorators:
            result = decorator_func(result)

        # Wynik powinien mieć wszystkie dekoratory
        assert result.get_price() == 425.0  # (500 * 0.9) - 25 = 425
        description = result.get_description()
        assert all(text in description for text in [
            "10% off", "$25 off", "Free Shipping"
        ])


class TestBlackFridayDeal:
    """Testy Black Friday deal (jeśli zaimplementowany)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_black_friday_deal_creation(self):
        """Test tworzenia promocji Black Friday"""
        product = BaseProduct("Premium Item", 1000.0)
        deal = create_black_friday_deal(product)

        assert isinstance(deal, Product)
        assert deal.get_price() < 1000.0  # Powinien być tańszy

        description = deal.get_description()
        assert "20% off" in description
        assert "$10 off" in description
        assert "Free Shipping" in description


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
