"""
Factory Method Pattern - RPG Weapons - SOLUTION

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
# - Name: Factory Method - RPG Weapons - SOLUTION
# - Difficulty: easy
# - Lines: 20
# - Minutes: 15
# - Focus: Factory Method pattern - subclasses decide what to create

# %% Description
"""
Factory Method Pattern - RPG Weapons - SOLUTION

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

class Sword(Weapon):
    """Miecz - broń wojownika"""

    def get_name(self) -> str:
        return "Sword"

    def get_damage(self) -> int:
        return 50


class Staff(Weapon):
    """Różdżka - broń maga"""

    def get_name(self) -> str:
        return "Staff"

    def get_damage(self) -> int:
        return 30


class Bow(Weapon):
    """Łuk - broń łucznika"""

    def get_name(self) -> str:
        return "Bow"

    def get_damage(self) -> int:
        return 40


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

class Warrior(Character):
    """Wojownik - tworzy miecz"""

    def create_weapon(self) -> Weapon:
        """Factory method - zwraca Sword"""
        return Sword()


class Mage(Character):
    """Mag - tworzy różdżkę"""

    def create_weapon(self) -> Weapon:
        """Factory method - zwraca Staff"""
        return Staff()


class Archer(Character):
    """Łucznik - tworzy łuk"""

    def create_weapon(self) -> Weapon:
        """Factory method - zwraca Bow"""
        return Bow()


# %% Run
# - Terminal: `python -m doctest -f -v solution.py`

# %% Example
if __name__ == "__main__":
    print("=== Factory Method Pattern Demo ===\n")

    warrior = Warrior("Conan")
    print(warrior.attack())

    mage = Mage("Gandalf")
    print(mage.attack())

    archer = Archer("Legolas")
    print(archer.attack())

    print("\n=== How Factory Method Works ===")
    print("1. Character class defines abstract create_weapon() method")
    print("2. Each subclass (Warrior, Mage, Archer) overrides it")
    print("3. attack() method calls create_weapon() without knowing the concrete type")
    print("4. Subclass decides which weapon to create - that's the Factory Method pattern!")
