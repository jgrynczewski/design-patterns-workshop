# 🏭 Factory Method - Bronie RPG

**Poziom**: średni  
**Cel**: Factory Method - podklasy decydują co stworzyć

## 🎯 Zadanie
Zaimplementuj wzorzec Factory Method dla systemu broni w grze RPG. Każda postać (Warrior, Mage, Archer) tworzy swoją unikalną broń poprzez nadpisanie metody `create_weapon()`.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `Character` jest klasą abstrakcyjną z metodą `create_weapon()`
- [ ] Każda podklasa `Character` implementuje `create_weapon()` (Factory Method)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v` dla bardziej szczegółowego outputu)
3. Klasy broni (`Sword`, `Staff`, `Bow`) są już gotowe (STEP 1-2)
4. Zaimplementuj klasę `Character` (STEP 3)
   - Klasa abstrakcyjna z konstruktorem przyjmującym `name: str`
   - Abstrakcyjna metoda `create_weapon()` (Factory Method)
   - Metoda `attack()` używająca `create_weapon()`
5. Zaimplementuj klasy postaci: `Warrior`, `Mage`, `Archer` (STEP 4)
   - Każda dziedziczy po `Character`
   - Nadpisz metodę `create_weapon()` - każda zwraca odpowiednią broń
6. Uruchom testy ponownie (teraz powinny przejść)
7. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Lab XX - Factory Method"
   git push
   ```
8. Sprawdź wynik w GitHub Actions

## 💡 Factory Method w pigułce

**Factory Method deleguje tworzenie obiektów do podklas**

### Jak to działa:
1. Klasa bazowa (`Character`) definiuje abstrakcyjną metodę `create_weapon()`
2. Podklasy (`Warrior`, `Mage`, `Archer`) implementują tę metodę
3. Każda podklasa decyduje co stworzyć (Sword, Staff, Bow)

### Kluczowy moment:
```python
def attack(self) -> str:
    weapon = self.create_weapon()  # Wywołanie factory method
    # Character nie wie jaka broń zostanie stworzona!
```

- `Warrior.create_weapon()` → zwraca `Sword`
- `Mage.create_weapon()` → zwraca `Staff`
- `Archer.create_weapon()` → zwraca `Bow`

---

### ❌ Bez wzorca (Simple Factory):
```python
def create_weapon(character_type):
    if character_type == "warrior":
        return Sword()
    elif character_type == "mage":
        return Staff()
    
    # Nowa postać = edycja if/elif ❌
    elif character_type == "paladin":
        return Mace()
```

### ✅ Z wzorcem (Factory Method):
```python
class Paladin(Character):
    def create_weapon(self):
        return Mace()
# Nowa postać = nowa klasa, zero zmian w istniejącym kodzie ✅
```

**Korzyść**: Open/Closed Principle - dodawanie bez modyfikacji.
