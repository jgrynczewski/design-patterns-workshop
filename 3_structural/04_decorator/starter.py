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


# Decorator - DO IMPLEMENTACJI
# WZORZEC: Kompozycja + Dziedziczenie + Delegacja

# TODO: Zaimplementuj DiscountDecorator
# KLUCZOWE dla wzorca Decorator:
# 1. DZIEDZICZENIE: class DiscountDecorator(Product) - ten sam interfejs co Product
# 2. KOMPOZYCJA: __init__(self, product: Product) - wrappuje Product
# 3. DELEGACJA: get_price() i get_description() wywołują self.product.get_price()
#
# Bazowy dekorator tylko deleguje (bez modyfikacji) - konkretne dekoratory nadpiszą metody

class DiscountDecorator:
    pass


# Concrete Decorators - DO IMPLEMENTACJI
# Nadpisują get_price() i/lub get_description() żeby dodać funkcjonalność

# TODO: Zaimplementuj PercentageDiscount
# Dziedziczy po DiscountDecorator
# __init__(self, product: Product, percentage: float) - dodatkowo zapisz percentage
# get_price() - pobierz cenę z self.product, zastosuj rabat procentowy
# get_description() - pobierz opis z self.product, dodaj " ({percentage}% off)"

class PercentageDiscount:
    pass


# TODO: Zaimplementuj FixedAmountDiscount
# Dziedziczy po DiscountDecorator
# __init__(self, product: Product, amount: float) - dodatkowo zapisz amount
# get_price() - pobierz cenę z self.product, odejmij amount (min 0)
# get_description() - pobierz opis z self.product, dodaj " (${amount} off)"

class FixedAmountDiscount:
    pass


# TODO: Zaimplementuj FreeShipping
# Dziedziczy po DiscountDecorator
# __init__(self, product: Product) - tylko product (bez dodatkowych parametrów)
# get_price() - deleguj bez zmian (free shipping nie wpływa na cenę)
# get_description() - pobierz opis z self.product, dodaj " + Free Shipping"

class FreeShipping:
    pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     # Podstawowy produkt
#     laptop = BaseProduct("Gaming Laptop", 1000.0)
#     print(f"{laptop.get_description()}: ${laptop.get_price()}")
#
#     # Opakowywanie decoratorami
#     step1 = PercentageDiscount(laptop, 10)  # 10% off -> $900
#     print(f"{step1.get_description()}: ${step1.get_price()}")
#
#     step2 = FixedAmountDiscount(step1, 50)  # $50 off -> $850
#     print(f"{step2.get_description()}: ${step2.get_price()}")
#
#     step3 = FreeShipping(step2)  # Free shipping
#     print(f"{step3.get_description()}: ${step3.get_price()}")
#
#     print("\n--- Black Friday Deal ---")
#     phone = BaseProduct("Smartphone", 800.0)
#     black_friday = FreeShipping(FixedAmountDiscount(PercentageDiscount(phone, 20), 50))
#     print(f"{black_friday.get_description()}: ${black_friday.get_price()}")
#
#     # Wzorzec Decorator pozwala dynamicznie opakowywać obiekt w funkcjonalności!
