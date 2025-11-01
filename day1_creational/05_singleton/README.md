# 🎯 Singleton Pattern - RPG Management

**Difficulty**: easy → advanced \
**Time**: 12-25 minutes \
**Focus**: Singleton pattern (basic → thread-safe)

## 🎯 Zadanie
Implementuj wzorzec Singleton w dwóch wersjach - od prostej do zaawansowanej.

## 📊 Poziom 1: Config Manager (easy - 12 min)
**Plik**: `starter_basic.py`

### Wymagania:
- [ ] `ConfigManager` jako basic Singleton
- [ ] Zarządzanie ustawieniami gry (theme, difficulty, language)
- [ ] Metody: set_config, get_config, has_config
- [ ] Shared state między instancjami
- [ ] Bez threading complexity

### Jak zacząć:
1. Otwórz `starter_basic.py`
2. Uruchom doctests: `python -m doctest starter_basic.py -v`
3. Uruchom testy: `python -m pytest test_basic.py -v`

 ## ⭐ Poziom 2: Game Manager (advanced - 25 min)
 **Plik**: `starter_advanced.py`

 ### Wymagania:
- [ ] `GameManager` jako thread-safe Singleton
- [ ] Zarządzanie graczami i stanem gry
- [ ] Thread safety z `threading.Lock()`
- [ ] Metody: add_player, remove_player, get_player_count
- [ ] Production-ready implementation

### Jak zacząć:
1. Ukończ Poziom 1 najpierw!
2. Otwórz `starter_advanced.py`
3. Uruchom doctests: `python -m doctest starter_advanced.py -v`
4. Uruchom testy: `python -m pytest test_advanced.py -v`

 ## 💡 Podpowiedź
- **Poziom 1**: Focus na core Singleton concept
- **Poziom 2**: Dodaj threading considerations
- Sprawdź doctests w każdym pliku
- Zacznij od prostego, potem zaawansowany

## ⚠️ Uwagi
- Singleton to kontrowersyjny wzorzec (global state)
- W projektach produkcyjnych rozważ Dependency Injection
- Przydatny dla: config, logging, cache management

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Chaos z wieloma instancjami
config1 = GameConfig()
config1.set_difficulty("hard")

config2 = GameConfig()  # Nowa instancja! ❌
config2.get_difficulty()  # None - utracone ustawienia ❌
```

### ✅ Z wzorcem:

```python
# Jedna globalna instancja
config1 = GameManager.get_instance()
config1.set_difficulty("hard")

config2 = GameManager.get_instance()  # Ta sama instancja ✅
config2.get_difficulty()  # "hard" - zachowane! ✅
```

Korzyść: Gwarantuje jedną instancję z globalnym dostępem do stanu
