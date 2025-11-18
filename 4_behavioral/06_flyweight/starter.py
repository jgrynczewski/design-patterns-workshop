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


# ProductType (Flyweight) - ROZWIĄZANIE
# WZORZEC: Przechowuje intrinsic state (dane współdzielone)

class ProductType:
    """
    Flyweight przechowujący intrinsic state

    KLUCZOWE dla wzorca Flyweight:
    1. INTRINSIC STATE: Przechowuje TYLKO dane współdzielone (category, brand, specs)
    2. NIEZMIENNOŚĆ: Flyweight powinien być niemutowalny (immutable)
    3. WSPÓŁDZIELENIE: Jeden flyweight jest używany przez wiele kontekstów
    """

    def __init__(self, category: str, brand: str, specifications: Dict[str, Any]):
        """Inicjalizuj flyweight z intrinsic state"""
        # Intrinsic state - dane współdzielone między produktami
        self.category = category
        self.brand = brand
        self.specifications = specifications

    def display_shared_info(self, sku: str, price: float, stock_quantity: int) -> str:
        """
        Wyświetl pełne info łącząc intrinsic state z extrinsic state

        KLUCZOWE: Flyweight otrzymuje extrinsic state jako parametry,
        nie przechowuje ich (bo są unikalne dla każdego produktu)
        """
        # Połączenie intrinsic (self.*) z extrinsic (parametry)
        specs_str = ", ".join(f"{k}: {v}" for k, v in self.specifications.items())
        return (
            f"SKU: {sku} | "
            f"{self.brand} {self.category} | "
            f"Price: ${price} | "
            f"Stock: {stock_quantity} | "
            f"Specs: {specs_str}"
        )


# ProductTypeFactory - ROZWIĄZANIE
# WZORZEC: Zarządza pulą flyweights, zapobiega duplikatom

class ProductTypeFactory:
    """
    Factory zarządzający pulą flyweights

    KLUCZOWE dla wzorca Flyweight:
    1. PULA FLYWEIGHTS: Słownik przechowujący utworzone flyweights
    2. SPRAWDZANIE ISTNIENIA: Przed utworzeniem sprawdza czy flyweight istnieje
    3. WSPÓŁDZIELENIE: Zwraca istniejący flyweight zamiast tworzyć nowy
    """

    def __init__(self):
        """Inicjalizuj factory z pustą pulą"""
        self._flyweights: Dict[tuple, ProductType] = {}

    def get_product_type(self, category: str, brand: str,
                        specifications: Dict[str, Any]) -> ProductType:
        """
        Zwróć flyweight dla podanych danych

        KLUCZOWE: Jeśli flyweight istnieje - zwróć go
        Jeśli nie - stwórz nowy i zapisz w puli
        """
        # Stwórz klucz hashable z parametrów
        # frozenset dla specifications (dict nie jest hashable)
        key = (category, brand, frozenset(specifications.items()))

        # Sprawdź czy flyweight już istnieje
        if key not in self._flyweights:
            # Nie istnieje - stwórz nowy i zapisz
            self._flyweights[key] = ProductType(category, brand, specifications)

        # Zwróć flyweight (istniejący lub nowo utworzony)
        return self._flyweights[key]

    def get_flyweight_count(self) -> int:
        """Zwróć liczbę flyweights w puli"""
        return len(self._flyweights)


# Product (Context) - ROZWIĄZANIE
# WZORZEC: Przechowuje extrinsic state + referencję do flyweight

class Product:
    """
    Context przechowujący extrinsic state

    KLUCZOWE dla wzorca Flyweight:
    1. EXTRINSIC STATE: Przechowuje TYLKO dane unikalne (sku, price, stock)
    2. REFERENCJA DO FLYWEIGHT: Wskazuje na współdzielony flyweight
    3. DELEGACJA: Przekazuje extrinsic state do flyweight gdy potrzeba
    """

    def __init__(self, sku: str, product_type: ProductType,
                 price: float, stock_quantity: int):
        """Inicjalizuj produkt z extrinsic state i flyweight"""
        # Extrinsic state - dane unikalne dla tego produktu
        self.sku = sku
        self.price = price
        self.stock_quantity = stock_quantity

        # Referencja do flyweight (intrinsic state)
        self.product_type = product_type

    def display_info(self) -> str:
        """Wyświetl pełne info o produkcie"""
        # Deleguj do flyweight, przekazując extrinsic state
        return self.product_type.display_shared_info(
            self.sku, self.price, self.stock_quantity
        )

    def update_price(self, new_price: float) -> None:
        """Zaktualizuj cenę (extrinsic state)"""
        self.price = new_price

    def update_stock(self, new_stock: int) -> None:
        """Zaktualizuj stan magazynowy (extrinsic state)"""
        self.stock_quantity = new_stock


# Przykład użycia
if __name__ == "__main__":
    # Stwórz factory
    factory = ProductTypeFactory()

    # Specyfikacje laptopa Dell
    dell_specs = {"CPU": "i7", "RAM": "16GB", "Storage": "512GB"}

    # Stwórz wiele produktów tego samego typu
    print("=== Tworzenie produktów ===")
    products = []
    for i in range(5):
        # get_product_type zwróci TEN SAM flyweight dla tych samych danych
        laptop_type = factory.get_product_type("Electronics", "Dell", dell_specs)
        product = Product(f"DELL-{i:03d}", laptop_type, 1500 + i*50, 10 - i)
        products.append(product)
        print(product.display_info())

    # Pokaż oszczędność pamięci
    print(f"\n=== Statystyki ===")
    print(f"Liczba produktów: {len(products)}")
    print(f"Liczba flyweights: {factory.get_flyweight_count()}")
    print(f"Oszczędność: {len(products)} produktów współdzieli {factory.get_flyweight_count()} flyweight(s)!")

    # Sprawdź że wszystkie produkty mają ten sam flyweight
    print(f"\n=== Weryfikacja współdzielenia ===")
    first_type = products[0].product_type
    all_same = all(p.product_type is first_type for p in products)
    print(f"Wszystkie produkty współdzielą ten sam flyweight: {all_same}")

    # Dodaj produkty innych typów
    print(f"\n=== Dodanie innych typów ===")
    hp_specs = {"CPU": "i5", "RAM": "8GB", "Storage": "256GB"}
    hp_type = factory.get_product_type("Electronics", "HP", hp_specs)
    hp_product = Product("HP-001", hp_type, 999.0, 15)
    products.append(hp_product)

    apple_specs = {"CPU": "M1", "RAM": "16GB", "Storage": "512GB"}
    apple_type = factory.get_product_type("Electronics", "Apple", apple_specs)
    apple_product = Product("APPLE-001", apple_type, 2499.0, 5)
    products.append(apple_product)

    print(f"Liczba produktów: {len(products)}")
    print(f"Liczba flyweights: {factory.get_flyweight_count()}")
    print(f"7 produktów, ale tylko {factory.get_flyweight_count()} flyweights!")
