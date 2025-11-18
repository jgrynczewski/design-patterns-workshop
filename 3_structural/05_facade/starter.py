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


# Facade - ROZWIĄZANIE
# WZORZEC: Facade (fasada upraszczająca interfejs do podsystemów)

class SmartHomeFacade:
    """
    Fasada dla systemu inteligentnego domu

    Upraszcza interfejs do wielu podsystemów poprzez wystawienie
    metod wysokiego poziomu (evening_mode, leaving_home).
    Klient nie musi znać szczegółów Light, Thermostat, SecuritySystem, TV.
    """

    def __init__(self):
        """
        Konstruktor tworzy wszystkie podsystemy

        Facade jest odpowiedzialna za tworzenie i zarządzanie
        wszystkimi podsystemami - klient ich nie widzi.
        """
        self.light = Light()
        self.thermostat = Thermostat()
        self.security = SecuritySystem()
        self.tv = TV()

    def evening_mode(self) -> str:
        """
        Tryb wieczorny - koordynuje wszystkie podsystemy

        Jedna metoda zamiast czterech wywołań.
        Facade wie jaka sekwencja jest potrzebna.

        Returns:
            Połączone wyniki z wszystkich podsystemów
        """
        result = ""
        result += self.light.dim(50) + "\n"
        result += self.thermostat.set_temperature(22) + "\n"
        result += self.security.disarm() + "\n"
        result += self.tv.turn_on()
        return result

    def leaving_home(self) -> str:
        """
        Wychodzenie z domu - koordynuje wszystkie podsystemy

        Jedna metoda zamiast czterech wywołań.
        Facade wie jaka sekwencja jest potrzebna.

        Returns:
            Połączone wyniki z wszystkich podsystemów
        """
        result = ""
        result += self.light.turn_off() + "\n"
        result += self.thermostat.set_temperature(18) + "\n"
        result += self.security.arm() + "\n"
        result += self.tv.turn_off()
        return result


# Przykład użycia
if __name__ == "__main__":
    # Tworzenie fasady
    home = SmartHomeFacade()

    # Tryb wieczorny - jedno wywołanie zamiast czterech
    print("=== Evening Mode ===")
    print(home.evening_mode())

    print("\n=== Leaving Home ===")
    print(home.leaving_home())
