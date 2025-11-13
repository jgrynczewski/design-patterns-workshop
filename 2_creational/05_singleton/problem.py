# Problem bez wzorca Singleton
# Pokazuje chaos z wieloma instancjami zarządzającymi konfiguracją

from typing import Any, Dict


# ❌ PROBLEM: Zwykła klasa - każde wywołanie tworzy NOWĄ instancję
class ConfigManager:
    """
    Config Manager BEZ wzorca Singleton

    Problem: Każde ConfigManager() tworzy NOWĄ instancję z WŁASNYM stanem
    """

    def __init__(self):
        # ❌ Każda instancja ma SWÓJ słownik - brak współdzielonego stanu!
        self._config: Dict[str, Any] = {}

    # Metody pomocnicze (nie związane z wzorcem)
    def set_config(self, key: str, value: Any) -> None:
        self._config[key] = value

    def get_config(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)


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
Jakie problemy rozwiązuje Singleton?

1. ❌ Utrata stanu między modułami
   - Każdy moduł tworzy swoją instancję ConfigManager
   - Logger ustawia log_level, ale Graphics tego nie widzi
   - Brak współdzielonego globalnego stanu

2. ❌ Duplikacja danych
   - Wiele instancji = wiele kopii tej samej konfiguracji
   - Marnowanie pamięci
   - Niespójność: różne instancje mogą mieć różne wartości

3. ❌ Brak kontroli nad liczbą instancji
   - Nic nie powstrzymuje programisty przed ConfigManager() × 100
   - Trudno debugować: która instancja jest "prawdziwa"?
   - Chaotyczny dostęp do konfiguracji

4. ❌ Trudne testowanie
   - Nie wiadomo która instancja jest używana w testach
   - Cleanup po testach: trzeba znaleźć WSZYSTKIE instancje
   - Izolacja testów: jedna test tworzy instancję, inna może ją nadpisać

Jak Singleton to rozwiązuje?
1. Tylko JEDNA instancja w całej aplikacji (kontrolowane przez __new__)
2. Współdzielony globalny stan - wszystkie moduły widzą te same dane
3. config1 = ConfigManager(); config2 = ConfigManager() → config1 is config2 (True)
4. Łatwy reset w testach: ConfigManager._instance = None
"""
