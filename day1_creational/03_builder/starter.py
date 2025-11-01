# %% About
# - Name: Builder - Character Creator RPG
# - Difficulty: medium
# - Lines: 15
# - Minutes: 15
# - Focus: Builder pattern + fluent interface

# %% Description
"""
Builder Pattern - RPG Character Creator
Zaimplementuj wzorzec Builder do tworzenia złożonych postaci RPG krok po kroku.
"""

from typing import List, Dict, Optional

# %% Hints
# - Return 'self' from each builder method for chaining
# - Validate required fields (name, class) in build() method
# - Use reset() to clear builder state for reuse
# - Director contains "recipes" for common character builds
# - Initialize collections as empty lists/dicts

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test fluent interface (method chaining)
>>> builder = CharacterBuilder()
>>> character = (builder
...     .set_name("Aragorn")
...     .set_class("ranger")
...     .set_level(25)
...     .set_stat("strength", 80)
...     .add_skill("archery")
...     .add_equipment("sword")
...     .build())
>>> character.name
'Aragorn'
>>> character.character_class
'ranger'
>>> character.level
25

>>> # Test builder returns self for chaining
>>> result = builder.reset().set_name("Test")
>>> result is builder
True

>>> # Test validation - missing name
>>> CharacterBuilder().set_class("warrior").build()
Traceback (most recent call last):
ValueError: Character name is required

>>> # Test validation - missing class
>>> CharacterBuilder().set_name("Test").build()
Traceback (most recent call last):
ValueError: Character class is required

>>> # Test director patterns
>>> director = CharacterDirector()
>>> warrior = director.create_beginner_warrior("Conan")
>>> warrior.name
'Conan'
>>> warrior.character_class
'warrior'
>>> warrior.stats['strength'] >= 70
True

>>> # Test custom character function
>>> custom = create_custom_character()
>>> custom.name is not None
True
>>> custom.character_class is not None
True
>>> len(custom.skills) > 0
True
"""


# %% Run
# - PyCharm: right-click and `Run Doctest in ...`
# - Terminal: `python -m doctest -f -v starter.py`
# - Tests: `python -m pytest test_builder.py -v`

# %% TODO: Implement Product Class

class Character:
    """Klasa reprezentująca postać RPG"""

    def __init__(self):
        self.name: Optional[str] = None
        self.character_class: Optional[str] = None
        self.level: int = 1
        self.stats: Dict[str, int] = {}
        self.skills: List[str] = []
        self.equipment: List[str] = []

    def __str__(self) -> str:
        return f"{self.name} the {self.character_class} (Level {self.level})"

    def get_info(self) -> Dict:
        """Zwraca pełne informacje o postaci"""
        return {
            "name": self.name,
            "class": self.character_class,
            "level": self.level,
            "stats": self.stats.copy(),
            "skills": self.skills.copy(),
            "equipment": self.equipment.copy()
        }


# %% TODO: Implement Builder

class CharacterBuilder:
    """Builder do tworzenia postaci RPG z fluent interface"""

    def __init__(self):
        self.reset()

    def reset(self) -> 'CharacterBuilder':
        """Resetuje builder do stanu początkowego"""
        # TODO: Zaimplementuj reset - stwórz nową instancję Character
        pass

    def set_name(self, name: str) -> 'CharacterBuilder':
        """Ustawia imię postaci"""
        # TODO: Zaimplementuj i zwróć self dla chaining
        pass

    def set_class(self, character_class: str) -> 'CharacterBuilder':
        """Ustawia klasę postaci"""
        # TODO: Zaimplementuj i zwróć self dla chaining
        pass

    def set_level(self, level: int) -> 'CharacterBuilder':
        """Ustawia poziom postaci"""
        # TODO: Zaimplementuj i zwróć self dla chaining
        pass

    def set_stat(self, stat_name: str, value: int) -> 'CharacterBuilder':
        """Ustawia statystykę postaci"""
        # TODO: Zaimplementuj i zwróć self dla chaining
        pass

    def add_skill(self, skill: str) -> 'CharacterBuilder':
        """Dodaje umiejętność do postaci"""
        # TODO: Zaimplementuj i zwróć self dla chaining
        pass

    def add_equipment(self, item: str) -> 'CharacterBuilder':
        """Dodaje przedmiot do ekwipunku"""
        # TODO: Zaimplementuj i zwróć self dla chaining
        pass

    def build(self) -> Character:
        """
        Buduje i zwraca gotową postać

        Raises:
            ValueError: Gdy brakuje wymaganych pól (name, class)
        """
        # TODO: Zaimplementuj walidację i zwrócenie postaci
        pass


# %% TODO: Implement Director

class CharacterDirector:
    """Director zawierający predefiniowane buildy postaci"""

    def __init__(self):
        self.builder = CharacterBuilder()

    def create_beginner_warrior(self, name: str) -> Character:
        """Tworzy początkującego wojownika"""
        # TODO: Zaimplementuj preset dla wojownika
        # Wojownik: high strength, medium constitution, basic equipment
        pass

    def create_elite_mage(self, name: str) -> Character:
        """Tworzy elitarnego maga"""
        # TODO: Zaimplementuj preset dla maga
        # Mag: high intelligence, medium wisdom, magic equipment
        pass

    def create_sneaky_archer(self, name: str) -> Character:
        """Tworzy podstępnego łucznika"""
        # TODO: Zaimplementuj preset dla łucznika
        # Łucznik: high dexterity, medium perception, ranged equipment
        pass


# %% TODO: Implement Helper Function

def create_custom_character() -> Character:
    """
    Przykład użycia builder pattern z fluent interface

    Returns:
        Postać stworzona za pomocą method chaining
    """
    # TODO: Zaimplementuj przykład fluent interface
    # return (CharacterBuilder()
    #         .set_name("Gandalf")
    #         .set_class("mage")
    #         .set_level(50)
    #         .set_stat("intelligence", 95)
    #         .add_skill("fireball")
    #         .add_equipment("staff of power")
    #         .build())
    pass

# %% Example Usage
# Odkomentuj gdy zaimplementujesz
# if __name__ == "__main__":
#     # Builder usage - step by step
#     builder = CharacterBuilder()
#     character = (builder
#                 .set_name("Legolas")
#                 .set_class("archer")
#                 .set_level(30)
#                 .set_stat("dexterity", 95)
#                 .set_stat("perception", 90)
#                 .add_skill("archery")
#                 .add_skill("stealth")
#                 .add_equipment("elven bow")
#                 .add_equipment("quiver")
#                 .build())
#
#     print(f"Built character: {character}")
#     print(f"Character info: {character.get_info()}")
#
#     # Director usage - presets
#     director = CharacterDirector()
#     warrior = director.create_beginner_warrior("Conan")
#     mage = director.create_elite_mage("Merlin")
#
#     print(f"\nPreset warrior: {warrior}")
#     print(f"Preset mage: {mage}")
#
#     # Custom character
#     custom = create_custom_character()
#     print(f"Custom character: {custom}")
