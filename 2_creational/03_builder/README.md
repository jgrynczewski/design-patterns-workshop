# 🏗️ Builder - Character Creator RPG

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Builder pattern + fluent interface

## 🎯 Zadanie
Implementuj wzorzec Builder do tworzenia złożonych postaci RPG z różnymi atrybutami, umiejętnościami i ekwipunkiem.

## 📋 Wymagania
- [ ] `CharacterBuilder` z fluent interface (method chaining)
- [ ] Możliwość ustawiania: name, class, level, stats, skills, equipment
- [ ] `CharacterDirector` z predefiniowanymi buildami (BeginnerWarrior, EliteMage, etc.)
- [ ] Walidacja - character musi mieć name i class przed build()
- [ ] Reset() funkcjonalność dla reużycia builder
- [ ] `create_custom_character()` helper function

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Sprawdź `# %% Hints` section dla technical tips
3. Uruchom doctests: `python -m doctest starter.py -v`
4. Zaimplementuj CharacterBuilder z fluent interface
5. Zaimplementuj CharacterDirector z presets
6. Uruchom testy: `python -m pytest test_builder.py -v`
7. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź (Conceptual)
- **Builder** buduje complex objects step by step
- **Fluent interface** = method chaining (`builder.set_name().set_class().build()`)
- **Director** zawiera predefiniowane "przepisy" na popularne buildy
- **Validation** - sprawdź required fields przed build()
- **Reset** pozwala reużyć tego samego builder dla wielu characters

## 🎮 Przykład użycia
```python
# Fluent interface
character = (CharacterBuilder()
  .set_name("Gandalf")
  .set_class("mage")
  .set_level(50)
  .add_skill("fireball")
  .build())

# Director pattern
director = CharacterDirector()
beginner = director.create_beginner_warrior("Conan")
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
