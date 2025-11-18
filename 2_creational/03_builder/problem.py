"""
❌ PROBLEM: Ogromny konstruktor z wieloma parametrami

Rozwiązanie bez wzorca Builder:
- Konstruktor z dziesiątkami parametrów
- Trudno zapamiętać kolejność parametrów
- Większość parametrów opcjonalna - trzeba podawać None
- Niemożliwe stopniowe budowanie obiektu
- Kod trudny do czytania i utrzymania
"""

from typing import List, Dict, Optional


class Character:
    """❌ Postać RPG z ogromnym konstruktorem"""

    def __init__(
        self,
        name: str,
        character_class: str,
        level: int = 1,
        strength: int = 10,
        intelligence: int = 10,
        dexterity: int = 10,
        constitution: int = 10,
        wisdom: int = 10,
        charisma: int = 10,
        skill1: Optional[str] = None,
        skill2: Optional[str] = None,
        skill3: Optional[str] = None,
        skill4: Optional[str] = None,
        skill5: Optional[str] = None,
        equipment1: Optional[str] = None,
        equipment2: Optional[str] = None,
        equipment3: Optional[str] = None,
        equipment4: Optional[str] = None,
        equipment5: Optional[str] = None,
    ):
        """
        ❌ PROBLEM: Konstruktor z 20+ parametrami!

        - Jaka kolejność?
        - Co jest wymagane, a co opcjonalne?
        - Jak dodać nowy parametr bez breaking changes?
        """
        self.name = name
        self.character_class = character_class
        self.level = level
        self.stats = {
            "strength": strength,
            "intelligence": intelligence,
            "dexterity": dexterity,
            "constitution": constitution,
            "wisdom": wisdom,
            "charisma": charisma,
        }
        # ❌ Umiejętności jako osobne parametry - nieelastyczne!
        self.skills = [s for s in [skill1, skill2, skill3, skill4, skill5] if s]
        self.equipment = [e for e in [equipment1, equipment2, equipment3, equipment4, equipment5] if e]

    def __str__(self) -> str:
        return f"{self.name} the {self.character_class} (Level {self.level})"


# ❌ Przykład użycia
if __name__ == "__main__":
    # ❌ PROBLEM 1: Ogromna liczba parametrów
    warrior = Character(
        name="Conan",
        character_class="warrior",
        level=10,
        strength=85,
        intelligence=40,
        dexterity=60,
        constitution=80,
        wisdom=45,
        charisma=50,
        skill1="sword mastery",
        skill2="shield bash",
        skill3="rage",
        skill4=None,  # ❌ Musimy podawać None dla niewykorzystanych
        skill5=None,
        equipment1="steel sword",
        equipment2="iron shield",
        equipment3="plate armor",
        equipment4=None,
        equipment5=None,
    )
    print(f"Created: {warrior}")

    # ❌ PROBLEM 2: Trudno zapamiętać kolejność
    # Co to był piąty parametr? strength czy dexterity?
    mage = Character("Gandalf", "mage", 50, 30, 95, 40, 50, 80, 70)
    # ❌ Niejasne - które statystyki to są?
    print(f"Created: {mage}")

    # ❌ PROBLEM 3: Niemożliwe stopniowe budowanie
    # Chcę najpierw stworzyć postać, potem dodać umiejętności?
    # Nie mogę - wszystko musi być w konstruktorze!

    # ❌ PROBLEM 4: Ograniczona liczba umiejętności/ekwipunku
    # Maksymalnie 5 umiejętności, 5 przedmiotów
    # Chcę więcej? Trzeba zmienić konstruktor!

    # ❌ PROBLEM 5: Kod nieczytelny
    archer = Character(
        "Legolas", "archer", 30, 60, 70, 95, 65, 80, 75,
        "archery", "stealth", "tracking", None, None,
        "elven bow", "quiver", "leather armor", None, None
    )
    # ❌ Która wartość to co? Niemożliwe zrozumieć bez dokumentacji!
    print(f"Created: {archer}")


"""
Jakie problemy rozwiązuje Builder?

1. ❌ Telescoping constructor problem
   - Konstruktor z dziesiątkami parametrów
   - Niemożliwe zapamiętać kolejności
   - Trudne utrzymanie

2. ❌ Brak czytelności
   - Character("Name", "class", 50, 30, 95, 40, 50, 80, 70, ...)
   - Co oznaczają te liczby?
   - Kod niesamodokumentujący się

3. ❌ Nieelastyczność
   - Ograniczona liczba umiejętności/ekwipunku
   - Dodanie nowego parametru = breaking change
   - Wszystkie wartości muszą być znane od razu

4. ❌ Brak walidacji w trakcie budowania
   - Można stworzyć postać bez nazwy
   - Można stworzyć postać bez klasy
   - Walidacja tylko po utworzeniu

5. ❌ Niemożliwe stopniowe budowanie
   - Nie można najpierw stworzyć bazowej postaci
   - Potem dodać umiejętności
   - Potem dodać ekwipunek
   - Wszystko na raz w konstruktorze

Jak Builder to rozwiązuje?
1. Fluent interface: builder.set_name("Conan").set_class("warrior").build()
2. Czytelne - każda operacja ma nazwę
3. Elastyczne - dowolna liczba umiejętności/ekwipunku
4. Walidacja w build()
5. Stopniowe budowanie - krok po kroku
6. Method chaining - zwracanie self dla łatwego łączenia
"""
