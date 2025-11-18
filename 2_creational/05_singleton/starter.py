"""
Singleton Pattern - Config Manager

>>> import sys; sys.tracebacklimit = 0

>>> # Test singleton behavior - ta sama instancja
>>> config1 = ConfigManager()
>>> config2 = ConfigManager()
>>> config1 is config2
True

>>> # Test współdzielonego stanu
>>> config1.set_config("theme", "dark")
>>> config2.get_config("theme")
'dark'

>>> # Zmiana przez config2 widoczna w config1
>>> config2.set_config("language", "en")
>>> config1.get_config("language")
'en'
"""

from typing import Any, Dict


class ConfigManager:
    """
    Config Manager dla gry

    TODO: Zaimplementuj wzorzec Singleton
    - Zmienna klasowa _instance (początkowo None)
    - Metoda __new__(cls) kontrolująca tworzenie instancji
    - Inicjalizacja _config w __new__ (gdy tworzysz nową instancję)
    """

    def set_config(self, key: str, value: Any) -> None:
        """Ustawia wartość konfiguracji"""
        self._config[key] = value

    def get_config(self, key: str) -> Any:
        """Pobiera wartość konfiguracji"""
        return self._config.get(key)


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     # Test singleton
#     config1 = ConfigManager()
#     config2 = ConfigManager()
#
#     print(f"Same instance: {config1 is config2}")
#
#     # Test współdzielonego stanu
#     config1.set_config("theme", "dark")
#     config1.set_config("language", "en")
#
#     print(f"Theme from config1: {config1.get_config('theme')}")
#     print(f"Theme from config2: {config2.get_config('theme')}")
