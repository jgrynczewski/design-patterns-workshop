"""
Flyweight Pattern - Product Data Optimization

>>> # Test factory - zwraca ten sam flyweight dla tych samych danych
>>> factory = ProductTypeFactory()
>>> laptop1 = factory.get_product_type("Electronics", "Dell", {"CPU": "i7", "RAM": "16GB"})
>>> laptop2 = factory.get_product_type("Electronics", "Dell", {"CPU": "i7", "RAM": "16GB"})
>>> laptop1 is laptop2  # Ten sam obiekt w pamięci!
True
>>> factory.get_flyweight_count()
1

>>> # Test produktu z flyweight
>>> product = Product("DELL001", laptop1, 1500.0, 10)
>>> product.sku
'DELL001'
>>> product.price
1500.0

>>> # Test wyświetlania - łączenie intrinsic + extrinsic
>>> info = product.display_info()
>>> "Dell" in info and "DELL001" in info and "1500" in info
True
"""

from typing import Dict, Any


# ProductType (Flyweight) - CZĘŚCIOWO GOTOWE
# WZORZEC: Przechowuje intrinsic state (dane współdzielone)

class ProductType:
    """
    Flyweight przechowujący intrinsic state

    KLUCZOWE: Przechowuje TYLKO dane współdzielone (niezmienne)
    Wiele produktów może współdzielić ten sam ProductType
    """

    def __init__(self, category: str, brand: str, specifications: Dict[str, Any]):
        """Inicjalizuj flyweight z intrinsic state"""
        # TODO: Zapisz intrinsic state (dane współdzielone):
        # self.category = category
        # self.brand = brand
        # self.specifications = specifications
        pass

    def display_shared_info(self, sku: str, price: float, stock_quantity: int) -> str:
        """
        Wyświetl pełne info łącząc intrinsic state z extrinsic state

        KLUCZOWE: Flyweight otrzymuje extrinsic state jako parametry,
        nie przechowuje ich (bo są unikalne dla każdego produktu)
        """
        # TODO: Połącz intrinsic state (self.*) z extrinsic state (parametry)
        # Format: "SKU: {sku} | {brand} {category} | Price: ${price} | Stock: {stock} | Specs: ..."
        pass


# ProductTypeFactory - DO IMPLEMENTACJI
# WZORZEC: Zarządza pulą flyweights, zapobiega duplikatom

class ProductTypeFactory:
    """
    Factory zarządzający pulą flyweights

    KLUCZOWE: Zwraca istniejący flyweight lub tworzy nowy
    To eliminuje duplikację - ten sam typ = ten sam obiekt
    """

    def __init__(self):
        """Inicjalizuj factory z pustą pulą"""
        # TODO: Stwórz słownik do przechowywania flyweights
        # self._flyweights = {}
        pass

    def get_product_type(self, category: str, brand: str,
                        specifications: Dict[str, Any]) -> ProductType:
        """
        Zwróć flyweight dla podanych danych

        KLUCZOWE: Jeśli flyweight istnieje - zwróć go
        Jeśli nie - stwórz nowy i zapisz w puli
        """
        # TODO: Implementuj logikę factory:
        # 1. Stwórz klucz z parametrów (category, brand, frozenset(specifications.items()))
        # 2. Sprawdź czy flyweight już istnieje w self._flyweights
        # 3. Jeśli tak - zwróć istniejący
        # 4. Jeśli nie - stwórz nowy ProductType, zapisz w puli, zwróć
        pass

    def get_flyweight_count(self) -> int:
        """Zwróć liczbę flyweights w puli"""
        # TODO: return len(self._flyweights)
        pass


# Product (Context) - DO IMPLEMENTACJI
# WZORZEC: Przechowuje extrinsic state + referencję do flyweight

class Product:
    """
    Context przechowujący extrinsic state

    KLUCZOWE: Przechowuje TYLKO dane unikalne + referencję do flyweight
    Nie duplikuje intrinsic state - tylko wskazuje na współdzielony flyweight
    """

    def __init__(self, sku: str, product_type: ProductType,
                 price: float, stock_quantity: int):
        """Inicjalizuj produkt z extrinsic state i flyweight"""
        # TODO: Zapisz extrinsic state (dane unikalne):
        # self.sku = sku
        # self.price = price
        # self.stock_quantity = stock_quantity
        # self.product_type = product_type  # Referencja do flyweight
        pass

    def display_info(self) -> str:
        """Wyświetl pełne info o produkcie"""
        # TODO: Deleguj do flyweight, przekazując extrinsic state
        # return self.product_type.display_shared_info(self.sku, self.price, self.stock_quantity)
        pass

    def update_price(self, new_price: float) -> None:
        """Zaktualizuj cenę (extrinsic state)"""
        # TODO: self.price = new_price
        pass

    def update_stock(self, new_stock: int) -> None:
        """Zaktualizuj stan magazynowy (extrinsic state)"""
        # TODO: self.stock_quantity = new_stock
        pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     # Stwórz factory
#     factory = ProductTypeFactory()
#
#     # Specyfikacje laptopa Dell
#     dell_specs = {"CPU": "i7", "RAM": "16GB", "Storage": "512GB"}
#
#     # Stwórz wiele produktów tego samego typu
#     print("=== Tworzenie produktów ===")
#     products = []
#     for i in range(5):
#         # get_product_type zwróci TEN SAM flyweight dla tych samych danych
#         laptop_type = factory.get_product_type("Electronics", "Dell", dell_specs)
#         product = Product(f"DELL-{i:03d}", laptop_type, 1500 + i*50, 10 - i)
#         products.append(product)
#         print(product.display_info())
#
#     # Pokaż oszczędność pamięci
#     print(f"\n=== Statystyki ===")
#     print(f"Liczba produktów: {len(products)}")
#     print(f"Liczba flyweights: {factory.get_flyweight_count()}")
#     print(f"Oszczędność: {len(products)} produktów współdzieli {factory.get_flyweight_count()} flyweight(s)!")
#
#     # Sprawdź że wszystkie produkty mają ten sam flyweight
#     print(f"\n=== Weryfikacja współdzielenia ===")
#     first_type = products[0].product_type
#     all_same = all(p.product_type is first_type for p in products)
#     print(f"Wszystkie produkty współdzielą ten sam flyweight: {all_same}")
