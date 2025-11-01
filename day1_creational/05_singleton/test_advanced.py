"""
Testy dla Advanced Thread-Safe Singleton Pattern - Game Manager
"""

import pytest
import threading
import time
from advanced_starter import GameManager


class TestThreadSafeSingleton:
    """Testy thread-safe wzorca Singleton"""

    def setup_method(self):
        """Reset przed każdym testem"""
        GameManager._instance = None
        GameManager._initialized = False

    def test_singleton_same_instance(self):
        """Test czy zawsze zwraca tę samą instancję"""
        gm1 = GameManager.get_instance()
        gm2 = GameManager.get_instance()
        gm3 = GameManager()

        assert gm1 is gm2
        assert gm2 is gm3
        assert gm1 is gm3

    def test_thread_safe_singleton_creation(self):
        """Test thread-safe tworzenia singleton"""
        instances = []

        def create_instance():
            instance = GameManager.get_instance()
            instances.append(instance)

        # Stwórz wiele wątków próbujących utworzyć instancję
        threads = []
        for _ in range(10):
            thread = threading.Thread(target=create_instance)
            threads.append(thread)

        # Uruchom wszystkie wątki jednocześnie
        for thread in threads:
            thread.start()

        # Poczekaj na zakończenie
        for thread in threads:
            thread.join()

        # Wszystkie instancje powinny być tym samym obiektem
        first_instance = instances[0]
        for instance in instances:
            assert instance is first_instance

    def test_initialization_only_once(self):
        """Test że inicjalizacja następuje tylko raz"""
        gm1 = GameManager.get_instance()
        gm1.add_player("TestPlayer")

        gm2 = GameManager.get_instance()

        # Drugi manager powinien widzieć gracza dodanego przez pierwszy
        assert gm2.get_player_count() == 1
        assert "TestPlayer" in gm2.get_players()


class TestPlayerManagement:
    """Testy zarządzania graczami"""

    def setup_method(self):
        """Reset przed każdym testem"""
        GameManager._instance = None
        GameManager._initialized = False

    def test_add_and_remove_players(self):
        """Test dodawania i usuwania graczy"""
        gm = GameManager.get_instance()

        # Dodaj graczy
        gm.add_player("Alice")
        gm.add_player("Bob")
        gm.add_player("Charlie")

        assert gm.get_player_count() == 3
        players = gm.get_players()
        assert "Alice" in players
        assert "Bob" in players
        assert "Charlie" in players

        # Usuń gracza
        removed = gm.remove_player("Bob")
        assert removed is True
        assert gm.get_player_count() == 2
        assert "Bob" not in gm.get_players()

        # Próba usunięcia nieistniejącego gracza
        removed = gm.remove_player("NonExistent")
        assert removed is False
        assert gm.get_player_count() == 2

    def test_thread_safe_player_operations(self):
        """Test thread-safe operacji na graczach"""
        gm = GameManager.get_instance()
        results = []

        def add_players(start_id, count):
            for i in range(start_id, start_id + count):
                gm.add_player(f"Player_{i}")
                time.sleep(0.001)  # Small delay to increase contention

        def remove_players(start_id, count):
            removed_count = 0
            for i in range(start_id, start_id + count):
                if gm.remove_player(f"Player_{i}"):
                    removed_count += 1
                time.sleep(0.001)
            results.append(removed_count)

        # Dodaj graczy w różnych wątkach
        add_threads = []
        for i in range(0, 20, 5):  # 4 wątki, każdy dodaje 5 graczy
            thread = threading.Thread(target=add_players, args=(i, 5))
            add_threads.append(thread)
            thread.start()

        for thread in add_threads:
            thread.join()

        # Sprawdź czy wszyscy gracze zostali dodani
        assert gm.get_player_count() == 20

        # Usuń graczy w różnych wątkach
        remove_threads = []
        for i in range(0, 20, 10):  # 2 wątki, każdy usuwa 10 graczy
            thread = threading.Thread(target=remove_players, args=(i, 10))
            remove_threads.append(thread)
            thread.start()

        for thread in remove_threads:
            thread.join()

        # Sprawdź rezultaty
        total_removed = sum(results)
        assert total_removed <= 20  # Nie można usunąć więcej niż było
        assert gm.get_player_count() == 20 - total_removed

    def test_get_players_returns_copy(self):
        """Test że get_players zwraca kopię dla thread safety"""
        gm = GameManager.get_instance()

        gm.add_player("Alice")
        gm.add_player("Bob")

        players1 = gm.get_players()
        players2 = gm.get_players()

        # Powinny być różnymi listami
        assert players1 is not players2
        # Ale z tą samą zawartością
        assert players1 == players2

        # Modyfikacja kopii nie powinna wpłynąć na oryginał
        players1.append("Hacker")
        assert "Hacker" not in gm.get_players()


class TestGameSettings:
    """Testy zarządzania ustawieniami gry"""

    def setup_method(self):
        """Reset przed każdym testem"""
        GameManager._instance = None
        GameManager._initialized = False

    def test_settings_management(self):
        """Test zarządzania ustawieniami"""
        gm = GameManager.get_instance()

        # Ustaw ustawienia
        gm.set_setting("difficulty", "hard")
        gm.set_setting("max_players", 8)
        gm.set_setting("pvp_enabled", True)

        # Pobierz ustawienia
        assert gm.get_setting("difficulty") == "hard"
        assert gm.get_setting("max_players") == 8
        assert gm.get_setting("pvp_enabled") is True

        # Test wartości domyślnej
        assert gm.get_setting("nonexistent", "default") == "default"

    def test_thread_safe_settings(self):
        """Test thread-safe operacji na ustawieniach"""
        gm = GameManager.get_instance()

        def set_settings(thread_id):
            for i in range(10):
                gm.set_setting(f"setting_{thread_id}_{i}", f"value_{thread_id}_{i}")
                time.sleep(0.001)

        # Uruchom wiele wątków ustawiających konfigurację
        threads = []
        for thread_id in range(5):
            thread = threading.Thread(target=set_settings, args=(thread_id,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Sprawdź czy wszystkie ustawienia zostały zapisane
        for thread_id in range(5):
            for i in range(10):
                key = f"setting_{thread_id}_{i}"
                expected_value = f"value_{thread_id}_{i}"
                assert gm.get_setting(key) == expected_value


class TestGameState:
    """Testy zarządzania stanem gry"""

    def setup_method(self):
        """Reset przed każdym testem"""
        GameManager._instance = None
        GameManager._initialized = False

    def test_game_state_management(self):
        """Test zarządzania stanem gry"""
        gm = GameManager.get_instance()

        # Stan domyślny
        assert gm.get_game_state() == "lobby"

        # Zmiana stanu
        gm.set_game_state("playing")
        assert gm.get_game_state() == "playing"

        gm.set_game_state("paused")
        assert gm.get_game_state() == "paused"

        gm.set_game_state("ended")
        assert gm.get_game_state() == "ended"

    def test_shared_state_across_instances(self):
        """Test współdzielonego stanu między instancjami"""
        gm1 = GameManager.get_instance()
        gm2 = GameManager.get_instance()

        # Zmiana przez gm1
        gm1.add_player("Alice")
        gm1.set_setting("difficulty", "expert")
        gm1.set_game_state("playing")

        # Sprawdź przez gm2
        assert gm2.get_player_count() == 1
        assert "Alice" in gm2.get_players()
        assert gm2.get_setting("difficulty") == "expert"
        assert gm2.get_game_state() == "playing"


class TestReset:
    """Testy funkcji reset"""

    def setup_method(self):
        """Reset przed każdym testem"""
        GameManager._instance = None
        GameManager._initialized = False

    def test_reset_functionality(self):
        """Test resetowania stanu gry"""
        gm = GameManager.get_instance()

        # Dodaj dane
        gm.add_player("Alice")
        gm.add_player("Bob")
        gm.set_setting("difficulty", "hard")
        gm.set_game_state("playing")

        # Sprawdź że dane są obecne
        assert gm.get_player_count() == 2
        assert gm.get_setting("difficulty") == "hard"
        assert gm.get_game_state() == "playing"

        # Reset
        gm.reset()

        # Sprawdź że dane zostały wyczyszczone
        assert gm.get_player_count() == 0
        assert gm.get_setting("difficulty") is None
        assert gm.get_game_state() == "lobby"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
