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


# Builder - ROZWIĄZANIE
# WZORZEC: Fluent interface (method chaining) + stopniowe budowanie

class CharacterBuilder:
    """
    Builder do tworzenia postaci RPG z fluent interface

    KLUCZOWE dla wzorca Builder:
    1. FLUENT INTERFACE: każda metoda zwraca self
    2. STOPNIOWE BUDOWANIE: obiekt budowany krok po kroku
    3. WALIDACJA: sprawdzenie wymaganych pól przed build()
    4. RESET: możliwość ponownego użycia buildera
    """

    def __init__(self):
        """Inicjalizuj builder poprzez reset"""
        self.reset()

    def reset(self) -> 'CharacterBuilder':
        """
        Resetuje builder do stanu początkowego

        Returns:
            self dla method chaining
        """
        self.character = Character()
        return self  # FLUENT INTERFACE

    def set_name(self, name: str) -> 'CharacterBuilder':
        """Ustawia imię postaci"""
        self.character.name = name
        return self  # FLUENT INTERFACE

    def set_class(self, character_class: str) -> 'CharacterBuilder':
        """Ustawia klasę postaci"""
        self.character.character_class = character_class
        return self  # FLUENT INTERFACE

    def set_level(self, level: int) -> 'CharacterBuilder':
        """Ustawia poziom postaci"""
        self.character.level = level
        return self  # FLUENT INTERFACE

    def set_stat(self, stat_name: str, value: int) -> 'CharacterBuilder':
        """Ustawia statystykę postaci"""
        self.character.stats[stat_name] = value
        return self  # FLUENT INTERFACE

    def add_skill(self, skill: str) -> 'CharacterBuilder':
        """Dodaje umiejętność do postaci"""
        self.character.skills.append(skill)
        return self  # FLUENT INTERFACE

    def add_equipment(self, item: str) -> 'CharacterBuilder':
        """Dodaje przedmiot do ekwipunku"""
        self.character.equipment.append(item)
        return self  # FLUENT INTERFACE

    def build(self) -> Character:
        """
        Buduje i zwraca gotową postać

        Returns:
            Zbudowana postać

        Raises:
            ValueError: Gdy brakuje wymaganych pól (name, class)
        """
        # WALIDACJA - sprawdź wymagane pola
        if not self.character.name:
            raise ValueError("Character name is required")
        if not self.character.character_class:
            raise ValueError("Character class is required")

        return self.character


# Przykład użycia
if __name__ == "__main__":
    # Tworzenie postaci krok po kroku z fluent interface
    builder = CharacterBuilder()

    # Wojownik
    warrior = (builder
               .set_name("Conan")
               .set_class("warrior")
               .set_level(15)
               .set_stat("strength", 85)
               .set_stat("constitution", 80)
               .add_skill("sword mastery")
               .add_skill("shield bash")
               .add_equipment("steel sword")
               .add_equipment("iron shield")
               .build())
    print(f"Created: {warrior}")
    print(f"Stats: {warrior.stats}")
    print(f"Skills: {warrior.skills}")

    # Reset i nowa postać
    mage = (builder
            .reset()
            .set_name("Gandalf")
            .set_class("mage")
            .set_level(50)
            .set_stat("intelligence", 95)
            .set_stat("wisdom", 90)
            .add_skill("fireball")
            .add_skill("teleport")
            .add_skill("heal")
            .add_equipment("staff of power")
            .add_equipment("robe of the archmagi")
            .build())
    print(f"\nCreated: {mage}")
    print(f"Stats: {mage.stats}")
    print(f"Skills: {mage.skills}")
