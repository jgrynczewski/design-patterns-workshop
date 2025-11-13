"""
❌ PROBLEM: Tworzenie obiektów z funkcją fabryczną

Rozwiązanie bez wzorca (funkcja fabryczna):
- Centralna funkcja create_weapon() z if/elif dla każdego typu
- Dodanie nowej postaci wymaga MODYFIKACJI funkcji
- Brak polimorfizmu na poziomie postaci
"""

from abc import ABC, abstractmethod


# Weapons (Product)
class Weapon(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_damage(self) -> int:
        pass


class Sword(Weapon):
    def get_name(self) -> str:
        return "Sword"

    def get_damage(self) -> int:
        return 50


class Staff(Weapon):
    def get_name(self) -> str:
        return "Staff"

    def get_damage(self) -> int:
        return 30


class Bow(Weapon):
    def get_name(self) -> str:
        return "Bow"

    def get_damage(self) -> int:
        return 40


# ❌ PROBLEM: Funkcja fabryczna z if/elif
def create_weapon(character_type: str) -> Weapon:
    """Funkcja fabryczna - wszystkie decyzje w jednym miejscu"""
    if character_type == "warrior":
        return Sword()
    elif character_type == "mage":
        return Staff()
    elif character_type == "archer":
        return Bow()
    # ❌ Dodanie Paladin wymaga edycji tej funkcji
    else:
        raise ValueError(f"Unknown character type: {character_type}")


class Character:
    """Postać używa funkcji fabrycznej create_weapon()"""

    def __init__(self, name: str, character_type: str):
        self.name = name
        self.character_type = character_type  # ❌ Typ jako string

    def attack(self) -> str:
        # ❌ Wywołujemy funkcję zewnętrzną zamiast własnej metody
        weapon = create_weapon(self.character_type)
        return f"{self.name} attacks with {weapon.get_name()} for {weapon.get_damage()} damage!"


# ❌ Przykład użycia
if __name__ == "__main__":
    # Działa, ale nie jest elastyczne
    warrior = Character("Conan", "warrior")
    print(warrior.attack())

    mage = Character("Gandalf", "mage")
    print(mage.attack())

    # ❌ Chcę dodać Paladin z Mace?
    # Muszę:
    # 1. Stworzyć klasę Mace
    # 2. EDYTOWAĆ create_weapon() (dodać elif)
    # 3. Zapamiętać nowy string "paladin"
    #
    # Naruszenie Open/Closed Principle!


"""
Jakie problemy rozwiązuje Factory Method?

1. ❌ Naruszenie Open/Closed Principle
   - Dodanie Paladin wymaga EDYCJI create_weapon()
   - Nie można rozszerzyć bez modyfikacji

2. ❌ Brak polimorfizmu
   - Wszystkie postaci używają tej samej klasy Character
   - Postać przechowuje typ jako string, nie jako zachowanie

3. ❌ Centralizacja logiki tworzenia
   - Funkcja create_weapon() musi znać wszystkie typy
   - Im więcej postaci, tym dłuższa lista if/elif

4. ❌ Podatność na błędy
   - Łatwo o literówkę w stringu ("archr" zamiast "archer")
   - Brak sprawdzenia typów w compile-time

5. ❌ Trudne testowanie
   - Testowanie Character wymaga testowania wszystkich typów
   - Nie można testować każdej postaci w izolacji

Jak Factory Method to rozwiązuje?
1. Character staje się klasą abstrakcyjną z create_weapon() (Factory Method)
2. Każda postać (Warrior, Mage, Archer) dziedziczy po Character
3. Każda podklasa implementuje create_weapon() i zwraca odpowiednią broń
4. Brak centralnej funkcji - każda klasa decyduje co stworzyć
"""
