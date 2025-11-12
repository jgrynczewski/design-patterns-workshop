"""
Testy dla Basic Singleton Pattern - Config Manager
"""

import pytest
from basic_starter import ConfigManager


class TestBasicSingleton:
    """Testy podstawowego wzorca Singleton"""

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


class TestConfigManagement:
    """Testy zarządzania konfiguracją"""

    def setup_method(self):
        """Reset przed każdym testem"""
        ConfigManager._instance = None

    def test_set_and_get_config(self):
        """Test ustawiania i pobierania konfiguracji"""
        config = ConfigManager()

        config.set_config("theme", "dark")
        config.set_config("difficulty", "hard")
        config.set_config("language", "en")

        assert config.get_config("theme") == "dark"
        assert config.get_config("difficulty") == "hard"
        assert config.get_config("language") == "en"

    def test_shared_state_between_instances(self):
        """Test współdzielonego stanu między instancjami"""
        config1 = ConfigManager()
        config2 = ConfigManager()

        config1.set_config("player_name", "Alice")
        config1.set_config("level", 42)

        # config2 powinien widzieć te same wartości
        assert config2.get_config("player_name") == "Alice"
        assert config2.get_config("level") == 42

        # Zmiana przez config2 powinna być widoczna w config1
        config2.set_config("score", 9999)
        assert config1.get_config("score") == 9999

    def test_get_config_with_default(self):
        """Test pobierania z wartością domyślną"""
        config = ConfigManager()

        # Klucz nie istnieje - powinien zwrócić default
        assert config.get_config("nonexistent", "default") == "default"
        assert config.get_config("missing", 123) == 123
        assert config.get_config("nothing") is None

        # Istniejący klucz - powinien zwrócić rzeczywistą wartość
        config.set_config("existing", "value")
        assert config.get_config("existing", "default") == "value"

    def test_has_config(self):
        """Test sprawdzania istnienia konfiguracji"""
        config = ConfigManager()

        # Początkowo pusty
        assert not config.has_config("anything")

        # Po dodaniu
        config.set_config("theme", "light")
        assert config.has_config("theme")
        assert not config.has_config("nonexistent")

    def test_get_all_configs(self):
        """Test pobierania wszystkich konfiguracji"""
        config = ConfigManager()

        # Początkowo pusty
        all_configs = config.get_all_configs()
        assert isinstance(all_configs, dict)
        assert len(all_configs) == 0

        # Po dodaniu kilku
        config.set_config("theme", "dark")
        config.set_config("difficulty", "medium")
        config.set_config("sound", True)

        all_configs = config.get_all_configs()
        assert len(all_configs) == 3
        assert all_configs["theme"] == "dark"
        assert all_configs["difficulty"] == "medium"
        assert all_configs["sound"] is True

    def test_reset_configs(self):
        """Test resetowania konfiguracji"""
        config = ConfigManager()

        # Dodaj kilka konfiguracji
        config.set_config("theme", "dark")
        config.set_config("language", "pl")
        assert len(config.get_all_configs()) == 2

        # Reset
        config.reset_configs()
        assert len(config.get_all_configs()) == 0
        assert not config.has_config("theme")
        assert not config.has_config("language")


class TestConfigTypes:
    """Test różnych typów wartości konfiguracji"""

    def setup_method(self):
        """Reset przed każdym testem"""
        ConfigManager._instance = None

    def test_different_value_types(self):
        """Test przechowywania różnych typów wartości"""
        config = ConfigManager()

        # Różne typy
        config.set_config("string_val", "hello")
        config.set_config("int_val", 42)
        config.set_config("float_val", 3.14)
        config.set_config("bool_val", True)
        config.set_config("list_val", [1, 2, 3])
        config.set_config("dict_val", {"nested": "value"})

        # Sprawdź czy zachowują typy
        assert config.get_config("string_val") == "hello"
        assert config.get_config("int_val") == 42
        assert config.get_config("float_val") == 3.14
        assert config.get_config("bool_val") is True
        assert config.get_config("list_val") == [1, 2, 3]
        assert config.get_config("dict_val") == {"nested": "value"}

    def test_overwrite_values(self):
        """Test nadpisywania wartości"""
        config = ConfigManager()

        config.set_config("changeable", "original")
        assert config.get_config("changeable") == "original"

        config.set_config("changeable", "updated")
        assert config.get_config("changeable") == "updated"

        # Zmiana typu
        config.set_config("changeable", 999)
        assert config.get_config("changeable") == 999


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
