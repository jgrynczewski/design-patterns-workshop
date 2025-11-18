# 🎯 Singleton - Config Manager

**Poziom**: łatwy  
**Cel**: Singleton - jedna globalna instancja

## 🎯 Zadanie
Zaimplementuj wzorzec Singleton dla systemu zarządzania konfiguracją gry. `ConfigManager` musi gwarantować że istnieje tylko jedna instancja w całej aplikacji, aby wszystkie moduły współdzieliły ten sam stan.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `ConfigManager` gwarantuje jedną instancję
- [ ] Metoda `__new__` kontroluje tworzenie instancji
- [ ] Współdzielony stan między wszystkimi "instancjami"

## 🚀 Jak zacząć
1. Przejrzyj `problem.py` - zobacz problem z wieloma instancjami
   ```bash
   python problem.py
   ```
2. Otwórz `starter.py`
3. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest tests.py -v`
4. Zaimplementuj wzorzec Singleton w `ConfigManager`:
   - Zmienna klasowa `_instance` przechowuje jedyną instancję
   - Metoda `__new__` kontroluje tworzenie - zwraca `_instance` jeśli istnieje
5. Uruchom testy ponownie (teraz powinny przejść)

## 💡 Singleton w pigułce

**Singleton gwarantuje że klasa ma tylko JEDNĄ instancję**

### Jak to działa:
1. Zmienna klasowa `_instance` przechowuje jedyną instancję
2. Metoda `__new__` sprawdza czy `_instance` już istnieje
3. Jeśli tak - zwraca istniejącą, jeśli nie - tworzy nową
4. Wszystkie wywołania `ConfigManager()` zwracają TEN SAM obiekt

### ❌ Bez wzorca:
```python
class ConfigManager:
    def __init__(self):
        self._config = {}

# Problem: każde wywołanie = NOWA instancja
config1 = ConfigManager()
config1.set_config("theme", "dark")

config2 = ConfigManager()  # Nowa instancja!
config2.get_config("theme")  # None - utracona konfiguracja
```

### ✅ Z wzorcem (Singleton):
```python
# Ta sama instancja zawsze
config1 = ConfigManager()
config1.set_config("theme", "dark")

config2 = ConfigManager()  # Ta sama instancja!
config2.get_config("theme")  # "dark" - współdzielony stan
config1 is config2  # True
```

**Korzyść**: Jedna instancja = współdzielony globalny stan. Wszystkie moduły widzą tę samą konfigurację.

## ⚠️ Uwagi
- Singleton to kontrowersyjny wzorzec (global state, trudne testowanie)
- Przydatny dla: config, logging, cache management
- Ten przykład to **basic Singleton** (bez thread safety)
