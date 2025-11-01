# %% About
# - Name: Flyweight - Product Data Optimization
# - Difficulty: hard
# - Lines: 25
# - Minutes: 20
# - Focus: Flyweight pattern - memory optimization through shared state

# %% Description
"""
Implementuj wzorzec Flyweight do optymalizacji pamięci dla tysięcy
produktów e-commerce przez współdzielenie powtarzających się danych.

Zadanie: Oddziel intrinsic state (współdzielony) od extrinsic state (unikalny)
"""

# %% Hints
# - ProductType (flyweight) = intrinsic state (category, brand, specs)
# - Product (context) = extrinsic state (sku, price, stock) + flyweight reference
# - Factory zarządza pulą flyweights, unika duplikatów
# - display_product_info() łączy intrinsic + extrinsic data

# %% Doctests
"""
>>> # Test factory - zwraca ten sam flyweight dla tych samych danych
>>> factory = ProductTypeFactory()
>>> laptop_type1 = factory.get_product_type("Electronics", "Dell", {"CPU": "i7", "RAM": "16GB"})
>>> laptop_type2 = factory.get_product_type("Electronics", "Dell", {"CPU": "i7", "RAM": "16GB"})
>>> laptop_type1 is laptop_type2
True

>>> # Test produktu z flyweight
>>> product = Product("DELL001", laptop_type1, 1500.0, 10)
>>> product.sku
'DELL001'
>>> product.price
1500.0

>>> # Test wyświetlania informacji (łączenie intrinsic + extrinsic)
>>> info = product.display_product_info()
>>> "Dell" in info and "DELL001" in info and "1500" in info
True
"""

# %% Imports
from typing import Dict, Any, List


# %% TODO: Implement ProductType (Flyweight)

class ProductType:
    """
    Flyweight przechowujący intrinsic state (dane współdzielone)
    """

    def __init__(self, category: str, brand: str, specifications: Dict[str, Any]):
        """Inicjalizuj flyweight z intrinsic state"""
        # TODO: Zapisz intrinsic state (dane współdzielone między produktami)
        # self.category = ...
        # self.brand = ...
        # self.specifications = ... (słownik z CPU, RAM, itp.)
        pass

    def display_shared_info(self, sku: str, price: float, stock_quantity: int) -> str:
        """
        Wyświetl informacje o produkcie łącząc intrinsic state (self)
        z extrinsic state (parametry)
        """
        # TODO:
        # 1. Połącz dane intrinsic (self.category, self.brand, self.specifications)
        # 2. z danymi extrinsic (sku, price, stock_quantity)
        # 3. Zwróć sformatowany string z pełnymi informacjami
        # Format: "SKU: {sku} | {brand} {category} | Price: ${price} | Stock: {stock} | Specs: {specs}"
        pass


# %% TODO: Implement ProductTypeFactory

class ProductTypeFactory:
    """Factory zarządzający pulą flyweights"""

    def __init__(self):
        """Inicjalizuj factory z pustą pulą flyweights"""
        # TODO: Stwórz słownik do przechowywania flyweights
        # Key: tuple(category, brand, frozenset(specifications.items()))
        # Value: ProductType instance
        pass

    def get_product_type(self, category: str, brand: str, specifications: Dict[str, Any]) -> ProductType:
        """
        Zwróć flyweight dla podanych danych.
        Jeśli nie istnieje, stwórz nowy. Jeśli istnieje, zwróć istniejący.
        """
        # TODO:
        # 1. Stwórz key z category, brand, specifications
        #    (użyj frozenset dla specifications żeby był hashable)
        # 2. Sprawdź czy flyweight już istnieje w self.flyweights
        # 3. Jeśli tak, zwróć istniejący
        # 4. Jeśli nie, stwórz nowy ProductType i zapisz w puli
        # 5. Zwróć flyweight
        pass

    def get_flyweight_count(self) -> int:
        """Zwróć liczbę utworzonych flyweights"""
        # TODO: Zwróć len(self.flyweights)
        pass

    def list_flyweights(self) -> List[str]:
        """Zwróć listę wszystkich flyweights (do debugowania)"""
        # TODO: Zwróć listę stringów opisujących flyweights
        # Format: [f"{brand} {category}", ...]
        pass


# %% TODO: Implement Product (Context)

class Product:
    """
    Context przechowujący extrinsic state + referencję do flyweight
    """

    def __init__(self, sku: str, product_type: ProductType, price: float, stock_quantity: int):
        """Inicjalizuj produkt z extrinsic state i flyweight reference"""
        # TODO: Zapisz extrinsic state (dane unikalne dla tego produktu)
        # self.sku = ...
        # self.price = ...
        # self.stock_quantity = ...
        # self.product_type = ... (reference do flyweight)
        pass

    def display_product_info(self) -> str:
        """Wyświetl pełne informacje o produkcie"""
        # TODO: Deleguj do flyweight, przekazując extrinsic state
        # return self.product_type.display_shared_info(...)
        pass

    def update_price(self, new_price: float) -> None:
        """Zaktualizuj cenę produktu (extrinsic state)"""
        # TODO: Zaktualizuj self.price
        pass

    def update_stock(self, new_stock: int) -> None:
        """Zaktualizuj stock produktu (extrinsic state)"""
        # TODO: Zaktualizuj self.stock_quantity
        pass


# %% TODO: Implement ProductCatalog

class ProductCatalog:
    """Katalog przechowujący produkty i zarządzający flyweights"""

    def __init__(self):
        """Inicjalizuj katalog"""
        # TODO:
        # self.products = [] (lista produktów)
        # self.factory = ProductTypeFactory() (factory do flyweights)
        pass

    def add_product(self, sku: str, category: str, brand: str,
                    specifications: Dict[str, Any], price: float, stock_quantity: int) -> None:
        """Dodaj produkt do katalogu"""
        # TODO:
        # 1. Pobierz flyweight z factory
        # 2. Stwórz Product z flyweight i extrinsic state
        # 3. Dodaj do self.products
        pass

    def get_product_by_sku(self, sku: str) -> Product:
        """Znajdź produkt po SKU"""
        # TODO: Przeszukaj self.products i zwróć Product z matching SKU
        pass

    def get_products_by_brand(self, brand: str) -> List[Product]:
        """Znajdź wszystkie produkty danej marki"""
        # TODO: Przeszukaj produkty i zwróć listę z matching brand
        pass

    def display_catalog(self) -> str:
        """Wyświetl cały katalog"""
        # TODO: Dla każdego produktu wywołaj display_product_info()
        pass

    def get_memory_stats(self) -> Dict[str, int]:
        """Zwróć statystyki zużycia pamięci"""
        # TODO: Zwróć słownik z:
        # - "total_products": liczba produktów
        # - "flyweight_count": liczba flyweights
        # - "memory_savings": orientacyjne oszczędności w %
        pass


# %% Example Usage (Optional)

def create_sample_catalog() -> ProductCatalog:
    """Stwórz przykładowy katalog z wieloma produktami tego samego typu"""
    # TODO (Opcjonalne):
    # 1. Stwórz katalog
    # 2. Dodaj 10+ produktów tego samego typu (np. Dell laptopy)
    # 3. Dodaj kilka produktów innych typów
    # 4. Zwróć katalog
    #
    # To pokaże że mamy np. 50 produktów ale tylko 5 flyweights
    pass
