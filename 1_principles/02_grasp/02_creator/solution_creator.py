"""
GRASP Creator - Restaurant System - SOLUTION

>>> restaurant = Restaurant("Luigi's", 5)
>>> restaurant.get_name()
"Luigi's"
>>> len(restaurant.get_tables())
5
>>> restaurant.get_tables()[0].get_number()
1
"""


class Menu:
    """Menu restauracji"""

    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float):
        self.items.append((name, price))

    def get_items(self) -> list:
        return self.items


class Table:
    """Stolik w restauracji"""

    def __init__(self, number: int):
        self.number = number
        self.available = True

    def get_number(self) -> int:
        return self.number

    def is_available(self) -> bool:
        return self.available


class Restaurant:
    """Restauracja - CREATOR dla Menu i Tables"""

    def __init__(self, name: str, tables_count: int):
        self.name = name
        self.menu = Menu()  # Restaurant tworzy Menu
        self.tables = [Table(i) for i in range(1, tables_count + 1)]  # Restaurant tworzy Tables

    def get_name(self) -> str:
        return self.name

    def get_menu(self) -> Menu:
        return self.menu

    def get_tables(self) -> list[Table]:
        return self.tables


if __name__ == "__main__":
    print("=== GRASP Creator ===\n")

    restaurant = Restaurant("Luigi's Italian", 5)
    print(f"Restaurant: {restaurant.get_name()}")
    print(f"Tables: {len(restaurant.get_tables())}")

    menu = restaurant.get_menu()
    menu.add_item("Pizza Margherita", 12.99)
    menu.add_item("Pasta Carbonara", 10.50)
    print(f"Menu items: {len(menu.get_items())}")

    print("\nCreator: Restaurant tworzy Menu i Tables (zawiera je)")
