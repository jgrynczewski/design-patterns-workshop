"""
GRASP Creator - Restaurant System

>>> menu = Menu()
>>> menu.add_item("Pizza", 12.99)
>>> menu.add_item("Pasta", 10.50)
>>> menu.get_items()
[('Pizza', 12.99), ('Pasta', 10.50)]

>>> table = Table(5)
>>> table.get_number()
5
>>> table.is_available()
True

>>> # Test Restaurant as Creator
>>> restaurant = Restaurant("Luigi's", 10)
>>> restaurant.get_name()
"Luigi's"
>>> restaurant.get_menu().get_items()
[]
>>> len(restaurant.get_tables())
10
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


# TODO: Zaimplementuj Restaurant
# Hint: Restaurant "ma" Menu i Tables → powinien je TWORZYĆ (Creator pattern)
# Hint: W konstruktorze przyjmij name i tables_count
# Hint: Stwórz Menu w __init__
# Hint: Stwórz listę Tables w __init__ (od 1 do tables_count)

class Restaurant:
    """
    Restauracja - CREATOR dla Menu i Tables

    GRASP Creator: Restaurant agreguje/zawiera Menu i Tables,
    więc to Restaurant powinien je tworzyć
    """

    def __init__(self, name: str, tables_count: int):
        """
        TODO: Zaimplementuj
        - Zapisz name
        - Stwórz Menu
        - Stwórz listę Tables (numery od 1 do tables_count)
        """
        pass

    def get_name(self) -> str:
        pass

    def get_menu(self) -> Menu:
        pass

    def get_tables(self) -> list[Table]:
        pass


# GRASP Creator:
# Kto tworzy obiekt A?
# → Klasa B, która:
#   - zawiera A (aggregation/composition)
#   - rejestruje A
#   - blisko współpracuje z A
#   - ma dane inicjalizujące A
