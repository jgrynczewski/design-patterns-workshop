"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test factory creation
>>> warrior_factory = get_equipment_factory("warrior")
>>> mage_factory = get_equipment_factory("mage")
>>> archer_factory = get_equipment_factory("archer")

>>> # Test warrior equipment (high damage + defense)
>>> warrior_weapon = warrior_factory.create_weapon()
>>> warrior_armor = warrior_factory.create_armor()
>>> warrior_weapon.damage() >= 80
True
>>> warrior_armor.defense() >= 50
True
>>> "sword" in warrior_weapon.get_name().lower()
True

>>> # Test mage equipment (medium damage + low defense)
>>> mage_weapon = mage_factory.create_weapon()
>>> mage_armor = mage_factory.create_armor()
>>> mage_weapon.damage() >= 40
True
>>> mage_armor.defense() >= 15
True
>>> "staff" in mage_weapon.get_name().lower()
True

>>> # Test archer equipment (medium-high damage + medium defense)
>>> archer_weapon = archer_factory.create_weapon()
>>> archer_armor = archer_factory.create_armor()
>>> archer_weapon.damage() >= 60
True
>>> archer_armor.defense() >= 25
True
>>> "bow" in archer_weapon.get_name().lower()
True

>>> # Test case insensitive
>>> factory1 = get_equipment_factory("WARRIOR")
>>> factory2 = get_equipment_factory("warrior")
>>> type(factory1).__name__ == type(factory2).__name__
True

>>> # Test error handling
>>> get_equipment_factory("invalid")
Traceback (most recent call last):
ValueError: Unknown character class: invalid
"""

# %% About
# - Name: Abstract Factory - Equipment Systems RPG
# - Difficulty: medium
# - Lines: 12
# - Minutes: 15
# - Focus: Abstract Factory pattern + product families

# %% Description
"""
Abstract Factory Pattern - RPG Equipment
Zaimplementuj wzorzec Abstract Factory do tworzenia spójnych zestawów ekwipunku.
"""

from abc import ABC, abstractmethod

# %% Hints
# - Each concrete factory creates family of related products
# - Use inheritance: Sword(Weapon), HeavyArmor(Armor)
# - Factory method: get_equipment_factory(character_class)
# - Case-insensitive input with .lower()
# - Consistent damage/defense values per character class

# %% Doctests


# %% Run
# - PyCharm: right-click and `Run Doctest in ...`
# - Terminal: `python -m doctest -f -v starter.py`
# - Tests: `python -m pytest test_abstract_factory.py -v`

# %% TODO: Implement Product Interfaces

class Weapon(ABC):
    """Bazowy interfejs dla broni"""

    @abstractmethod
    def damage(self) -> int:
        """Zwraca obrażenia broni"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Zwraca nazwę broni"""
        pass


class Armor(ABC):
    """Bazowy interfejs dla pancerza"""

    @abstractmethod
    def defense(self) -> int:
        """Zwraca obronę pancerza"""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Zwraca nazwę pancerza"""
        pass


# %% TODO: Implement Abstract Factory

class EquipmentFactory(ABC):
    """Abstract Factory dla ekwipunku"""

    @abstractmethod
    def create_weapon(self) -> Weapon:
        """Tworzy broń odpowiednią dla klasy"""
        pass

    @abstractmethod
    def create_armor(self) -> Armor:
        """Tworzy pancerz odpowiedni dla klasy"""
        pass


# %% TODO: Implement Concrete Products - Weapons

class Sword:
    pass


class Staff:
    pass


class Bow:
    pass


# %% TODO: Implement Concrete Products - Armor

class HeavyArmor:
    pass


class LightRobe:
    pass


class LeatherArmor:
    pass


# %% TODO: Implement Concrete Factories

class WarriorEquipmentFactory:
    pass


class MageEquipmentFactory:
    pass


class ArcherEquipmentFactory:
    pass


# %% TODO: Implement Factory Method

def get_equipment_factory(character_class: str) -> EquipmentFactory:
    """
    Factory Method zwracający odpowiednią fabrykę dla klasy postaci

    Args:
        character_class: "warrior", "mage", lub "archer"

    Returns:
        Instancja odpowiedniej fabryki

    Raises:
        ValueError: Gdy character_class jest nieznany
    """
    pass

# %% Example Usage
# Odkomentuj gdy zaimplementujesz
# if __name__ == "__main__":
#     # Test different equipment sets
#     classes = ["warrior", "mage", "archer"]
#
#     for char_class in classes:
#         print(f"\n=== {char_class.upper()} EQUIPMENT ===")
#         factory = get_equipment_factory(char_class)
#
#         weapon = factory.create_weapon()
#         armor = factory.create_armor()
#
#         print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
#         print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")
#
#         # Test equipment synergy
#         total_power = weapon.damage() + armor.defense()
#         print(f"Total Power: {total_power}")
