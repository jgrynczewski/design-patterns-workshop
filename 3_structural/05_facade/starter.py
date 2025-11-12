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


# TODO: Zaimplementuj SmartHomeFacade
# Hint: Facade upraszcza interakcję z wieloma podsystemami
# Hint: evening_mode() - zapala światło (50%), termostat (22°C), TV ON
# Hint: leaving_home() - gasi światło, TV, uzbr Security

class SmartHomeFacade:
    """
    FACADE - upraszcza sterowanie inteligentnym domem

    Zamiast klient wywołujący 5+ metod dla każdej akcji,
    fasada wystawia 2 proste metody
    """

    def __init__(self):
        """
        TODO: Stwórz instancje podsystemów
        - self.light = Light()
        - self.thermostat = Thermostat()
        - self.security = SecuritySystem()
        - self.tv = TV()
        """
        pass

    def evening_mode(self) -> str:
        """
        Tryb wieczorny

        TODO: Wywołaj metody podsystemów:
        - light.dim(50)
        - thermostat.set_temperature(22)
        - security.disarm()
        - tv.turn_on()

        Zwróć połączone wyniki (każdy w nowej linii)
        """
        pass

    def leaving_home(self) -> str:
        """
        Wychodzenie z domu

        TODO: Wywołaj metody podsystemów:
        - light.turn_off()
        - thermostat.set_temperature(18)
        - security.arm()
        - tv.turn_off()

        Zwróć połączone wyniki (każdy w nowej linii)
        """
        pass


# Facade Pattern:
# Upraszcza interfejs do złożonego podsystemu
# Klient nie musi znać szczegółów Light, Thermostat, Security, TV
# Klient używa tylko evening_mode() i leaving_home()
