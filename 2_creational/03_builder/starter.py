"""
Builder Pattern - RPG Character Creator

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
"""

from typing import List, Dict, Optional


# Character Class - GOTOWE
# Product - klasa reprezentująca złożony obiekt do zbudowania

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


# Builder - DO IMPLEMENTACJI
# WZORZEC: Fluent interface (method chaining) + stopniowe budowanie

# TODO: Zaimplementuj CharacterBuilder
# KLUCZOWE dla wzorca Builder:
# 1. FLUENT INTERFACE: każda metoda zwraca self (dla method chaining)
# 2. STOPNIOWE BUDOWANIE: budowanie obiektu krok po kroku
# 3. WALIDACJA: sprawdź wymagane pola w build() przed zwróceniem
# 4. RESET: możliwość resetowania buildera do ponownego użycia
#
# Metody do zaimplementowania:
# - __init__() - inicjalizuj poprzez wywołanie reset()
# - reset() - stwórz nową instancję Character (self.character = Character()), zwróć self
# - set_name(name) - ustaw self.character.name, zwróć self
# - set_class(character_class) - ustaw self.character.character_class, zwróć self
# - set_level(level) - ustaw self.character.level, zwróć self
# - set_stat(stat_name, value) - ustaw self.character.stats[stat_name], zwróć self
# - add_skill(skill) - dodaj do self.character.skills, zwróć self
# - add_equipment(item) - dodaj do self.character.equipment, zwróć self
# - build() - sprawdź czy name i class są ustawione, jeśli nie - raise ValueError, zwróć self.character

class CharacterBuilder:
    pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     # Tworzenie postaci krok po kroku z fluent interface
#     builder = CharacterBuilder()
#
#     # Wojownik
#     warrior = (builder
#                .set_name("Conan")
#                .set_class("warrior")
#                .set_level(15)
#                .set_stat("strength", 85)
#                .set_stat("constitution", 80)
#                .add_skill("sword mastery")
#                .add_skill("shield bash")
#                .add_equipment("steel sword")
#                .add_equipment("iron shield")
#                .build())
#     print(f"Created: {warrior}")
#     print(f"Stats: {warrior.stats}")
#     print(f"Skills: {warrior.skills}")
#
#     # Reset i nowa postać
#     mage = (builder
#             .reset()
#             .set_name("Gandalf")
#             .set_class("mage")
#             .set_level(50)
#             .set_stat("intelligence", 95)
#             .set_stat("wisdom", 90)
#             .add_skill("fireball")
#             .add_skill("teleport")
#             .add_skill("heal")
#             .add_equipment("staff of power")
#             .add_equipment("robe of the archmagi")
#             .build())
#     print(f"\nCreated: {mage}")
#     print(f"Stats: {mage.stats}")
#     print(f"Skills: {mage.skills}")
