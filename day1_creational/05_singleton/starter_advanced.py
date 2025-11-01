# %% About
# - Name: Singleton - Game Manager (Advanced)
# - Difficulty: medium
# - Lines: 15
# - Minutes: 25
# - Focus: Thread-safe Singleton pattern

# %% Description
"""
Singleton Pattern - Game Manager (Thread-Safe)
Zaimplementuj zaawansowany wzorzec Singleton z thread safety dla zarządzania grą.
"""

import threading
from typing import List, Dict, Any, Optional

# %% Hints
# - Use __new__ method with threading.Lock()
# - Double-checked locking pattern for performance
# - Initialize data structures only once
# - Protect shared state modifications with locks

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0

>>> # Test singleton behavior
>>> gm1 = GameManager.get_instance()
>>> gm2 = GameManager.get_instance()
>>> gm1 is gm2
True

>>> # Test player management
>>> gm1.add_player("Alice")
>>> gm1.add_player("Bob")
>>> gm1.get_player_count()
2

>>> # Test shared state
>>> gm2.get_player_count()
2
>>> "Alice" in gm2.get_players()
True

>>> # Test remove player
>>> gm1.remove_player("Alice")
>>> gm2.get_player_count()
1
>>> "Alice" in gm1.get_players()
False

>>> # Test settings
>>> gm1.set_setting("difficulty", "hard")
>>> gm2.get_setting("difficulty")
'hard'

>>> # Test game state
>>> gm1.set_game_state("playing")
>>> gm2.get_game_state()
'playing'

>>> # Test reset (for testing purposes)
>>> gm1.reset()
>>> gm1.get_player_count()
0
>>> gm1.get_game_state()
'lobby'
"""


# %% Run
# - PyCharm: right-click and `Run Doctest in ...`
# - Terminal: `python -m doctest -f -v advanced_starter.py`
# - Tests: `python -m pytest advanced_test.py -v`

# %% TODO: Implement Thread-Safe Singleton GameManager

class GameManager:
    """
    Thread-Safe Singleton Game Manager dla gry RPG

    Zarządza stanem gry, graczami i ustawieniami w sposób bezpieczny dla wielowątkowości.
    """

    _instance: Optional['GameManager'] = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls) -> 'GameManager':
        """
        Thread-safe kontrola tworzenia instancji

        Returns:
            Jedyna instancja GameManager
        """
        # TODO: Zaimplementuj double-checked locking pattern
        # Hint: sprawdź _instance dwa razy - przed i w środku lock
        pass

    def __init__(self):
        """Inicjalizuje manager tylko raz (thread-safe)"""
        # TODO: Zaimplementuj thread-safe inicjalizację
        # Hint: użyj _initialized flag żeby nie inicjalizować wielokrotnie
        pass

    @classmethod
    def get_instance(cls) -> 'GameManager':
        """
        Publiczny interfejs do dostępu do singleton

        Returns:
            Jedyna instancja GameManager
        """
        # TODO: Zaimplementuj - wywołaj konstruktor
        pass

    def add_player(self, player_name: str) -> None:
        """
        Dodaje gracza do gry (thread-safe)

        Args:
            player_name: Nazwa gracza do dodania
        """
        # TODO: Zaimplementuj z thread safety
        pass

    def remove_player(self, player_name: str) -> bool:
        """
        Usuwa gracza z gry (thread-safe)

        Args:
            player_name: Nazwa gracza do usunięcia

        Returns:
            True jeśli gracz został usunięty, False jeśli nie istniał
        """
        # TODO: Zaimplementuj z thread safety
        pass

    def get_player_count(self) -> int:
        """
        Zwraca liczbę graczy (thread-safe read)

        Returns:
            Liczba graczy w grze
        """
        # TODO: Zaimplementuj
        pass

    def get_players(self) -> List[str]:
        """
        Zwraca kopię listy graczy (thread-safe)

        Returns:
            Lista nazw graczy
        """
        # TODO: Zaimplementuj - zwróć kopię dla thread safety
        pass

    def set_setting(self, key: str, value: Any) -> None:
        """
        Ustawia konfigurację gry (thread-safe)

        Args:
            key: Klucz ustawienia
            value: Wartość ustawienia
        """
        # TODO: Zaimplementuj z thread safety
        pass

    def get_setting(self, key: str, default: Any = None) -> Any:
        """
        Pobiera ustawienie gry (thread-safe)

        Args:
            key: Klucz ustawienia
            default: Wartość domyślna

        Returns:
            Wartość ustawienia lub default
        """
        # TODO: Zaimplementuj
        pass

    def set_game_state(self, state: str) -> None:
        """
        Ustawia stan gry (thread-safe)

        Args:
            state: Nowy stan gry (lobby, playing, paused, ended)
        """
        # TODO: Zaimplementuj z walidacją stanów
        pass

    def get_game_state(self) -> str:
        """
        Pobiera aktualny stan gry

        Returns:
            Aktualny stan gry
        """
        # TODO: Zaimplementuj
        pass

    def reset(self) -> None:
        """
        Resetuje stan gry (thread-safe, przydatne do testów)
        """
        # TODO: Zaimplementuj - wyczyść wszystkie dane
        pass

# %% Example Usage
# Odkomentuj gdy zaimplementujesz
# if __name__ == "__main__":
#     import threading
#     import time
#
#     # Test thread safety
#     def worker(worker_id):
#         gm = GameManager.get_instance()
#         gm.add_player(f"Player_{worker_id}")
#         time.sleep(0.1)  # Simulate work
#         print(f"Worker {worker_id}: {gm.get_player_count()} players")
#
#     # Create multiple threads
#     threads = []
#     for i in range(5):
#         t = threading.Thread(target=worker, args=(i,))
#         threads.append(t)
#         t.start()
#
#     # Wait for all threads
#     for t in threads:
#         t.join()
#
#     # Final check
#     gm = GameManager.get_instance()
#     print(f"Final players: {gm.get_players()}")
