# 🏠 Facade - SmartHome System

**Poziom**: łatwy
**Cel**: Facade - uproszczenie interfejsu do złożonych podsystemów

## 🎯 Zadanie
Zaimplementuj wzorzec Facade dla systemu inteligentnego domu. `SmartHomeFacade` upraszcza sterowanie wieloma urządzeniami poprzez wystawienie prostych metod wysokiego poziomu.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `SmartHomeFacade` tworzy wszystkie podsystemy w konstruktorze
- [ ] Metoda `evening_mode()` koordynuje wszystkie podsystemy
- [ ] Metoda `leaving_home()` koordynuje wszystkie podsystemy

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v` dla bardziej szczegółowego outputu)
3. Podsystemy (`Light`, `Thermostat`, `SecuritySystem`, `TV`) są już gotowe
4. Zaimplementuj klasę `SmartHomeFacade`:
   - Konstruktor tworzy instancje wszystkich podsystemów
   - Metoda `evening_mode()` - wywołuje odpowiednie metody podsystemów
   - Metoda `leaving_home()` - wywołuje odpowiednie metody podsystemów
5. Uruchom testy ponownie (teraz powinny przejść)
6. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Facade pattern"
   git push
   ```
7. Sprawdź wynik w GitHub Actions

## 💡 Facade w pigułce

**Facade deleguje pracę do wielu podsystemów i upraszcza interfejs**

### Jak to działa:
1. Facade tworzy instancje wszystkich podsystemów w konstruktorze
2. Klient wywołuje jedną metodę Facade (np. `evening_mode()`)
3. Facade koordynuje wywołania do wielu podsystemów w odpowiedniej kolejności

### Kluczowy moment:
```python
def evening_mode(self) -> str:
    # Facade wywołuje wiele podsystemów
    result1 = self.light.dim(50)
    result2 = self.thermostat.set_temperature(22)
    # ... itd
```

Klient nie musi znać `Light`, `Thermostat`, `SecuritySystem`, `TV` - tylko `SmartHomeFacade`.

---

### ❌ Bez wzorca:
```python
# Klient zarządza wszystkim
light = Light()
thermostat = Thermostat()
security = SecuritySystem()
tv = TV()

# Musi pamiętać sekwencję
light.dim(50)
thermostat.set_temperature(22)
security.disarm()
tv.turn_on()
```

### ✅ Z wzorcem (Facade):
```python
home = SmartHomeFacade()
home.evening_mode()
# Facade zarządza wszystkim wewnętrznie
```

**Korzyść**: Klient wywołuje jedną metodę zamiast czterech, bez znajomości implementacji podsystemów.
