"""
Testy dla Composite Pattern - Product Categories Tree
"""

import pytest
from starter import ProductComponent, Product, Category, create_sample_catalog


class TestProduct:
    """Testy klasy Product (Leaf)"""

    def test_product_creation(self):
        """Test tworzenia produktu"""
        product = Product("Gaming Laptop", 1500.0)

        assert product.name == "Gaming Laptop"
        assert product.price == 1500.0

    def test_product_implements_interface(self):
        """Test że Product implementuje ProductComponent"""
        product = Product("Phone", 800.0)
        assert isinstance(product, ProductComponent)

    def test_product_get_price(self):
        """Test pobierania ceny produktu"""
        product = Product("Tablet", 400.0)
        assert product.get_price() == 400.0

    def test_product_get_count(self):
        """Test liczenia produktów - zawsze 1"""
        product = Product("Mouse", 25.0)
        assert product.get_product_count() == 1

    def test_product_display(self):
        """Test wyświetlania produktu"""
        product = Product("Keyboard", 75.0)

        # Bez wcięcia
        display = product.display(0)
        assert "Product: Keyboard" in display
        assert "$75.0" in display
        assert not display.startswith("  ")

        # Z wcięciem
        display_indented = product.display(2)
        assert display_indented.startswith("    ")  # 2 * "  "


class TestCategory:
    """Testy klasy Category (Composite)"""

    def test_category_creation(self):
        """Test tworzenia kategorii"""
        category = Category("Electronics")

        assert category.name == "Electronics"
        assert len(category.get_children()) == 0

    def test_category_implements_interface(self):
        """Test że Category implementuje ProductComponent"""
        category = Category("Books")
        assert isinstance(category, ProductComponent)

    def test_category_add_remove_items(self):
        """Test dodawania i usuwania elementów"""
        category = Category("Gadgets")
        product1 = Product("Phone", 800.0)
        product2 = Product("Tablet", 400.0)

        # Dodawanie
        category.add_item(product1)
        category.add_item(product2)
        assert len(category.get_children()) == 2

        # Usuwanie
        category.remove_item(product1)
        assert len(category.get_children()) == 1
        assert product2 in category.get_children()
        assert product1 not in category.get_children()

    def test_category_remove_nonexistent_item(self):
        """Test usuwania nieistniejącego elementu"""
        category = Category("Test")
        product = Product("Test Product", 100.0)

        # Nie powinno rzucać wyjątku
        category.remove_item(product)
        assert len(category.get_children()) == 0

    def test_empty_category_operations(self):
        """Test operacji na pustej kategorii"""
        category = Category("Empty")

        assert category.get_price() == 0.0
        assert category.get_product_count() == 0


class TestCompositeOperations:
    """Testy operacji composite na strukturze drzewa"""

    def test_category_with_products_price(self):
        """Test sumowania cen produktów w kategorii"""
        category = Category("Electronics")
        category.add_item(Product("Phone", 800.0))
        category.add_item(Product("Tablet", 400.0))
        category.add_item(Product("Earphones", 100.0))

        assert category.get_price() == 1300.0

    def test_category_with_products_count(self):
        """Test liczenia produktów w kategorii"""
        category = Category("Accessories")
        category.add_item(Product("Mouse", 25.0))
        category.add_item(Product("Keyboard", 75.0))
        category.add_item(Product("Monitor", 200.0))

        assert category.get_product_count() == 3

    def test_nested_categories_price(self):
        """Test sumowania cen w zagnieżdżonych kategoriach"""
        # Główna kategoria
        electronics = Category("Electronics")

        # Podkategoria laptops
        laptops = Category("Laptops")
        laptops.add_item(Product("Gaming Laptop", 1500.0))
        laptops.add_item(Product("Business Laptop", 1000.0))

        # Podkategoria phones
        phones = Category("Phones")
        phones.add_item(Product("iPhone", 800.0))
        phones.add_item(Product("Android", 400.0))

        # Dodaj podkategorie do głównej
        electronics.add_item(laptops)
        electronics.add_item(phones)

        # Dodaj bezpośredni produkt
        electronics.add_item(Product("Cable", 25.0))

        # Test rekurencyjnego sumowania
        assert electronics.get_price() == 3725.0  # 2500 + 1200 + 25

    def test_nested_categories_count(self):
        """Test liczenia produktów w zagnieżdżonych kategoriach"""
        electronics = Category("Electronics")

        laptops = Category("Laptops")
        laptops.add_item(Product("Gaming Laptop", 1500.0))
        laptops.add_item(Product("Business Laptop", 1000.0))

        phones = Category("Phones")
        phones.add_item(Product("iPhone", 800.0))
        phones.add_item(Product("Android", 400.0))
        phones.add_item(Product("Feature Phone", 50.0))

        electronics.add_item(laptops)
        electronics.add_item(phones)
        electronics.add_item(Product("Cable", 25.0))

        # Test rekurencyjnego liczenia
        assert electronics.get_product_count() == 6  # 2 + 3 + 1

    def test_three_level_nesting(self):
        """Test trzech poziomów zagnieżdżenia"""
        # Poziom 1: Electronics
        electronics = Category("Electronics")

        # Poziom 2: Computers
        computers = Category("Computers")

        # Poziom 3: Gaming
        gaming = Category("Gaming")
        gaming.add_item(Product("Gaming PC", 2000.0))
        gaming.add_item(Product("Gaming Monitor", 500.0))

        computers.add_item(gaming)
        computers.add_item(Product("Office PC", 800.0))

        electronics.add_item(computers)
        electronics.add_item(Product("Phone", 400.0))

        assert electronics.get_price() == 3700.0
        assert electronics.get_product_count() == 4


class TestCompositeDisplay:
    """Testy wyświetlania struktury drzewa"""

    def test_category_display_with_products(self):
        """Test wyświetlania kategorii z produktami"""
        category = Category("Gadgets")
        category.add_item(Product("Phone", 800.0))
        category.add_item(Product("Tablet", 400.0))

        display = category.display(0)

        assert "Category: Gadgets" in display
        assert "Product: Phone" in display
        assert "Product: Tablet" in display
        assert "$800.0" in display
        assert "$400.0" in display

    def test_nested_display_indentation(self):
        """Test wcięć w zagnieżdżonej strukturze"""
        electronics = Category("Electronics")
        laptops = Category("Laptops")
        laptops.add_item(Product("Gaming Laptop", 1500.0))

        electronics.add_item(laptops)

        display = electronics.display(0)
        lines = display.split('\n')

        # Sprawdź wcięcia
        assert lines[0] == "Category: Electronics"  # Level 0
        assert lines[1] == "  Category: Laptops"  # Level 1
        assert lines[2] == "    Product: Gaming Laptop ($1500.0)"  # Level 2


class TestUniformInterface:
    """Testy jednolitego interfejsu dla Product i Category"""

    def test_uniform_interface_operations(self):
        """Test że Product i Category mają ten sam interfejs"""
        items = [
            Product("Laptop", 1000.0),
            Category("Empty Category")
        ]

        for item in items:
            # Wszystkie powinny mieć te same metody
            assert hasattr(item, 'get_price')
            assert hasattr(item, 'get_product_count')
            assert hasattr(item, 'display')

            # Wszystkie metody powinny być callable
            assert callable(item.get_price)
            assert callable(item.get_product_count)
            assert callable(item.display)

    def test_polymorphic_behavior(self):
        """Test polimorficznego zachowania"""

        def process_component(component: ProductComponent) -> dict:
            return {
                'price': component.get_price(),
                'count': component.get_product_count(),
                'display': component.display()
            }

        # Test z produktem
        product = Product("Test Product", 100.0)
        result1 = process_component(product)
        assert result1['price'] == 100.0
        assert result1['count'] == 1

        # Test z kategorią
        category = Category("Test Category")
        category.add_item(Product("Item", 50.0))
        result2 = process_component(category)
        assert result2['price'] == 50.0
        assert result2['count'] == 1


class TestSampleCatalog:
    """Testy przykładowego katalogu (jeśli zaimplementowany)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_sample_catalog_creation(self):
        """Test tworzenia przykładowego katalogu"""
        catalog = create_sample_catalog()

        assert isinstance(catalog, Category)
        assert catalog.name == "Electronics"
        assert catalog.get_product_count() > 0
        assert catalog.get_price() > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
