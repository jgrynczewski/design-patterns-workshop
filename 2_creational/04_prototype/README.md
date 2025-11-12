# 📋 Prototype - Object Cloning RPG

**Difficulty**: easy \
**Time**: 15 minutes \
**Focus**: Prototype pattern + object cloning

## 🎯 Zadanie
Implementuj wzorzec Prototype do klonowania obiektów gry RPG zamiast tworzenia ich od zera.

## 📋 Wymagania
- [ ] `Character` z metodą `clone()`
- [ ] **Shallow copy** dla basic stats
- [ ] **Deep copy** dla equipment (lista)
- [ ] `PrototypeManager` do zarządzania szablonami
- [ ] Klonowanie różnych typów: enemies, items, spells
- [ ] Performance benefit vs constructor

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj `clone()` methods
4. Zaimplementuj PrototypeManager
5. Uruchom testy: `python -m pytest test_prototype.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Sprawdź doctests w starter.py - pokazują expected behavior
- Użyj `copy.copy()` dla shallow, `copy.deepcopy()` dla deep
- `clone()` powinien zwrócić nową instancję
- PrototypeManager jak registry wzorców

## 🎮 Use Cases
- **Enemies**: Sklonuj base_orc → army of orcs
- **Items**: Legendary sword template → player inventory  
- **Configurations**: Default settings → customized variants

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Kosztowne tworzenie za każdym razem
orc_army = []
for i in range(100):
  orc = Enemy("Orc")
  orc.load_graphics()      # Wolne I/O ❌
  orc.setup_ai()           # Kosztowne obliczenia ❌
  orc.configure_stats()    # Dużo pracy ❌
  orc_army.append(orc)
```

### ✅ Z wzorcem:

```python
# Szybkie klonowanie gotowego wzorca
base_orc = Enemy("Orc")  # Przygotuj raz
base_orc.load_graphics()
orc_army = [base_orc.clone() for _ in range(100)]  # Szybko! ✅
```

Korzyść: Szybkie tworzenie podobnych obiektów przez klonowanie
