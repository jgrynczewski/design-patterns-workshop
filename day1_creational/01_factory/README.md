# 🏭 Factory Method - System Bohaterów RPG

**Difficulty**: easy \
**Time**: 15 minutes \
**Focus**: Factory Method core concept

## 🎯 Zadanie
Implementuj wzorzec Factory Method do tworzenia różnych klas bohaterów w grze RPG.

## 📋 Wymagania
- [ ] `create_hero("warrior")` zwraca obiekt Warrior z mieczem i 100 HP
- [ ] `create_hero("mage")` zwraca obiekt Mage z różdżką i 60 HP
- [ ] `create_hero("archer")` zwraca obiekt Archer z łukiem i 80 HP
- [ ] Każdy bohater ma metody `attack()` i `get_stats()`
- [ ] Factory obsługuje case-insensitive input
- [ ] Proper error handling dla unknown types

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj klasy Warrior, Mage, Archer
4. Zaimplementuj funkcję `create_hero()`
5. Uruchom testy: `python -m pytest test_factory.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Sprawdź doctests w starter.py - pokazują expected behavior
- Użyj `hero_type.lower()` dla case-insensitive
- Każda klasa powinna dziedziczyć z `Character`

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Jeden wielki if/else - trudny do rozszerzania
def create_character(type):
  if type == "warrior":
      char = Character("Warrior", "sword", 100)
      char.setup_warrior_abilities()
      return char
  elif type == "mage":
      char = Character("Mage", "staff", 60)
      char.setup_mage_abilities()
      return char
  # Nowa klasa = modyfikacja tego kodu ❌
```

### ✅ Z wzorcem:
```python
# Każda klasa ma własną fabrykę
warrior = create_hero("warrior")  # → WarriorFactory  
mage = create_hero("mage")        # → MageFactory
new_class = create_hero("ninja")  # → NinjaFactory (zero zmian!)
```

Korzyść: Dodanie nowej klasy postaci nie wymaga modyfikacji istniejącego kodu
