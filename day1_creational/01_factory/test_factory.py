"""
Testy dla Factory Method Pattern - RPG Heroes
"""

import pytest
from starter import create_hero, Character


class TestFactoryMethod:
    """Testy wzorca Factory Method"""

    def test_create_warrior(self):
        """Test tworzenia wojownika"""
        warrior = create_hero("warrior")

        assert isinstance(warrior, Character)
        assert warrior.weapon == "sword"
        assert warrior.hp == 100
        assert "warrior" in warrior.name.lower()

    def test_create_mage(self):
        """Test tworzenia maga"""
        mage = create_hero("mage")

        assert isinstance(mage, Character)
        assert mage.weapon == "staff"
        assert mage.hp == 60
        assert "mage" in mage.name.lower()

    def test_create_archer(self):
        """Test tworzenia łucznika"""
        archer = create_hero("archer")

        assert isinstance(archer, Character)
        assert archer.weapon == "bow"
        assert archer.hp == 80
        assert "archer" in archer.name.lower()

    def test_hero_attack_method(self):
        """Test metody attack()"""
        warrior = create_hero("warrior")
        attack_msg = warrior.attack()

        assert isinstance(attack_msg, str)
        assert len(attack_msg) > 0

    def test_hero_get_stats(self):
        """Test metody get_stats()"""
        mage = create_hero("mage")
        stats = mage.get_stats()

        assert isinstance(stats, dict)
        assert "name" in stats
        assert "weapon" in stats
        assert "hp" in stats
        assert stats["weapon"] == "staff"
        assert stats["hp"] == 60

    def test_invalid_hero_type(self):
        """Test błędnego typu bohatera"""
        with pytest.raises(ValueError):
            create_hero("invalid_type")

    def test_case_insensitive(self):
        """Test czy factory działa z różnymi wielkościami liter"""
        warrior1 = create_hero("warrior")
        warrior2 = create_hero("WARRIOR")
        warrior3 = create_hero("Warrior")

        assert warrior1.weapon == warrior2.weapon == warrior3.weapon
        assert warrior1.hp == warrior2.hp == warrior3.hp


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
