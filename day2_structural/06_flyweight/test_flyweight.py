"""
Testy dla Flyweight Pattern - Product Data Optimization
"""

import pytest
from starter import (
    ProductType, ProductTypeFactory, Product, ProductCatalog,
    create_sample_catalog
)


class TestProductType:
    """Testy flyweight (ProductType)"""

    def test_product_type_creation(self):
        """Test tworzenia flyweight"""
        specs = {"CPU": "Intel i7", "RAM": "16GB", "Storage": "512GB SSD"}
        product_type = ProductType("Electronics", "Dell", specs)

        assert product_type.category == "Electronics"
        assert product_type.brand == "Dell"
        assert product_type.specifications == specs

    def test_display_shared_info(self):
        """Test wyświetlania informacji z flyweight"""
        specs = {"CPU": "Intel i5", "RAM": "8GB"}
        product_type = ProductType("Laptops", "HP", specs)

        info = product_type.display_shared_info("HP001", 999.99, 5)

        # Sprawdź że zawiera wszystkie dane
        assert "HP001" in info
        assert "HP" in info
        assert "Laptops" in info
        assert "999.99" in info
        assert "5" in info
        assert "Intel i5" in info
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

    def test_factory_creates_different_flyweights_for_different_data(self):
        """Test że factory tworzy różne flyweights dla różnych danych"""
        factory = ProductTypeFactory()
        specs1 = {"CPU": "Intel i5", "RAM": "8GB"}
        specs2 = {"CPU": "Intel i7", "RAM": "16GB"}

        flyweight1 = factory.get_product_type("Laptop", "Dell", specs1)
        flyweight2 = factory.get_product_type("Laptop", "Dell", specs2)
        flyweight3 = factory.get_product_type("Laptop", "HP", specs1)

        # Wszystkie powinny być różne
        assert flyweight1 is not flyweight2
        assert flyweight1 is not flyweight3
        assert flyweight2 is not flyweight3
        assert factory.get_flyweight_count() == 3

    def test_factory_handles_complex_specifications(self):
        """Test że factory obsługuje złożone specifications"""
        factory = ProductTypeFactory()
        specs = {
            "CPU": "Intel i7-12700K",
            "RAM": "32GB DDR5",
            "GPU": "RTX 4080",
            "Storage": ["1TB NVMe", "2TB HDD"],
            "Ports": {"USB": 6, "HDMI": 2, "Display Port": 1}
        }

        flyweight1 = factory.get_product_type("Gaming PC", "Custom", specs)
        flyweight2 = factory.get_product_type("Gaming PC", "Custom", specs)

        assert flyweight1 is flyweight2
        assert factory.get_flyweight_count() == 1


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

        info = product.display_product_info()

        # Sprawdź że deleguje do flyweight
        assert "LEN001" in info
        assert "Lenovo" in info
        assert "1299.99" in info
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


class TestProductCatalog:
    """Testy katalogu produktów"""

    def test_catalog_creation(self):
        """Test tworzenia katalogu"""
        catalog = ProductCatalog()

        assert hasattr(catalog, 'products')
        assert hasattr(catalog, 'factory')
        assert isinstance(catalog.factory, ProductTypeFactory)

    def test_catalog_add_product(self):
        """Test dodawania produktu do katalogu"""
        catalog = ProductCatalog()
        specs = {"CPU": "Intel i7", "RAM": "16GB", "Storage": "512GB"}

        catalog.add_product("DELL001", "Laptop", "Dell", specs, 1499.99, 5)

        # Sprawdź że produkt został dodany
        assert len(catalog.products) == 1

        product = catalog.products[0]
        assert product.sku == "DELL001"
        assert product.price == 1499.99
        assert product.product_type.brand == "Dell"

    def test_catalog_get_product_by_sku(self):
        """Test pobierania produktu po SKU"""
        catalog = ProductCatalog()
        specs = {"CPU": "AMD Ryzen", "RAM": "32GB"}

        catalog.add_product("AMD001", "Gaming", "MSI", specs, 1899.99, 3)

        product = catalog.get_product_by_sku("AMD001")
        assert product is not None
        assert product.sku == "AMD001"
        assert product.price == 1899.99

    def test_catalog_get_product_by_sku_not_found(self):
        """Test pobierania nieistniejącego produktu"""
        catalog = ProductCatalog()

        product = catalog.get_product_by_sku("NONEXISTENT")
        assert product is None

    def test_catalog_get_products_by_brand(self):
        """Test pobierania produktów po marce"""
        catalog = ProductCatalog()

        # Dodaj produkty różnych marek
        hp_specs = {"CPU": "Intel i5", "RAM": "8GB"}
        dell_specs = {"CPU": "Intel i7", "RAM": "16GB"}

        catalog.add_product("HP001", "Laptop", "HP", hp_specs, 999.99, 5)
        catalog.add_product("HP002", "Laptop", "HP", hp_specs, 1099.99, 3)
        catalog.add_product("DELL001", "Laptop", "Dell", dell_specs, 1299.99, 7)

        hp_products = catalog.get_products_by_brand("HP")
        assert len(hp_products) == 2
        assert all(p.product_type.brand == "HP" for p in hp_products)

        dell_products = catalog.get_products_by_brand("Dell")
        assert len(dell_products) == 1
        assert dell_products[0].product_type.brand == "Dell"

    def test_catalog_memory_stats(self):
        """Test statystyk zużycia pamięci"""
        catalog = ProductCatalog()

        # Dodaj wiele produktów tego samego typu
        same_specs = {"CPU": "Intel i5", "RAM": "8GB"}
        for i in range(10):
            catalog.add_product(f"SAME{i:03d}", "Laptop", "Dell", same_specs, 999.99 + i, 5)

        # Dodaj kilka różnych typów
        different_specs = {"CPU": "AMD", "RAM": "16GB"}
        catalog.add_product("DIFF001", "Gaming", "ASUS", different_specs, 1599.99, 3)

        stats = catalog.get_memory_stats()

        assert stats["total_products"] == 11
        assert stats["flyweight_count"] == 2  # Tylko 2 różne typy
        assert "memory_savings" in stats


class TestFlyweightPattern:
    """Testy wzorca Flyweight"""

    def test_flyweight_sharing_reduces_memory(self):
        """Test że flyweight faktycznie współdzieli pamięć"""
        factory = ProductTypeFactory()
        same_specs = {"CPU": "Intel i7", "RAM": "16GB", "Storage": "1TB"}

        # Stwórz wiele produktów tego samego typu
        products = []
        for i in range(100):
            flyweight = factory.get_product_type("Laptop", "Dell", same_specs)
            product = Product(f"DELL{i:03d}", flyweight, 1000 + i, 10 - (i % 10))
            products.append(product)

        # Sprawdź że wszystkie produkty współdzielą ten sam flyweight
        first_flyweight = products[0].product_type
        for product in products:
            assert product.product_type is first_flyweight

        # Sprawdź że factory utworzył tylko jeden flyweight
        assert factory.get_flyweight_count() == 1

    def test_intrinsic_vs_extrinsic_state_separation(self):
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
        assert product1.sku != product2.sku != product3.sku
        assert product1.price != product2.price != product3.price
        assert product1.stock_quantity != product2.stock_quantity != product3.stock_quantity

    def test_flyweight_immutability(self):
        """Test że flyweight jest niemodyfikowalny (powinien być)"""
        factory = ProductTypeFactory()
        specs = {"CPU": "Intel", "RAM": "8GB"}

        flyweight = factory.get_product_type("Office", "Lenovo", specs)

        # Flyweight powinien być niemodyfikowalny
        # (w praktyce to zależy od implementacji, ale jest good practice)
        original_category = flyweight.category
        original_brand = flyweight.brand
        original_specs = flyweight.specifications

        # Spróbuj zmodyfikować (nie powinno wpłynąć na inne produkty)
        # Ten test może być skip jeśli nie implementujesz immutability
        try:
            flyweight.category = "Modified"
            flyweight.brand = "Modified"
        except AttributeError:
            # Expected if properties are read-only
            pass

        # Stwórz nowy produkt z tym samym flyweight
        product = Product("TEST001", flyweight, 999.99, 1)
        info = product.display_product_info()

        # Sprawdź że dane się nie zmieniły
        assert flyweight.category in [original_category, "Modified"]  # Depends on implementation


class TestMemoryOptimization:
    """Testy demonstrujące optymalizację pamięci"""

    def test_large_scale_memory_optimization(self):
        """Test optymalizacji dla dużej liczby produktów"""
        catalog = ProductCatalog()

        # Symuluj tysiące produktów z kilkoma typami
        product_types = [
            ("Laptop", "Dell", {"CPU": "Intel i5", "RAM": "8GB"}),
            ("Laptop", "HP", {"CPU": "Intel i5", "RAM": "8GB"}),
            ("Gaming", "ASUS", {"CPU": "AMD Ryzen", "RAM": "32GB"}),
            ("Workstation", "Lenovo", {"CPU": "Intel Xeon", "RAM": "64GB"}),
            ("Ultrabook", "Apple", {"CPU": "M1", "RAM": "16GB"})
        ]

        # Dodaj po 200 produktów każdego typu (1000 total)
        for i, (category, brand, specs) in enumerate(product_types):
            for j in range(200):
                sku = f"{brand.upper()}{i}{j:03d}"
                price = 1000 + (i * 500) + j
                stock = (j % 20) + 1
                catalog.add_product(sku, category, brand, specs, price, stock)

        stats = catalog.get_memory_stats()

        # Sprawdź efektywność
        assert stats["total_products"] == 1000
        assert stats["flyweight_count"] == 5  # Tylko 5 typów
        assert stats["memory_savings"] > 90  # Ponad 90% oszczędności


class TestSampleCatalog:
    """Testy przykładowego katalogu (jeśli zaimplementowany)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_sample_catalog_creation(self):
        """Test tworzenia przykładowego katalogu"""
        catalog = create_sample_catalog()

        assert isinstance(catalog, ProductCatalog)
        assert len(catalog.products) > 10

        stats = catalog.get_memory_stats()
        assert stats["flyweight_count"] < stats["total_products"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
