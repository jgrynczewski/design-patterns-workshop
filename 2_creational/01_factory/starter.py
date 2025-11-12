"""
Factory Method Pattern - RPG Weapons

>>> # Test Warrior creates Sword
>>> warrior = Warrior("Conan")
>>> weapon = warrior.create_weapon()
>>> weapon.get_name()
'Sword'
>>> weapon.get_damage()
50

>>> # Test Mage creates Staff
>>> mage = Mage("Gandalf")
>>> weapon = mage.create_weapon()
>>> weapon.get_name()
'Staff'
>>> weapon.get_damage()
30

>>> # Test Archer creates Bow
>>> archer = Archer("Legolas")
>>> weapon = archer.create_weapon()
>>> weapon.get_name()
'Bow'
>>> weapon.get_damage()
40

>>> # Test character uses weapon
>>> warrior = Warrior("Conan")
>>> warrior.attack()
'Conan attacks with Sword for 50 damage!'
"""

# %% About
# - Name: Factory Method - RPG Weapons
# - Difficulty: easy
# - Lines: 20
# - Minutes: 15
# - Focus: Factory Method pattern - subclasses decide what to create

# %% Description
"""
Factory Method Pattern - RPG Weapons

Wzorzec Factory Method deleguje tworzenie obiektów do podklas.
Każda klasa postaci (Warrior, Mage, Archer) tworzy swoją unikalną broń.
"""

from abc import ABC, abstractmethod


# %% STEP 1: Product Interface (Weapon)

class Weapon(ABC):
    """Interfejs produktu - broń"""

    @abstractmethod
    def get_name(self) -> str:
        """Zwraca nazwę broni"""
        pass

    @abstractmethod
    def get_damage(self) -> int:
        """Zwraca obrażenia broni"""
        pass


# %% STEP 2: Concrete Products (Sword, Staff, Bow)

# TODO: Zaimplementuj klasę Sword
# Hint: Dziedziczy po Weapon
# Hint: get_name() zwraca "Sword"
# Hint: get_damage() zwraca 50

class Sword:
    pass


# TODO: Zaimplementuj klasę Staff
# Hint: get_name() zwraca "Staff"
# Hint: get_damage() zwraca 30

class Staff:
    pass


# TODO: Zaimplementuj klasę Bow
# Hint: get_name() zwraca "Bow"
# Hint: get_damage() zwraca 40

class Bow:
    pass


# %% STEP 3: Creator (Character) - zawiera Factory Method

class Character(ABC):
    """Klasa Creator - zawiera factory method"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_weapon(self) -> Weapon:
        """
        FACTORY METHOD - abstrakcyjna metoda
        Każda podklasa nadpisze tę metodę i stworzy swoją broń
        """
        pass

    def attack(self) -> str:
        """
        Metoda używa factory method do stworzenia broni
        To jest klucz - Creator nie wie, jaka broń zostanie stworzona!
        """
        weapon = self.create_weapon()  # Wywołanie factory method
        return f"{self.name} attacks with {weapon.get_name()} for {weapon.get_damage()} damage!"


# %% STEP 4: Concrete Creators (Warrior, Mage, Archer)

# TODO: Zaimplementuj klasę Warrior
# Hint: Dziedziczy po Character
# Hint: Nadpisz create_weapon() - zwróć Sword()

class Warrior:
    pass


# TODO: Zaimplementuj klasę Mage
# Hint: Nadpisz create_weapon() - zwróć Staff()

class Mage:
    pass


# TODO: Zaimplementuj klasę Archer
# Hint: Nadpisz create_weapon() - zwróć Bow()

class Archer:
    pass


# %% Run
# - Terminal: `python -m doctest -f -v starter.py`
# - Tests: `python -m pytest test_factory.py -v`

# %% Example
# Odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     warrior = Warrior("Conan")
#     print(warrior.attack())
#
#     mage = Mage("Gandalf")
#     print(mage.attack())
