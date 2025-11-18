"""
Testy dla Abstract Factory Pattern - RPG Equipment
"""

import pytest
from starter import (
    EquipmentFactory,
    Weapon,
    Armor,
    WarriorEquipmentFactory,
    MageEquipmentFactory,
    ArcherEquipmentFactory
)


class TestFactoriesImplementInterface:
    """Testy czy fabryki implementują interfejs EquipmentFactory"""

    def test_warrior_factory_is_equipment_factory(self):
        """Test czy WarriorEquipmentFactory dziedziczy po EquipmentFactory"""
        factory = WarriorEquipmentFactory()
        assert isinstance(factory, EquipmentFactory)

    def test_mage_factory_is_equipment_factory(self):
        """Test czy MageEquipmentFactory dziedziczy po EquipmentFactory"""
        factory = MageEquipmentFactory()
        assert isinstance(factory, EquipmentFactory)

    def test_archer_factory_is_equipment_factory(self):
        """Test czy ArcherEquipmentFactory dziedziczy po EquipmentFactory"""
        factory = ArcherEquipmentFactory()
        assert isinstance(factory, EquipmentFactory)


class TestWarriorEquipment:
    """Testy ekwipunku wojownika"""

    def test_warrior_weapon(self):
        """Test broni wojownika"""
        factory = WarriorEquipmentFactory()
        weapon = factory.create_weapon()

        assert isinstance(weapon, Weapon)
        assert weapon.damage() >= 80  # High damage dla warrior
        assert "sword" in weapon.get_name().lower()

    def test_warrior_armor(self):
        """Test pancerza wojownika"""
        factory = WarriorEquipmentFactory()
        armor = factory.create_armor()

        assert isinstance(armor, Armor)
        assert armor.defense() >= 50  # High defense dla warrior
        assert any(word in armor.get_name().lower() for word in ["heavy", "plate", "mail"])


class TestMageEquipment:
    """Testy ekwipunku maga"""

    def test_mage_weapon(self):
        """Test broni maga"""
        factory = MageEquipmentFactory()
        weapon = factory.create_weapon()

        assert isinstance(weapon, Weapon)
        assert weapon.damage() >= 40  # Medium damage dla mage
        assert "staff" in weapon.get_name().lower()

    def test_mage_armor(self):
        """Test pancerza maga"""
        factory = MageEquipmentFactory()
        armor = factory.create_armor()

        assert isinstance(armor, Armor)
        assert armor.defense() >= 15  # Low defense dla mage
        assert any(word in armor.get_name().lower() for word in ["robe", "light", "cloth"])


class TestArcherEquipment:
    """Testy ekwipunku łucznika"""

    def test_archer_weapon(self):
        """Test broni łucznika"""
        factory = ArcherEquipmentFactory()
        weapon = factory.create_weapon()

        assert isinstance(weapon, Weapon)
        assert weapon.damage() >= 60  # Medium-high damage dla archer
        assert "bow" in weapon.get_name().lower()

    def test_archer_armor(self):
        """Test pancerza łucznika"""
        factory = ArcherEquipmentFactory()
        armor = factory.create_armor()

        assert isinstance(armor, Armor)
        assert armor.defense() >= 25  # Medium defense dla archer
        assert any(word in armor.get_name().lower() for word in ["leather", "medium", "light"])


class TestEquipmentConsistency:
    """Testy spójności ekwipunku - istota wzorca Abstract Factory"""

    def test_equipment_pairing(self):
        """
        Test czy fabryki tworzą spójne zestawy
        Istota wzorca: gwarancja spójności rodzin produktów
        """
        # Warrior - high defense, high damage
        warrior_factory = WarriorEquipmentFactory()
        warrior_weapon = warrior_factory.create_weapon()
        warrior_armor = warrior_factory.create_armor()

        # Mage - low defense, medium damage
        mage_factory = MageEquipmentFactory()
        mage_weapon = mage_factory.create_weapon()
        mage_armor = mage_factory.create_armor()

        # Archer - medium defense, medium-high damage
        archer_factory = ArcherEquipmentFactory()
        archer_weapon = archer_factory.create_weapon()
        archer_armor = archer_factory.create_armor()

        # Sprawdź logiczną spójność
        assert warrior_armor.defense() > archer_armor.defense() > mage_armor.defense()
        assert warrior_weapon.damage() > archer_weapon.damage() > mage_weapon.damage()

    def test_multiple_instances_different_objects(self):
        """Test czy każde wywołanie tworzy nowe obiekty"""
        factory = WarriorEquipmentFactory()

        weapon1 = factory.create_weapon()
        weapon2 = factory.create_weapon()

        armor1 = factory.create_armor()
        armor2 = factory.create_armor()

        # Powinny być różne instancje
        assert weapon1 is not weapon2
        assert armor1 is not armor2

    def test_factory_guarantees_consistency(self):
        """
        Test istoty wzorca: niemożliwe stworzenie niespójnego zestawu

        Bez wzorca można było: Sword + LightRobe (niespójne)
        Z wzorcem: fabryka gwarantuje że zawsze dostaniemy spójny zestaw
        """
        warrior_factory = WarriorEquipmentFactory()

        # Wywołujemy fabrykę 10 razy - zawsze spójny zestaw
        for _ in range(10):
            weapon = warrior_factory.create_weapon()
            armor = warrior_factory.create_armor()

            # Zawsze warrior weapon + warrior armor
            assert weapon.damage() >= 80
            assert armor.defense() >= 50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
