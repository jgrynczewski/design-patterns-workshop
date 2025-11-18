# 🏗️ Builder - Character Creator RPG

**Difficulty**: medium  
**Focus**: Builder pattern + fluent interface

## 🎯 Zadanie
Implementuj wzorzec Builder do tworzenia złożonych postaci RPG z różnymi atrybutami, umiejętnościami i ekwipunkiem.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `CharacterBuilder` z fluent interface (method chaining)
- [ ] Możliwość ustawiania: name, class, level, stats, skills, equipment
- [ ] Walidacja - character musi mieć name i class przed build()
- [ ] Reset() funkcjonalność dla reużycia buildera

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest tests.py -v`
3. Klasa `Character` jest już gotowa
4. Zaimplementuj `CharacterBuilder` z fluent interface (method chaining)
5. Uruchom testy ponownie (teraz powinny przejść)

## 💡 Podpowiedź
- **Fluent interface**: każda metoda zwraca `self` (method chaining)
- **Stopniowe budowanie**: buduj obiekt krok po kroku
- **Walidacja**: sprawdź wymagane pola w build()
- **Reset**: możliwość resetowania buildera do ponownego użycia
- Builder buduje złożone obiekty bez ogromnego konstruktora

## 🎮 Przykład użycia
```python
# Fluent interface - czytelne budowanie krok po kroku
character = (CharacterBuilder()
  .set_name("Gandalf")
  .set_class("mage")
  .set_level(50)
  .add_skill("fireball")
  .build())
```

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Ogromny konstruktor, trudny do użycia
character = Character(
  name="Gandalf",
  char_class="mage",
  level=50,
  strength=20, intelligence=95, dexterity=30, # ... 20 parametrów
  skills=["fireball", "heal", "teleport"],
  equipment=["staff", "robe", "ring"]
)  # Którą kolejność? Co jest opcjonalne? ❌
```

### ✅ Z wzorcem:

```python
# Czytelny, fluent interface
character = (CharacterBuilder()
  .set_name("Gandalf")
  .set_class("mage")
  .set_level(50)
  .add_skill("fireball")
  .build())  # Jasne, step-by-step ✅
```

Korzyść: Czytelne budowanie złożonych obiektów krok po kroku

🏗️ Builder vs Factory

- Factory: Tworzy proste obiekty jednym wywołaniem
- Builder: Buduje complex obiekty krok po kroku z customization
