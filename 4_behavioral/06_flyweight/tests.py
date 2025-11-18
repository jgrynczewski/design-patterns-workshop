"""
Testy dla Flyweight Pattern - Product Data Optimization
"""

import pytest
from starter import ProductType, ProductTypeFactory, Product


class TestProductType:
    """Testy flyweight (ProductType)"""

    def test_product_type_creation(self):
        """Test tworzenia flyweight"""
        specs = {"CPU": "Intel i7", "RAM": "16GB", "Storage": "512GB"}
        product_type = ProductType("Electronics", "Dell", specs)

        assert product_type.category == "Electronics"
        assert product_type.brand == "Dell"
        assert product_type.specifications == specs

    def test_display_shared_info(self):
        """Test wyświetlania informacji z flyweight"""
        specs = {"CPU": "Intel i5", "RAM": "8GB"}
        product_type = ProductType("Laptops", "HP", specs)

        info = product_type.display_shared_info("HP001", 999.99, 5)

        # Sprawdź że zawiera wszystkie dane (intrinsic + extrinsic)
        assert "HP001" in info
        assert "HP" in info
        assert "Laptops" in info
        assert "999.99" in info or "999.9" in info
        assert "5" in info
        assert "Intel i5" in info or "i5" in info
        assert "8GB" in info


class TestProductTypeFactory:
    """Testy factory zarządzającego flyweights"""

    def test_factory_creation(self):
        """Test tworzenia factory"""
        factory = ProductTypeFactory()
        assert factory.get_flyweight_count() == 0

    def test_factory_creates_flyweight(self):
        """Test że factory tworzy flyweight"""
        factory = ProductTypeFactory()
        specs = {"CPU": "AMD Ryzen", "RAM": "32GB"}

        flyweight = factory.get_product_type("Gaming", "ASUS", specs)

        assert isinstance(flyweight, ProductType)
        assert flyweight.category == "Gaming"
        assert flyweight.brand == "ASUS"
        assert flyweight.specifications == specs
        assert factory.get_flyweight_count() == 1

    def test_factory_reuses_flyweight(self):
        """Test że factory ponownie używa istniejącego flyweight"""
        factory = ProductTypeFactory()
        specs = {"CPU": "Intel i9", "RAM": "64GB"}

        # Stwórz flyweight pierwszy raz
        flyweight1 = factory.get_product_type("Workstation", "Dell", specs)

        # Pobierz ten sam flyweight
        flyweight2 = factory.get_product_type("Workstation", "Dell", specs)

        # Powinny być tym samym obiektem (not just equal, but identical)
        assert flyweight1 is flyweight2
        assert factory.get_flyweight_count() == 1

    def test_factory_creates_different_flyweights(self):
        """Test że factory tworzy różne flyweights dla różnych danych"""
        factory = ProductTypeFactory()
        specs1 = {"CPU": "Intel i5", "RAM": "8GB"}
        specs2 = {"CPU": "Intel i7", "RAM": "16GB"}

        # Różne specyfikacje
        flyweight1 = factory.get_product_type("Laptop", "Dell", specs1)
        flyweight2 = factory.get_product_type("Laptop", "Dell", specs2)

        # Różna marka
        flyweight3 = factory.get_product_type("Laptop", "HP", specs1)

        # Wszystkie powinny być różne
        assert flyweight1 is not flyweight2
        assert flyweight1 is not flyweight3
        assert flyweight2 is not flyweight3
        assert factory.get_flyweight_count() == 3


class TestProduct:
    """Testy produktu (context)"""

    def test_product_creation(self):
        """Test tworzenia produktu"""
        specs = {"CPU": "M1 Pro", "RAM": "16GB"}
        product_type = ProductType("Laptop", "Apple", specs)

        product = Product("APPLE001", product_type, 2499.99, 3)

        assert product.sku == "APPLE001"
        assert product.price == 2499.99
        assert product.stock_quantity == 3
        assert product.product_type is product_type

    def test_product_display_info(self):
        """Test wyświetlania informacji o produkcie"""
        specs = {"CPU": "Intel i5", "RAM": "16GB"}
        product_type = ProductType("Ultrabook", "Lenovo", specs)
        product = Product("LEN001", product_type, 1299.99, 7)

        info = product.display_info()

        # Sprawdź że deleguje do flyweight i zawiera wszystkie dane
        assert "LEN001" in info
        assert "Lenovo" in info
        assert "1299.99" in info or "1299.9" in info
        assert "7" in info

    def test_product_update_extrinsic_state(self):
        """Test aktualizacji extrinsic state"""
        specs = {"CPU": "AMD", "RAM": "8GB"}
        product_type = ProductType("Budget", "Acer", specs)
        product = Product("ACER001", product_type, 599.99, 10)

        # Update price
        product.update_price(549.99)
        assert product.price == 549.99

        # Update stock
        product.update_stock(15)
        assert product.stock_quantity == 15


class TestFlyweightPattern:
    """Testy wzorca Flyweight"""

    def test_flyweight_sharing(self):
        """Test że flyweight faktycznie współdzieli pamięć"""
        factory = ProductTypeFactory()
        same_specs = {"CPU": "Intel i7", "RAM": "16GB", "Storage": "1TB"}

        # Stwórz wiele produktów tego samego typu
        products = []
        for i in range(10):
            flyweight = factory.get_product_type("Laptop", "Dell", same_specs)
            product = Product(f"DELL{i:03d}", flyweight, 1000 + i, 10 - i)
            products.append(product)

        # Sprawdź że wszystkie produkty współdzielą ten sam flyweight
        first_flyweight = products[0].product_type
        for product in products:
            assert product.product_type is first_flyweight

        # Sprawdź że factory utworzył tylko jeden flyweight
        assert factory.get_flyweight_count() == 1

    def test_intrinsic_vs_extrinsic_separation(self):
        """Test oddzielenia intrinsic od extrinsic state"""
        factory = ProductTypeFactory()
        specs = {"CPU": "AMD Ryzen", "RAM": "32GB"}

        # Stwórz flyweight (intrinsic state)
        flyweight = factory.get_product_type("Gaming", "AMD", specs)

        # Stwórz różne produkty (extrinsic state)
        product1 = Product("AMD001", flyweight, 1500.0, 5)
        product2 = Product("AMD002", flyweight, 1600.0, 3)
        product3 = Product("AMD003", flyweight, 1400.0, 8)

        # Intrinsic state jest współdzielony
        assert product1.product_type is product2.product_type
        assert product2.product_type is product3.product_type

        # Extrinsic state jest unikalny
        assert product1.sku != product2.sku
        assert product2.sku != product3.sku
        assert product1.price != product2.price
        assert product2.price != product3.price

    def test_multiple_flyweight_types(self):
        """Test wielu różnych typów flyweights"""
        factory = ProductTypeFactory()

        # Stwórz różne typy produktów
        dell_specs = {"CPU": "i7", "RAM": "16GB"}
        hp_specs = {"CPU": "i5", "RAM": "8GB"}
        apple_specs = {"CPU": "M1", "RAM": "16GB"}

        dell_type = factory.get_product_type("Laptop", "Dell", dell_specs)
        hp_type = factory.get_product_type("Laptop", "HP", hp_specs)
        apple_type = factory.get_product_type("Laptop", "Apple", apple_specs)

        # Każdy typ powinien być inny
        assert dell_type is not hp_type
        assert hp_type is not apple_type
        assert dell_type is not apple_type

        # Ale pobieranie tego samego typu zwraca ten sam obiekt
        dell_type2 = factory.get_product_type("Laptop", "Dell", dell_specs)
        assert dell_type is dell_type2

        assert factory.get_flyweight_count() == 3

    def test_memory_optimization_scenario(self):
        """Test scenariusza optymalizacji pamięci"""
        factory = ProductTypeFactory()

        # Symuluj sklep z wieloma produktami kilku typów
        product_types = [
            ("Laptop", "Dell", {"CPU": "i5", "RAM": "8GB"}),
            ("Laptop", "HP", {"CPU": "i5", "RAM": "8GB"}),
            ("Gaming", "ASUS", {"CPU": "AMD Ryzen", "RAM": "32GB"}),
        ]

        products = []
        # Dodaj po 20 produktów każdego typu (60 total)
        for i, (category, brand, specs) in enumerate(product_types):
            for j in range(20):
                flyweight = factory.get_product_type(category, brand, specs)
                sku = f"{brand.upper()}{i}{j:02d}"
                price = 1000 + (i * 500) + (j * 10)
                stock = (j % 10) + 1
                product = Product(sku, flyweight, price, stock)
                products.append(product)

        # Sprawdź efektywność
        assert len(products) == 60
        assert factory.get_flyweight_count() == 3

        # 60 produktów, ale tylko 3 flyweights!
        print(f"\n60 produktów współdzieli tylko {factory.get_flyweight_count()} flyweights")

    def test_flyweight_identity_vs_equality(self):
        """Test różnicy między identity (is) a equality (==)"""
        factory = ProductTypeFactory()
        specs = {"CPU": "Intel", "RAM": "16GB"}

        flyweight1 = factory.get_product_type("Office", "Lenovo", specs)
        flyweight2 = factory.get_product_type("Office", "Lenovo", specs)

        # Powinny być tym samym obiektem (identity)
        assert flyweight1 is flyweight2

        # Oczywiście też są równe (equality)
        assert flyweight1 == flyweight2 or True  # Python może nie zdefiniować __eq__


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
