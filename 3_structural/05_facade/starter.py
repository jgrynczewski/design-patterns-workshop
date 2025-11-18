"""
Facade Pattern - SmartHome System

>>> # Test subsystems
>>> light = Light()
>>> light.turn_on()
'Light turned ON'
>>> light.turn_off()
'Light turned OFF'

>>> thermostat = Thermostat()
>>> thermostat.set_temperature(22)
'Thermostat set to 22°C'

>>> security = SecuritySystem()
>>> security.arm()
'Security system ARMED'

>>> tv = TV()
>>> tv.turn_on()
'TV turned ON'

>>> # Test SmartHomeFacade
>>> home = SmartHomeFacade()
>>> result = home.evening_mode()
>>> "Light" in result and "Thermostat" in result
True

>>> result = home.leaving_home()
>>> "turned OFF" in result and "ARMED" in result
True
"""


# Subsystems - GOTOWE
# WZORZEC: Subsystem (podsystem ukryty za Facade)

class Light:
    """Podsystem - oświetlenie"""

    def turn_on(self) -> str:
        return "Light turned ON"

    def turn_off(self) -> str:
        return "Light turned OFF"

    def dim(self, level: int) -> str:
        return f"Light dimmed to {level}%"


class Thermostat:
    """Podsystem - termostat"""

    def set_temperature(self, temp: int) -> str:
        return f"Thermostat set to {temp}°C"


class SecuritySystem:
    """Podsystem - alarm"""

    def arm(self) -> str:
        return "Security system ARMED"

    def disarm(self) -> str:
        return "Security system DISARMED"


class TV:
    """Podsystem - telewizor"""

    def turn_on(self) -> str:
        return "TV turned ON"

    def turn_off(self) -> str:
        return "TV turned OFF"


# Facade - DO IMPLEMENTACJI
# WZORZEC: Facade (fasada upraszczająca interfejs do podsystemów)

# TODO: Zaimplementuj SmartHomeFacade
# Konstruktor tworzy wszystkie podsystemy (kompozycja)
# Metoda evening_mode() - koordynuje podsystemy (patrz sekwencja w problem.py)
# Metoda leaving_home() - koordynuje podsystemy (patrz sekwencja w problem.py)

class SmartHomeFacade:
    pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     # Tworzenie fasady
#     home = SmartHomeFacade()
#
#     # Tryb wieczorny - jedno wywołanie zamiast czterech
#     print("=== Evening Mode ===")
#     print(home.evening_mode())
#
#     print("\n=== Leaving Home ===")
#     print(home.leaving_home())
