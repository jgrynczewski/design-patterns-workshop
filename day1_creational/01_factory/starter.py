# %% About
# - Name: Factory Method - RPG Heroes
# - Difficulty: easy
# - Lines: 8
# - Minutes: 15
# - Focus: Factory Method core concept

# %% Description
"""
Factory Method Pattern - RPG Heroes
Zaimplementuj wzorzec Factory Method do tworzenia bohaterów.
"""

from abc import ABC, abstractmethod


class Character(ABC):
    """Bazowa klasa dla wszystkich bohaterów"""

    def __init__(self, name: str, weapon: str, hp: int):
        self.name = name
        self.weapon = weapon
        self.hp = hp

    @abstractmethod
    def attack(self) -> str:
        """Zwraca opis ataku bohatera"""
        pass

    def get_stats(self) -> dict:
        """Zwraca statystyki bohatera"""
        return {
            "name": self.name,
            "weapon": self.weapon,
            "hp": self.hp
        }


# %% Hints
# - Use isinstance() for type checking in factory
# - Remember case-insensitive input with .lower()
# - Each class should inherit from Character

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test warrior creation
>>> warrior = create_hero("warrior")
>>> warrior.weapon
'sword'
>>> warrior.hp
100
>>> "warrior" in warrior.name.lower()
True

>>> # Test mage creation  
>>> mage = create_hero("mage")
>>> mage.weapon
'staff'
>>> mage.hp
60

>>> # Test archer creation
>>> archer = create_hero("archer") 
>>> archer.weapon
'bow'
>>> archer.hp
80

>>> # Test case insensitive
>>> warrior2 = create_hero("WARRIOR")
>>> warrior2.weapon
'sword'

>>> # Test attack method
>>> attack_msg = warrior.attack()
>>> isinstance(attack_msg, str)
True
>>> len(attack_msg) > 0
True

>>> # Test error handling
>>> create_hero("invalid")
Traceback (most recent call last):
ValueError: Unknown hero type: invalid
"""


# %% Run
# - PyCharm: right-click and `Run Doctest in ...`
# - Terminal: `python -m doctest -f -v starter.py`
# - Tests: `python -m pytest test_factory.py -v`

# %% TODO: Implement Classes

class Warrior:
    pass


class Mage:
    pass


class Archer:
    pass


# %% TODO: Implement Factory

def create_hero(hero_type: str) -> Character:
    """
    Factory Method do tworzenia bohaterów

    Args:
        hero_type: Typ bohatera ("warrior", "mage", "archer")

    Returns:
        Obiekt odpowiedniej klasy bohatera

    Raises:
        ValueError: Gdy hero_type jest nieznany
    """
    pass

# %% Example Usage
# Odkomentuj gdy zaimplementujesz
# if __name__ == "__main__":
#     warrior = create_hero("warrior")
#     print(f"{warrior.name}: {warrior.attack()}")
