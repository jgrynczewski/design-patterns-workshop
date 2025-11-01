# %% About
# - Name: Composite - Product Categories Tree
# - Difficulty: medium
# - Lines: 25
# - Minutes: 18
# - Focus: Composite pattern - tree structures with uniform interface

# %% Description
"""
Implementuj wzorzec Composite do budowy hierarchicznego drzewa
kategorii produktów z jednolitym interfejsem.

Zadanie: Stwórz strukturę gdzie produkty i kategorie mają ten sam interfejs
"""

# %% Hints
# - ProductComponent definiuje wspólny interfejs
# - Product (leaf) implementuje operacje dla pojedynczego produktu
# - Category (composite) agreguje operacje ze swoich children
# - Użyj rekurencji w Category dla operacji na całym drzewie

# %% Doctests
"""
>>> # Test podstawowy - single product
>>> laptop = Product("Gaming Laptop", 1500.0)
>>> laptop.get_price()
1500.0
>>> laptop.get_product_count()
1

>>> # Test category z produktami
>>> electronics = Category("Electronics")
>>> electronics.add_item(Product("Phone", 800.0))
>>> electronics.add_item(Product("Tablet", 400.0))
>>> electronics.get_price()
1200.0
>>> electronics.get_product_count()
2

>>> # Test zagnieżdżonych kategorii
>>> laptops = Category("Laptops")
>>> laptops.add_item(Product("Gaming Laptop", 1500.0))
>>> laptops.add_item(Product("Business Laptop", 1000.0))
>>> electronics.add_item(laptops)
>>> electronics.get_price()
3700.0
>>> electronics.get_product_count()
4
"""

# %% Imports
from abc import ABC, abstractmethod
from typing import List


# %% TODO: Implement ProductComponent Interface

class ProductComponent(ABC):
    """Wspólny interfejs dla produktów i kategorii"""

    @abstractmethod
    def get_price(self) -> float:
        """Zwróć cenę produktu lub sumę cen w kategorii"""
        pass

    @abstractmethod
    def get_product_count(self) -> int:
        """Zwróć liczbę produktów (1 dla produktu, suma dla kategorii)"""
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Wyświetl strukturę drzewa z wcięciami"""
        pass


# %% TODO: Implement Product (Leaf)

class Product:
    """Konkretny produkt - liść w drzewie"""

    def __init__(self, name: str, price: float):
        """Inicjalizuj produkt z nazwą i ceną"""
        # TODO: Zapisz name i price
        pass

    def get_price(self) -> float:
        """Zwróć cenę produktu"""
        # TODO: Zwróć self.price
        pass

    def get_product_count(self) -> int:
        """Produkt to zawsze 1 element"""
        # TODO: Zwróć 1
        pass

    def display(self, indent: int = 0) -> str:
        """Wyświetl produkt z wcięciem"""
        # TODO: Zwróć string w formacie: "  " * indent + f"Product: {self.name} (${self.price})"
        pass


# %% TODO: Implement Category (Composite)

class Category:
    """Kategoria - composite zawierający produkty i podkategorie"""

    def __init__(self, name: str):
        """Inicjalizuj kategorię z nazwą"""
        # TODO:
        # 1. Zapisz name
        # 2. Zainicjalizuj pustą listę children
        pass

    def add_item(self, item: ProductComponent) -> None:
        """Dodaj produkt lub podkategorię"""
        # TODO: Dodaj item do self.children
        pass

    def remove_item(self, item: ProductComponent) -> None:
        """Usuń produkt lub podkategorię"""
        # TODO:
        # 1. Sprawdź czy item jest w self.children
        # 2. Jeśli tak, usuń go
        pass

    def get_price(self) -> float:
        """Zwróć sumę cen wszystkich produktów w kategorii (rekurencyjnie)"""
        # TODO:
        # 1. Zainicjalizuj total = 0
        # 2. Dla każdego child w self.children:
        #    - Dodaj child.get_price() do total
        # 3. Zwróć total
        pass

    def get_product_count(self) -> int:
        """Zwróć liczbę wszystkich produktów w kategorii (rekurencyjnie)"""
        # TODO:
        # 1. Zainicjalizuj count = 0
        # 2. Dla każdego child w self.children:
        #    - Dodaj child.get_product_count() do count
        # 3. Zwróć count
        pass

    def display(self, indent: int = 0) -> str:
        """Wyświetl kategorię i wszystkie jej dzieci z wcięciami"""
        # TODO:
        # 1. Rozpocznij od: "  " * indent + f"Category: {self.name}"
        # 2. Dla każdego child w self.children:
        #    - Dodaj "\n" + child.display(indent + 1)
        # 3. Zwróć kompletny string
        pass

    def get_children(self) -> List[ProductComponent]:
        """Zwróć listę dzieci (do testów)"""
        # TODO: Zwróć self.children
        pass


# %% Example Usage (Optional)

def create_sample_catalog() -> Category:
    """Stwórz przykładowy katalog produktów"""
    # TODO (Opcjonalne - jeśli masz czas):
    # 1. Stwórz główną kategorię "Electronics"
    # 2. Dodaj produkty: "Phone" ($800), "Tablet" ($400)
    # 3. Stwórz podkategorię "Laptops"
    # 4. Dodaj do "Laptops": "Gaming Laptop" ($1500), "Business Laptop" ($1000)
    # 5. Dodaj kategorię "Laptops" do "Electronics"
    # 6. Zwróć główną kategorię
    pass
