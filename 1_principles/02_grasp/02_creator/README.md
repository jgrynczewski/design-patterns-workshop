# 🍽️ GRASP Creator - Restaurant

**Difficulty**: easy
**Time**: 10 minutes
**Focus**: GRASP Creator pattern

## 🎯 Zadanie
Zaimplementuj `Restaurant` - tworzy `Menu` i `Tables` (Creator pattern).

## 📋 Wymagania
- [ ] `Restaurant.__init__(name, tables_count)` - tworzy Menu i Tables
- [ ] `get_menu()` - zwraca Menu
- [ ] `get_tables()` - zwraca listę Tables (numery od 1)

## 🚀 Jak zacząć
```bash
cd day0_principles/02_grasp/02_creator
pytest test_creator.py -v
```

## 💡 GRASP Creator w pigułce

**Kto tworzy obiekt A? → Klasa B, która zawiera/agreguje A**

❌ **Źle** (klient tworzy komponenty):
```python
# Klient musi znać Menu i Tables
menu = Menu()
tables = [Table(i) for i in range(1, 11)]
restaurant = Restaurant("Luigi's", menu, tables)  # Złożone!
```

✅ **Dobrze** (Restaurant tworzy komponenty):
```python
class Restaurant:
    def __init__(self, name, tables_count):
        self.menu = Menu()  # Creator ✅
        self.tables = [Table(i) for i in range(1, tables_count + 1)]

# Klient ma prosty interfejs
restaurant = Restaurant("Luigi's", 10)  # Proste!
```

**Korzyść**: Restaurant wie jak stworzyć Menu i Tables - niskie sprzężenie z klientem.

**Kiedy B jest Creatorem dla A?**
- B zawiera/agreguje A
- B rejestruje A
- B blisko współpracuje z A
- B ma dane inicjalizujące A

Sprawdź `solution_creator.py` po wykonaniu.
