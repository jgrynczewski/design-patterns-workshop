"""
Decorator Pattern - Discount System

>>> # Test podstawowego produktu
>>> laptop = BaseProduct("Gaming Laptop", 1000.0)
>>> laptop.get_price()
1000.0
>>> laptop.get_description()
'Gaming Laptop'

>>> # Test rabatu procentowego
>>> discounted = PercentageDiscount(laptop, 10)
>>> discounted.get_price()
900.0
>>> "10% off" in discounted.get_description()
True

>>> # Test stackowania rabatów
>>> laptop = BaseProduct("Phone", 800.0)
>>> step1 = PercentageDiscount(laptop, 15)  # 15% off -> $680
>>> step2 = FixedAmountDiscount(step1, 50)  # $50 off -> $630
>>> step3 = FreeShipping(step2)             # Free shipping
>>> step3.get_price()
630.0
>>> "15% off" in step3.get_description()
True
>>> "Free Shipping" in step3.get_description()
True
"""

from abc import ABC, abstractmethod


# Product Interface - GOTOWE
# Wspólny interfejs dla produktów i decoratorów

class Product(ABC):
    """Wspólny interfejs dla produktów i decoratorów"""

    @abstractmethod
    def get_price(self) -> float:
        """Zwróć cenę produktu (po zastosowaniu promocji)"""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Zwróć opis produktu (z informacjami o promocjach)"""
        pass


# BaseProduct - GOTOWE
# ConcreteComponent - podstawowy produkt bez promocji

class BaseProduct(Product):
    """Podstawowy produkt bez żadnych promocji"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.name


# Decorator - ROZWIĄZANIE
# WZORZEC: Kompozycja + Dziedziczenie + Delegacja

class DiscountDecorator(Product):
    """
    Bazowy dekorator dla wszystkich rodzajów promocji

    KLUCZOWE dla wzorca Decorator:
    1. DZIEDZICZENIE: DiscountDecorator(Product) - ten sam interfejs
    2. KOMPOZYCJA: przechowuje referencję do Product
    3. DELEGACJA: wywołuje metody wrappowanego produktu
    """

    def __init__(self, product: Product):
        """
        Inicjalizuj dekorator z wrappowanym produktem

        Args:
            product: Produkt do wrappowania (może być BaseProduct lub inny decorator)
        """
        self.product = product  # KOMPOZYCJA - przechowujemy referencję

    def get_price(self) -> float:
        """DELEGACJA - wywołaj metodę wrappowanego produktu"""
        return self.product.get_price()

    def get_description(self) -> str:
        """DELEGACJA - wywołaj metodę wrappowanego produktu"""
        return self.product.get_description()


# Concrete Decorators - ROZWIĄZANIE
# Nadpisują get_price() i/lub get_description() żeby dodać funkcjonalność

class PercentageDiscount(DiscountDecorator):
    """Dekorator rabatu procentowego"""

    def __init__(self, product: Product, percentage: float):
        """
        Inicjalizuj z produktem i procentem rabatu

        Args:
            product: Wrappowany produkt
            percentage: Procent rabatu (np. 10 dla 10%)
        """
        super().__init__(product)  # Wywołaj konstruktor bazowy
        self.percentage = percentage

    def get_price(self) -> float:
        """Zwróć cenę po zastosowaniu rabatu procentowego"""
        original_price = self.product.get_price()  # DELEGACJA
        return original_price * (1 - self.percentage / 100)  # MODYFIKACJA

    def get_description(self) -> str:
        """Zwróć opis z informacją o rabacie"""
        original_desc = self.product.get_description()  # DELEGACJA
        return f"{original_desc} ({self.percentage}% off)"  # MODYFIKACJA


class FixedAmountDiscount(DiscountDecorator):
    """Dekorator rabatu kwotowego"""

    def __init__(self, product: Product, amount: float):
        """
        Inicjalizuj z produktem i kwotą rabatu

        Args:
            product: Wrappowany produkt
            amount: Kwota rabatu w $
        """
        super().__init__(product)
        self.amount = amount

    def get_price(self) -> float:
        """Zwróć cenę po odjęciu kwoty rabatu"""
        original_price = self.product.get_price()  # DELEGACJA
        return max(0, original_price - self.amount)  # MODYFIKACJA (min 0)

    def get_description(self) -> str:
        """Zwróć opis z informacją o rabacie kwotowym"""
        original_desc = self.product.get_description()  # DELEGACJA
        return f"{original_desc} (${self.amount} off)"  # MODYFIKACJA


class FreeShipping(DiscountDecorator):
    """Dekorator darmowej dostawy (nie zmienia ceny, tylko opis)"""

    def get_price(self) -> float:
        """Zwróć cenę bez zmian (free shipping nie wpływa na cenę produktu)"""
        return self.product.get_price()  # DELEGACJA bez modyfikacji

    def get_description(self) -> str:
        """Zwróć opis z informacją o darmowej dostawie"""
        original_desc = self.product.get_description()  # DELEGACJA
        return f"{original_desc} + Free Shipping"  # MODYFIKACJA


# Przykład użycia
if __name__ == "__main__":
    # Podstawowy produkt
    laptop = BaseProduct("Gaming Laptop", 1000.0)
    print(f"{laptop.get_description()}: ${laptop.get_price()}")

    # Opakowywanie decoratorami
    step1 = PercentageDiscount(laptop, 10)  # 10% off -> $900
    print(f"{step1.get_description()}: ${step1.get_price()}")

    step2 = FixedAmountDiscount(step1, 50)  # $50 off -> $850
    print(f"{step2.get_description()}: ${step2.get_price()}")

    step3 = FreeShipping(step2)  # Free shipping
    print(f"{step3.get_description()}: ${step3.get_price()}")

    print("\n--- Black Friday Deal ---")
    phone = BaseProduct("Smartphone", 800.0)
    black_friday = FreeShipping(FixedAmountDiscount(PercentageDiscount(phone, 20), 50))
    print(f"{black_friday.get_description()}: ${black_friday.get_price()}")

    # Wzorzec Decorator pozwala dynamicznie opakowywać obiekt w funkcjonalności!
