# %% About
# - Name: Prototype - Object Cloning RPG
# - Difficulty: easy
# - Lines: 10
# - Minutes: 15
# - Focus: Prototype pattern + cloning

# %% Description
"""
Prototype Pattern - Object Cloning
Zaimplementuj wzorzec Prototype do efektywnego klonowania obiektów gry.
"""

import copy
from typing import List, Dict, Any
from abc import ABC, abstractmethod

# %% Hints
# - Use copy.copy() for shallow copy (basic attributes)
# - Use copy.deepcopy() for deep copy (lists, dicts)
# - clone() method should return new instance with same data
# - PrototypeManager acts as registry of templates

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test basic character cloning
>>> orc = Enemy("Orc", 100, 15, ["club", "leather_armor"])
>>> orc_clone = orc.clone()
>>> orc_clone.name
'Orc'
>>> orc_clone.hp
100
>>> orc is orc_clone
False

>>> # Test deep copy of equipment
>>> orc_clone.equipment.append("shield")
>>> len(orc.equipment)
2
>>> len(orc_clone.equipment)
3

>>> # Test item cloning
>>> sword = Item("Iron Sword", "weapon", {"damage": 25, "durability": 100})
>>> sword_clone = sword.clone()
>>> sword_clone.properties["damage"] = 50
>>> sword.properties["damage"]
25

>>> # Test prototype manager
>>> manager = PrototypeManager()
>>> manager.register("basic_orc", orc)
>>> manager.register("iron_sword", sword)
>>> new_orc = manager.create("basic_orc")
>>> new_sword = manager.create("iron_sword")
>>> new_orc.name
'Orc'
>>> new_sword.name
'Iron Sword'

>>> # Test army creation
>>> orc_army = manager.create_multiple("basic_orc", 5)
>>> len(orc_army)
5
>>> all(enemy.name == "Orc" for enemy in orc_army)
True
"""


# %% Run
# - PyCharm: right-click and `Run Doctest in ...`
# - Terminal: `python -m doctest -f -v starter.py`
# - Tests: `python -m pytest test_prototype.py -v`

# %% TODO: Implement Prototype Interface

class Prototype(ABC):
    """Abstract base class dla wszystkich prototypów"""

    @abstractmethod
    def clone(self) -> 'Prototype':
        """
        Tworzy kopię obiektu

        Returns:
            Nowa instancja z tymi samymi danymi
        """
        pass


# %% TODO: Implement Enemy Prototype

class Enemy(Prototype):
    """Klasa przeciwnika z możliwością klonowania"""

    def __init__(self, name: str, hp: int, damage: int, equipment: List[str]):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.equipment = equipment  # Lista - potrzebuje deep copy

    def clone(self) -> 'Enemy':
        """
        Klonuje przeciwnika z deep copy equipment

        Returns:
            Nowa instancja Enemy
        """
        # TODO: Zaimplementuj klonowanie
        # Hint: użyj copy.deepcopy dla equipment (lista)
        pass

    def __str__(self) -> str:
        return f"{self.name} (HP: {self.hp}, DMG: {self.damage})"


# %% TODO: Implement Item Prototype

class Item(Prototype):
    """Klasa przedmiotu z możliwością klonowania"""

    def __init__(self, name: str, item_type: str, properties: Dict[str, Any]):
        self.name = name
        self.item_type = item_type
        self.properties = properties  # Dict - potrzebuje deep copy

    def clone(self) -> 'Item':
        """
        Klonuje przedmiot z deep copy properties

        Returns:
            Nowa instancja Item
        """
        # TODO: Zaimplementuj klonowanie
        # Hint: użyj copy.deepcopy dla properties (dict)
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.item_type})"


# %% TODO: Implement Spell Prototype

class Spell(Prototype):
    """Klasa czaru z możliwością klonowania"""

    def __init__(self, name: str, mana_cost: int, effects: List[str]):
        self.name = name
        self.mana_cost = mana_cost
        self.effects = effects  # Lista - potrzebuje deep copy

    def clone(self) -> 'Spell':
        """
        Klonuje czar z deep copy effects

        Returns:
            Nowa instancja Spell
        """
        # TODO: Zaimplementuj klonowanie
        pass

    def __str__(self) -> str:
        return f"{self.name} (Mana: {self.mana_cost})"


# %% TODO: Implement Prototype Manager

class PrototypeManager:
    """Manager do zarządzania i tworzenia prototypów"""

    def __init__(self):
        # TODO: Zainicjalizuj storage dla prototypów
        pass

    def register(self, name: str, prototype: Prototype) -> None:
        """
        Rejestruje prototyp pod daną nazwą

        Args:
            name: Nazwa szablonu
            prototype: Obiekt prototypu do zarejestrowania
        """
        # TODO: Zaimplementuj rejestrację
        pass

    def create(self, name: str) -> Prototype:
        """
        Tworzy nową instancję na podstawie zarejestrowanego prototypu

        Args:
            name: Nazwa zarejestrowanego prototypu

        Returns:
            Sklonowana instancja prototypu

        Raises:
            KeyError: Gdy prototyp nie został znaleziony
        """
        # TODO: Zaimplementuj tworzenie przez klonowanie
        pass

    def create_multiple(self, name: str, count: int) -> List[Prototype]:
        """
        Tworzy wiele instancji tego samego prototypu

        Args:
            name: Nazwa prototypu
            count: Liczba instancji do utworzenia

        Returns:
            Lista sklonowanych instancji
        """
        # TODO: Zaimplementuj tworzenie wielu kopii
        pass

    def list_prototypes(self) -> List[str]:
        """
        Zwraca listę zarejestrowanych nazw prototypów

        Returns:
            Lista nazw dostępnych prototypów
        """
        # TODO: Zaimplementuj listowanie
        pass

# %% Example Usage
# Odkomentuj gdy zaimplementujesz
# if __name__ == "__main__":
#     # Stwórz prototypy
#     base_orc = Enemy("Orc Warrior", 120, 20, ["rusty_sword", "leather_armor"])
#     base_spell = Spell("Fireball", 15, ["fire_damage", "area_effect"])
#
#     # Zarejestruj w managerze
#     manager = PrototypeManager()
#     manager.register("orc_template", base_orc)
#     manager.register("fireball_template", base_spell)
#
#     # Sklonuj armię orków
#     print("Creating orc army...")
#     orc_army = manager.create_multiple("orc_template", 5)
#     for i, orc in enumerate(orc_army):
#         print(f"Orc {i+1}: {orc}")
#
#     # Test deep copy
#     orc1 = manager.create("orc_template")
#     orc2 = manager.create("orc_template")
#     orc1.equipment.append("magic_ring")
#
#     print(f"\nOrc1 equipment: {orc1.equipment}")
#     print(f"Orc2 equipment: {orc2.equipment}")
#     print("Equipment lists are independent!")
