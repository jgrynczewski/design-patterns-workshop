"""
❌ PROBLEM: Brak wzorca Singleton - wiele instancji, utrata stanu

Problem: Każde ConfigManager() tworzy NOWĄ instancję z WŁASNYM stanem
- Brak współdzielonego globalnego stanu
- Różne moduły widzą różne wartości
- Chaos z wieloma instancjami
"""

from typing import Any, Dict


class ConfigManager:
    """
    Config Manager BEZ wzorca Singleton

    ❌ Problem: Każde wywołanie ConfigManager() = NOWA instancja
    """

    def __init__(self):
        # ❌ Każda instancja ma SWÓJ słownik - brak współdzielenia!
        self._config: Dict[str, Any] = {}

    def set_config(self, key: str, value: Any) -> None:
        """Ustawia wartość konfiguracji"""
        self._config[key] = value

    def get_config(self, key: str) -> Any:
        """Pobiera wartość konfiguracji"""
        return self._config.get(key)


# ❌ Przykład użycia
if __name__ == "__main__":
    # Moduł logowania tworzy config
    config_logger = ConfigManager()
    config_logger.set_config("log_level", "DEBUG")
    print(f"Logger set: log_level=DEBUG")

    # Moduł grafiki tworzy config
    config_graphics = ConfigManager()
    config_graphics.set_config("theme", "dark")
    print(f"Graphics set: theme=dark")

    # ❌ Graphics nie widzi ustawień loggera (różne instancje)
    print(f"Graphics reads log_level: {config_graphics.get_config('log_level')}")  # None!

    # ❌ Logger nie widzi ustawień graphics (różne instancje)
    print(f"Logger reads theme: {config_logger.get_config('theme')}")  # None!

    # ❌ Każde wywołanie ConfigManager() = nowa instancja
    print(f"\nconfig_logger is config_graphics? {config_logger is config_graphics}")  # False


"""
Dlaczego to jest ZŁE?

1. ❌ Utrata stanu między modułami
   - Każdy moduł tworzy swoją instancję ConfigManager
   - Logger ustawia log_level, ale Graphics tego nie widzi
   - Brak współdzielonego globalnego stanu

2. ❌ Duplikacja danych
   - Wiele instancji = wiele kopii tej samej konfiguracji
   - Marnowanie pamięci
   - Niespójność: różne instancje mogą mieć różne wartości

3. ❌ Brak kontroli nad liczbą instancji
   - Nic nie powstrzymuje przed ConfigManager() × 100
   - Trudno debugować: która instancja jest "prawdziwa"?
   - Chaotyczny dostęp do konfiguracji

Jak Singleton to rozwiązuje?
1. Tylko JEDNA instancja w całej aplikacji (kontrolowane przez __new__)
2. Współdzielony globalny stan - wszystkie moduły widzą te same dane
3. config1 = ConfigManager(); config2 = ConfigManager() → config1 is config2 (True)
4. Implementacja: _instance = None + __new__ sprawdzający czy instancja już istnieje
"""
