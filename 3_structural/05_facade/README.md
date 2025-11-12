# 🏠 Facade - SmartHome System

**Difficulty**: easy
**Time**: 10 minutes
**Focus**: Facade pattern - simplifying complex subsystems

## 🎯 Zadanie
Zaimplementuj `SmartHomeFacade` - upraszcza sterowanie wieloma urządzeniami.

## 📋 Wymagania
- [ ] `SmartHomeFacade.__init__()` - tworzy Light, Thermostat, Security, TV
- [ ] `evening_mode()` - dim(50), temp(22), disarm, TV on
- [ ] `leaving_home()` - light off, temp(18), arm, TV off

## 🚀 Jak zacząć
```bash
cd day2_structural/05_facade
pytest test_facade.py -v
```

## 💡 Facade w pigułce

**Upraszcza interfejs do złożonego podsystemu**

❌ **Źle** (klient zna wszystkie podsystemy):
```python
# Klient wywołuje 4 klasy ❌
light = Light()
thermostat = Thermostat()
security = SecuritySystem()
tv = TV()

# Klient musi pamiętać sekwencję ❌
light.dim(50)
thermostat.set_temperature(22)
security.disarm()
tv.turn_on()
```

✅ **Dobrze** (Facade ukrywa złożoność):
```python
home = SmartHomeFacade()  # Jedna klasa ✅
home.evening_mode()       # Jedna metoda ✅

# Facade wywoła wszystkie 4 podsystemy w odpowiedniej kolejności
```

**Korzyść**: Klient nie zna Light/Thermostat/Security/TV - tylko Facade.

**Kiedy stosować**:
- Uproszczenie złożonego API
- Ukrycie legacy code
- Jeden punkt wejścia do wielu systemów

Sprawdź `solution_facade.py` po wykonaniu.
