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


# %% Subsystems - GOTOWE
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


# %% Facade - DO IMPLEMENTACJI
# WZORZEC: Facade (fasada upraszczająca interfejs do podsystemów)

# TODO: Zaimplementuj klasę SmartHomeFacade
# Konstruktor:
#   - Tworzy instancje wszystkich podsystemów (Light, Thermostat, SecuritySystem, TV)
#   - Przechowuje je jako atrybuty (self.light, self.thermostat, self.security, self.tv)
#
# Metoda evening_mode() -> str:
#   - Wywołuje: light.dim(50), thermostat.set_temperature(22), security.disarm(), tv.turn_on()
#   - Zwraca połączone wyniki oddzielone znakiem nowej linii (\n)
#
# Metoda leaving_home() -> str:
#   - Wywołuje: light.turn_off(), thermostat.set_temperature(18), security.arm(), tv.turn_off()
#   - Zwraca połączone wyniki oddzielone znakiem nowej linii (\n)

class SmartHomeFacade:
    pass
