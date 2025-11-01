# %% About
# - Name: Singleton - Config Manager (Basic)
# - Difficulty: easy
# - Lines: 8
# - Minutes: 12
# - Focus: Basic Singleton pattern

# %% Description
"""
Singleton Pattern - Config Manager
Zaimplementuj podstawowy wzorzec Singleton dla zarządzania konfiguracją gry.
"""

from typing import Any, Dict

# %% Hints
# - Use __new__ method to control instance creation
# - Store single instance in class variable _instance
# - Simple if/else check - no threading needed
# - Initialize config dict only once

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test singleton behavior
>>> config1 = ConfigManager()
>>> config2 = ConfigManager()
>>> config1 is config2
True

>>> # Test config management
>>> config1.set_config("theme", "dark")
>>> config1.set_config("difficulty", "medium")
>>> config1.get_config("theme")
'dark'

>>> # Test shared state
>>> config2.get_config("theme")
'dark'
>>> config2.get_config("difficulty")  
'medium'

>>> # Test default values
>>> config1.get_config("nonexistent", "default_value")
'default_value'

>>> # Test has_config
>>> config1.has_config("theme")
True
>>> config1.has_config("nonexistent")
False

>>> # Test config count
>>> len(config1.get_all_configs())
2
"""


# %% Run
# - PyCharm: right-click and `Run Doctest in ...`
# - Terminal: `python -m doctest -f -v basic_starter.py`
# - Tests: `python -m pytest basic_test.py -v`

# %% TODO: Implement Basic Singleton ConfigManager

class ConfigManager:
    """
    Basic Singleton Config Manager dla gry RPG

    Zarządza ustawieniami gry w sposób centralny.
    Jedna instancja dla całej aplikacji.
    """

    _instance = None

    def __new__(cls):
        """
        Kontroluje tworzenie instancji - tylko jedna może istnieć

        Returns:
            Jedyna instancja ConfigManager
        """
        # TODO: Zaimplementuj basic singleton logic
        pass

    def __init__(self):
        """Inicjalizuje config dict tylko raz"""
        # TODO: Zaimplementuj inicjalizację (tylko przy pierwszym wywołaniu)
        # Hint: sprawdź czy już zainicjalizowane
        pass

    def set_config(self, key: str, value: Any) -> None:
        """
        Ustawia wartość konfiguracji

        Args:
            key: Klucz konfiguracji (np. "theme", "difficulty")
            value: Wartość do ustawienia
        """
        # TODO: Zaimplementuj
        pass

    def get_config(self, key: str, default: Any = None) -> Any:
        """
        Pobiera wartość konfiguracji

        Args:
            key: Klucz konfiguracji
            default: Wartość domyślna jeśli klucz nie istnieje

        Returns:
            Wartość konfiguracji lub default
        """
        # TODO: Zaimplementuj
        pass

    def has_config(self, key: str) -> bool:
        """
        Sprawdza czy konfiguracja istnieje

        Args:
            key: Klucz do sprawdzenia

        Returns:
            True jeśli klucz istnieje
        """
        # TODO: Zaimplementuj
        pass

    def get_all_configs(self) -> Dict[str, Any]:
        """
        Zwraca wszystkie konfiguracje

        Returns:
            Słownik wszystkich konfiguracji
        """
        # TODO: Zaimplementuj
        pass

    def reset_configs(self) -> None:
        """Resetuje wszystkie konfiguracje (przydatne do testów)"""
        # TODO: Zaimplementuj
        pass

# %% Example Usage
# Odkomentuj gdy zaimplementujesz
# if __name__ == "__main__":
#     # Test singleton
#     config1 = ConfigManager()
#     config2 = ConfigManager()
#
#     print(f"Same instance: {config1 is config2}")
#
#     # Test functionality
#     config1.set_config("theme", "dark")
#     config1.set_config("language", "en")
#
#     print(f"Theme from config1: {config1.get_config('theme')}")
#     print(f"Theme from config2: {config2.get_config('theme')}")
#     print(f"All configs: {config1.get_all_configs()}")
