"""
Facade Pattern - SmartHome System - SOLUTION

>>> home = SmartHomeFacade()
>>> result = home.evening_mode()
>>> "Light dimmed" in result
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


class SmartHomeFacade:
    """FACADE - upraszcza sterowanie inteligentnym domem"""

    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()
        self.security = SecuritySystem()
        self.tv = TV()

    def evening_mode(self) -> str:
        """Tryb wieczorny"""
        results = []
        results.append(self.light.dim(50))
        results.append(self.thermostat.set_temperature(22))
        results.append(self.security.disarm())
        results.append(self.tv.turn_on())
        return "\n".join(results)

    def leaving_home(self) -> str:
        """Wychodzenie z domu"""
        results = []
        results.append(self.light.turn_off())
        results.append(self.thermostat.set_temperature(18))
        results.append(self.security.arm())
        results.append(self.tv.turn_off())
        return "\n".join(results)


if __name__ == "__main__":
    print("=== Facade Pattern: SmartHome ===\n")

    home = SmartHomeFacade()

    print("Evening Mode:")
    print(home.evening_mode())
    print()

    print("Leaving Home:")
    print(home.leaving_home())
    print()

    print("Facade: Zamiast 4 wywołań → 1 metoda")
