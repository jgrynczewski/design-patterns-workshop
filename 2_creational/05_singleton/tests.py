"""
Testy dla Singleton Pattern - Config Manager
"""

import pytest
from starter import ConfigManager


class TestSingletonPattern:
    """Testy wzorca Singleton"""

    def setup_method(self):
        """Reset przed każdym testem"""
        # Reset singleton for clean tests
        ConfigManager._instance = None

    def test_singleton_same_instance(self):
        """Test czy zawsze zwraca tę samą instancję"""
        config1 = ConfigManager()
        config2 = ConfigManager()
        config3 = ConfigManager()

        assert config1 is config2
        assert config2 is config3
        assert config1 is config3

    def test_singleton_multiple_calls(self):
        """Test wielu wywołań konstruktora"""
        instances = [ConfigManager() for _ in range(10)]

        # Wszystkie powinny być tym samym obiektem
        first = instances[0]
        for instance in instances[1:]:
            assert instance is first

    def test_shared_state_between_instances(self):
        """Test współdzielonego stanu między instancjami - ISTOTA SINGLETONA"""
        config1 = ConfigManager()
        config2 = ConfigManager()

        # Ustawienie przez config1
        config1.set_config("player_name", "Alice")
        config1.set_config("level", 42)

        # config2 powinien widzieć te same wartości (ta sama instancja)
        assert config2.get_config("player_name") == "Alice"
        assert config2.get_config("level") == 42

        # Zmiana przez config2 powinna być widoczna w config1
        config2.set_config("score", 9999)
        assert config1.get_config("score") == 9999

    def test_set_and_get_config(self):
        """Test podstawowych operacji set/get"""
        config = ConfigManager()

        config.set_config("theme", "dark")
        config.set_config("difficulty", "hard")
        config.set_config("language", "en")

        assert config.get_config("theme") == "dark"
        assert config.get_config("difficulty") == "hard"
        assert config.get_config("language") == "en"

    def test_get_nonexistent_key(self):
        """Test pobierania nieistniejącego klucza"""
        config = ConfigManager()

        # Nieistniejący klucz powinien zwrócić None
        assert config.get_config("nonexistent") is None

    def test_different_value_types(self):
        """Test przechowywania różnych typów wartości"""
        config = ConfigManager()

        # Różne typy
        config.set_config("string_val", "hello")
        config.set_config("int_val", 42)
        config.set_config("bool_val", True)
        config.set_config("list_val", [1, 2, 3])

        # Sprawdź czy zachowują typy
        assert config.get_config("string_val") == "hello"
        assert config.get_config("int_val") == 42
        assert config.get_config("bool_val") is True
        assert config.get_config("list_val") == [1, 2, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])