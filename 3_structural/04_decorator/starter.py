# %% About
# - Name: Decorator - Discount System
# - Difficulty: medium
# - Lines: 20
# - Minutes: 15
# - Focus: Decorator pattern - adding behavior dynamically

# %% Description
"""
Implementuj wzorzec Decorator do dynamicznego dodawania rabatów
i promocji do produktów bez modyfikacji ich klasy.

Zadanie: Stwórz system stackowania różnych typów zniżek
"""

# %% Hints
# - Product interface definiuje wspólne metody
# - BaseProduct implementuje podstawową funkcjonalność
# - DiscountDecorator wrappuje Product i deleguje wywołania
# - Concrete decorators modyfikują wyniki przed zwróceniem

# %% Doctests
"""
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

# %% Imports
from abc import ABC, abstractmethod


# %% TODO: Implement Product Interface

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


# %% TODO: Implement BaseProduct (ConcreteComponent)

class BaseProduct:
    """Podstawowy produkt bez żadnych promocji"""

    def __init__(self, name: str, price: float):
        """Inicjalizuj produkt z nazwą i ceną"""
        # TODO: Zapisz name i price
        pass

    def get_price(self) -> float:
        """Zwróć podstawową cenę produktu"""
        # TODO: Zwróć self.price
        pass

    def get_description(self) -> str:
        """Zwróć nazwę produktu"""
        # TODO: Zwróć self.name
        pass


# %% TODO: Implement DiscountDecorator (Base Decorator)

class DiscountDecorator:
    """Bazowy dekorator dla wszystkich rodzajów promocji"""

    def __init__(self, product: Product):
        """Inicjalizuj dekorator z wrappowanym produktem"""
        # TODO: Zapisz product (composition!)
        pass

    def get_price(self) -> float:
        """Deleguj do wrappowanego produktu (domyślnie bez zmian)"""
        # TODO: Zwróć self.product.get_price()
        pass

    def get_description(self) -> str:
        """Deleguj do wrappowanego produktu (domyślnie bez zmian)"""
        # TODO: Zwróć self.product.get_description()
        pass


# %% TODO: Implement PercentageDiscount (Concrete Decorator)

class PercentageDiscount:
    """Dekorator rabatu procentowego"""

    def __init__(self, product: Product, percentage: float):
        """Inicjalizuj z produktem i procentem rabatu"""
        # TODO:
        # 1. Zapisz product (wrappowany produkt)
        # 2. Zapisz percentage (rabat w procentach, np. 10 dla 10%)
        pass

    def get_price(self) -> float:
        """Zwróć cenę po zastosowaniu rabatu procentowego"""
        # TODO:
        # 1. Pobierz cenę z self.product.get_price()
        # 2. Zastosuj rabat: price * (1 - percentage/100)
        # 3. Zwróć wynik
        pass

    def get_description(self) -> str:
        """Zwróć opis z informacją o rabacie"""
        # TODO:
        # 1. Pobierz opis z self.product.get_description()
        # 2. Dodaj info o rabacie: f" ({self.percentage}% off)"
        # 3. Zwróć połączony string
        pass


# %% TODO: Implement FixedAmountDiscount (Concrete Decorator)

class FixedAmountDiscount:
    """Dekorator rabatu kwotowego"""

    def __init__(self, product: Product, amount: float):
        """Inicjalizuj z produktem i kwotą rabatu"""
        # TODO:
        # 1. Zapisz product
        # 2. Zapisz amount (kwota rabatu w $)
        pass

    def get_price(self) -> float:
        """Zwróć cenę po odjęciu kwoty rabatu"""
        # TODO:
        # 1. Pobierz cenę z self.product.get_price()
        # 2. Odejmij rabat: price - self.amount
        # 3. Upewnij się że cena nie jest ujemna (max(0, result))
        # 4. Zwróć wynik
        pass

    def get_description(self) -> str:
        """Zwróć opis z informacją o rabacie kwotowym"""
        # TODO:
        # 1. Pobierz opis z self.product.get_description()
        # 2. Dodaj info: f" (${self.amount} off)"
        # 3. Zwróć połączony string
        pass


# %% TODO: Implement FreeShipping (Concrete Decorator)

class FreeShipping:
    """Dekorator darmowej dostawy (nie zmienia ceny, tylko opis)"""

    def __init__(self, product: Product):
        """Inicjalizuj z produktem"""
        # TODO: Zapisz product
        pass

    def get_price(self) -> float:
        """Zwróć cenę bez zmian (free shipping nie wpływa na cenę produktu)"""
        # TODO: Zwróć self.product.get_price()
        pass

    def get_description(self) -> str:
        """Zwróć opis z informacją o darmowej dostawie"""
        # TODO:
        # 1. Pobierz opis z self.product.get_description()
        # 2. Dodaj info: " + Free Shipping"
        # 3. Zwróć połączony string
        pass


# %% Example Usage (Optional)

def create_black_friday_deal(product: Product) -> Product:
    """Stwórz promocję Black Friday (opcjonalne)"""
    # TODO (Opcjonalne):
    # 1. Zastosuj 20% rabat
    # 2. Dodaj $10 off
    # 3. Dodaj free shipping
    # 4. Zwróć final decorated product
    pass
