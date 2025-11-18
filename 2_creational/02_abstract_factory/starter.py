"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test Warrior factory
>>> warrior_factory = WarriorEquipmentFactory()
>>> warrior_weapon = warrior_factory.create_weapon()
>>> warrior_armor = warrior_factory.create_armor()
>>> warrior_weapon.damage() >= 80
True
>>> warrior_armor.defense() >= 50
True
>>> "sword" in warrior_weapon.get_name().lower()
True

>>> # Test Mage factory
>>> mage_factory = MageEquipmentFactory()
>>> mage_weapon = mage_factory.create_weapon()
>>> mage_armor = mage_factory.create_armor()
>>> mage_weapon.damage() >= 40
True
>>> mage_armor.defense() >= 15
True
>>> "staff" in mage_weapon.get_name().lower()
True

>>> # Test Archer factory
>>> archer_factory = ArcherEquipmentFactory()
>>> archer_weapon = archer_factory.create_weapon()
>>> archer_armor = archer_factory.create_armor()
>>> archer_weapon.damage() >= 60
True
>>> archer_armor.defense() >= 25
True
>>> "bow" in archer_weapon.get_name().lower()
True

>>> # Test każda fabryka implementuje interfejs
>>> isinstance(warrior_factory, EquipmentFactory)
True
>>> isinstance(mage_factory, EquipmentFactory)
True
>>> isinstance(archer_factory, EquipmentFactory)
True
"""

from abc import ABC, abstractmethod


# Product Interfaces - GOTOWE

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


# Concrete Products - GOTOWE (takie same jak w problem.py)
# Te klasy są już zaimplementowane - skupiamy się na fabrykach!

class Sword(Weapon):
    """Miecz - broń wojownika"""

    def damage(self) -> int:
        return 100

    def get_name(self) -> str:
        return "Heavy Sword"


class Staff(Weapon):
    """Laska - broń maga"""

    def damage(self) -> int:
        return 50

    def get_name(self) -> str:
        return "Magic Staff"


class Bow(Weapon):
    """Łuk - broń łucznika"""

    def damage(self) -> int:
        return 70

    def get_name(self) -> str:
        return "Long Bow"


class HeavyArmor(Armor):
    """Ciężka zbroja - pancerz wojownika"""

    def defense(self) -> int:
        return 60

    def get_name(self) -> str:
        return "Heavy Plate Armor"


class LightRobe(Armor):
    """Lekka szata - pancerz maga"""

    def defense(self) -> int:
        return 20

    def get_name(self) -> str:
        return "Light Robe"


class LeatherArmor(Armor):
    """Skórzana zbroja - pancerz łucznika"""

    def defense(self) -> int:
        return 35

    def get_name(self) -> str:
        return "Leather Armor"


# TODO: Zaimplementuj Abstract Factory Interface
# Stwórz klasę EquipmentFactory(ABC) z abstrakcyjnymi metodami:
# - create_weapon() -> Weapon
# - create_armor() -> Armor

class EquipmentFactory:
    pass


# TODO: Zaimplementuj Concrete Factories
# Każda fabryka dziedziczy po EquipmentFactory
# Implementuje create_weapon() i create_armor()
# Gwarantuje spójność - zawsze zwraca pasujące produkty z jednej rodziny

class WarriorEquipmentFactory:
    pass


class MageEquipmentFactory:
    pass


class ArcherEquipmentFactory:
    pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     print("=== WARRIOR EQUIPMENT ===")
#     warrior_factory = WarriorEquipmentFactory()
#     weapon = warrior_factory.create_weapon()
#     armor = warrior_factory.create_armor()
#     print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
#     print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")
#
#     print("\n=== MAGE EQUIPMENT ===")
#     mage_factory = MageEquipmentFactory()
#     weapon = mage_factory.create_weapon()
#     armor = mage_factory.create_armor()
#     print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
#     print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")
#
#     print("\n=== ARCHER EQUIPMENT ===")
#     archer_factory = ArcherEquipmentFactory()
#     weapon = archer_factory.create_weapon()
#     armor = archer_factory.create_armor()
#     print(f"Weapon: {weapon.get_name()} (DMG: {weapon.damage()})")
#     print(f"Armor: {armor.get_name()} (DEF: {armor.defense()})")
#
#     print("\n✅ Gwarantowana spójność!")
#     print("Niemożliwe stworzenie Sword + LightRobe przez fabrykę")
