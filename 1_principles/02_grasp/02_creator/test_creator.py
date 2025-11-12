"""
Testy dla GRASP Creator - Restaurant
"""

import pytest
from starter import Menu, Table, Restaurant


class TestCreator:
    """Testy GRASP Creator"""

    def test_menu_creation(self):
        menu = Menu()
        menu.add_item("Pizza", 12.99)
        assert len(menu.get_items()) == 1
        assert menu.get_items()[0] == ("Pizza", 12.99)

    def test_table_creation(self):
        table = Table(5)
        assert table.get_number() == 5
        assert table.is_available() is True

    def test_restaurant_creates_menu(self):
        """Creator: Restaurant tworzy Menu"""
        restaurant = Restaurant("Test", 5)
        menu = restaurant.get_menu()

        assert menu is not None
        assert isinstance(menu, Menu)

    def test_restaurant_creates_tables(self):
        """Creator: Restaurant tworzy Tables"""
        restaurant = Restaurant("Test", 3)
        tables = restaurant.get_tables()

        assert len(tables) == 3
        assert all(isinstance(t, Table) for t in tables)

    def test_restaurant_table_numbers(self):
        """Tables powinny mieć numery od 1"""
        restaurant = Restaurant("Test", 5)
        tables = restaurant.get_tables()

        numbers = [t.get_number() for t in tables]
        assert numbers == [1, 2, 3, 4, 5]

    def test_restaurant_name(self):
        restaurant = Restaurant("Luigi's", 10)
        assert restaurant.get_name() == "Luigi's"

    def test_multiple_restaurants_independent(self):
        """Każda restauracja ma własne Menu i Tables"""
        r1 = Restaurant("Restaurant 1", 3)
        r2 = Restaurant("Restaurant 2", 5)

        assert r1.get_menu() is not r2.get_menu()
        assert len(r1.get_tables()) == 3
        assert len(r2.get_tables()) == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
