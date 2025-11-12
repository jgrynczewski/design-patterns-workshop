# 🏭 Factory Method - RPG Weapons

**Difficulty**: easy  
**Focus**: Factory Method pattern - subclasses decide what to create

## 🎯 Zadanie
Zaimplementuj wzorzec Factory Method. Każda klasa postaci (Warrior, Mage, Archer) tworzy swoją unikalną broń poprzez nadpisanie metody `create_weapon()`.

## 📋 Wymagania
- [ ] `Warrior.create_weapon()` zwraca `Sword` (damage: 50)
- [ ] `Mage.create_weapon()` zwraca `Staff` (damage: 30)
- [ ] `Archer.create_weapon()` zwraca `Bow` (damage: 40)
- [ ] Wszystkie bronie implementują interfejs `Weapon`
- [ ] Metoda `attack()` używa factory method do stworzenia broni

## 🚀 Jak zacząć

### Krok 1: Przeczytaj `starter.py`

Zwróć uwagę na strukturę:
- **STEP 1**: Interfejs `Weapon` (już gotowy)
- **STEP 2**: Klasy broni `Sword`, `Staff`, `Bow` (TODO)
- **STEP 3**: Klasa `Character` z factory method (już gotowa)
- **STEP 4**: Klasy postaci `Warrior`, `Mage`, `Archer` (TODO)

### Krok 2: Zaimplementuj klasy broni (STEP 2)
```python
class Sword(Weapon):
    def get_name(self) -> str:
        return "Sword"

    def get_damage(self) -> int:
        return 50
```

Analogicznie dla `Staff` (damage: 30) i `Bow` (damage: 40).

### Krok 3: Zaimplementuj klasy postaci (STEP 4)
```python
class Warrior(Character):
    def create_weapon(self) -> Weapon:
        return Sword()  # Factory method - zwraca konkretną broń
```

Analogicznie dla `Mage` (zwraca `Staff`) i `Archer` (zwraca `Bow`).

### Krok 4: Testuj
```bash
# Doctests
python -m doctest -f -v starter.py

# Pytest
pytest test_factory.py -v
```

### Krok 5: Commit
```bash
git add starter.py
git commit -m "Implement Factory Method pattern"
git push
```

## 💡 Podpowiedzi

### Co to jest Factory Method?
**Factory Method** to wzorzec, w którym:
1. Klasa bazowa (`Character`) definiuje **abstrakcyjną metodę** `create_weapon()`
2. Podklasy (`Warrior`, `Mage`, `Archer`) **nadpisują** tę metodę
3. Każda podklasa decyduje, jaki obiekt stworzyć (Sword, Staff, Bow)

### Kluczowy moment
Spójrz na metodę `attack()` w `Character`:
```python
def attack(self) -> str:
    weapon = self.create_weapon()  # Wywołanie factory method
    return f"{self.name} attacks with {weapon.get_name()}..."
```

**`Character` nie wie, jaka broń zostanie stworzona!**
- Dla `Warrior` → `create_weapon()` zwróci `Sword`
- Dla `Mage` → `create_weapon()` zwróci `Staff`
- Dla `Archer` → `create_weapon()` zwróci `Bow`

To jest **delegacja tworzenia do podklas** - istota Factory Method.

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca (Simple Factory):
```python
def create_weapon(character_type: str):
    if character_type == "warrior":
        return Sword()
    elif character_type == "mage":
        return Staff()
    # Nowa broń = modyfikacja if/elif ❌
```

### ✅ Z wzorcem (Factory Method):
```python
class Warrior(Character):
    def create_weapon(self):  # Factory method
        return Sword()

# Nowa klasa postaci = nowa klasa, zero zmian w istniejącym kodzie ✅
class Paladin(Character):
    def create_weapon(self):
        return Mace()
```

**Korzyść**: Dodanie nowej postaci z nową bronią nie wymaga modyfikacji istniejącego kodu (Open/Closed Principle).

## 📚 Czym różni się od Simple Factory?

**Simple Factory**: Jedna funkcja decyduje o wszystkim
**Factory Method**: Każda podklasa decyduje za siebie

## 🎓 Po wykonaniu zadania

**Gratulacje!** Zaimplementowałeś Factory Method pattern. 🎉
