"""
Testy dla Facade Pattern - SmartHome
"""

import pytest
from starter import Light, Thermostat, SecuritySystem, TV, SmartHomeFacade


class TestFacade:
    """Testy Facade Pattern"""

    def test_light_subsystem(self):
        light = Light()
        assert light.turn_on() == "Light turned ON"
        assert light.turn_off() == "Light turned OFF"
        assert light.dim(50) == "Light dimmed to 50%"

    def test_thermostat_subsystem(self):
        thermostat = Thermostat()
        assert thermostat.set_temperature(22) == "Thermostat set to 22°C"

    def test_security_subsystem(self):
        security = SecuritySystem()
        assert security.arm() == "Security system ARMED"
        assert security.disarm() == "Security system DISARMED"

    def test_tv_subsystem(self):
        tv = TV()
        assert tv.turn_on() == "TV turned ON"
        assert tv.turn_off() == "TV turned OFF"

    def test_facade_evening_mode(self):
        """Facade upraszcza evening mode"""
        home = SmartHomeFacade()
        result = home.evening_mode()

        # Sprawdź czy wszystkie podsystemy zostały wywołane
        assert "Light dimmed to 50%" in result
        assert "Thermostat set to 22°C" in result
        assert "Security system DISARMED" in result
        assert "TV turned ON" in result

    def test_facade_leaving_home(self):
        """Facade upraszcza leaving home"""
        home = SmartHomeFacade()
        result = home.leaving_home()

        # Sprawdź czy wszystkie podsystemy zostały wywołane
        assert "Light turned OFF" in result
        assert "Thermostat set to 18°C" in result
        assert "Security system ARMED" in result
        assert "TV turned OFF" in result

    def test_facade_creates_subsystems(self):
        """Facade tworzy instancje podsystemów"""
        home = SmartHomeFacade()

        assert hasattr(home, 'light')
        assert hasattr(home, 'thermostat')
        assert hasattr(home, 'security')
        assert hasattr(home, 'tv')

        assert isinstance(home.light, Light)
        assert isinstance(home.thermostat, Thermostat)
        assert isinstance(home.security, SecuritySystem)
        assert isinstance(home.tv, TV)

    def test_facade_simplification(self):
        """
        Facade upraszcza interfejs:
        Bez facade: 4 wywołania
        Z facade: 1 wywołanie
        """
        home = SmartHomeFacade()

        # Pojedyncze wywołanie zamiast 4
        result = home.evening_mode()

        # Wynik zawiera działania wszystkich 4 podsystemów
        assert result.count("\n") >= 3  # Co najmniej 4 linie (3 \n)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
