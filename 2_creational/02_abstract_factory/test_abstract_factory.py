"""
Testy dla Abstract Factory Pattern - RPG Equipment
"""

import pytest
from starter import (
    get_equipment_factory,
    EquipmentFactory,
    Weapon,
    Armor,
    WarriorEquipmentFactory,
    MageEquipmentFactory,
    ArcherEquipmentFactory
)


class TestAbstractFactory:
    """Testy wzorca Abstract Factory"""

    def test_warrior_factory_creation(self):
        """Test tworzenia fabryki wojownika"""
        factory = get_equipment_factory("warrior")
        assert isinstance(factory, WarriorEquipmentFactory)
        assert isinstance(factory, EquipmentFactory)

    def test_mage_factory_creation(self):
        """Test tworzenia fabryki maga"""
        factory = get_equipment_factory("mage")
        assert isinstance(factory, MageEquipmentFactory)
        assert isinstance(factory, EquipmentFactory)

    def test_archer_factory_creation(self):
        """Test tworzenia fabryki łucznika"""
        factory = get_equipment_factory("archer")
        assert isinstance(factory, ArcherEquipmentFactory)
        assert isinstance(factory, EquipmentFactory)

    def test_invalid_character_class(self):
        """Test błędnej klasy postaci"""
        with pytest.raises(ValueError):
            get_equipment_factory("invalid_class")

    def test_case_insensitive_factory_creation(self):
        """Test czy factory działa z różnymi wielkościami liter"""
        factory1 = get_equipment_factory("warrior")
        factory2 = get_equipment_factory("WARRIOR")
        factory3 = get_equipment_factory("Warrior")

        assert type(factory1) == type(factory2) == type(factory3)


class TestWarriorEquipment:
    """Testy ekwipunku wojownika"""

    def test_warrior_weapon(self):
        """Test broni wojownika"""
        factory = get_equipment_factory("warrior")
        weapon = factory.create_weapon()

        assert isinstance(weapon, Weapon)
        assert weapon.damage() >= 80  # High damage dla warrior
        assert "sword" in weapon.get_name().lower()

    def test_warrior_armor(self):
        """Test pancerza wojownika"""
        factory = get_equipment_factory("warrior")
        armor = factory.create_armor()

        assert isinstance(armor, Armor)
        assert armor.defense() >= 50  # High defense dla warrior
        assert any(word in armor.get_name().lower() for word in ["heavy", "plate", "mail"])


class TestMageEquipment:
    """Testy ekwipunku maga"""

    def test_mage_weapon(self):
        """Test broni maga"""
        factory = get_equipment_factory("mage")
        weapon = factory.create_weapon()

        assert isinstance(weapon, Weapon)
        assert weapon.damage() >= 40  # Medium damage dla mage
        assert "staff" in weapon.get_name().lower()

    def test_mage_armor(self):
        """Test pancerza maga"""
        factory = get_equipment_factory("mage")
        armor = factory.create_armor()

        assert isinstance(armor, Armor)
        assert armor.defense() >= 15  # Low defense dla mage
        assert any(word in armor.get_name().lower() for word in ["robe", "light", "cloth"])


class TestArcherEquipment:
    """Testy ekwipunku łucznika"""

    def test_archer_weapon(self):
        """Test broni łucznika"""
        factory = get_equipment_factory("archer")
        weapon = factory.create_weapon()

        assert isinstance(weapon, Weapon)
        assert weapon.damage() >= 60  # Medium-high damage dla archer
        assert "bow" in weapon.get_name().lower()

    def test_archer_armor(self):
        """Test pancerza łucznika"""
        factory = get_equipment_factory("archer")
        armor = factory.create_armor()

        assert isinstance(armor, Armor)
        assert armor.defense() >= 25  # Medium defense dla archer
        assert any(word in armor.get_name().lower() for word in ["leather", "medium", "light"])


class TestEquipmentConsistency:
    """Testy spójności ekwipunku"""

    def test_equipment_pairing(self):
        """Test czy fabryki tworzą spójne zestawy"""
        # Warrior - high defense, high damage
        warrior_factory = get_equipment_factory("warrior")
        warrior_weapon = warrior_factory.create_weapon()
        warrior_armor = warrior_factory.create_armor()

        # Mage - low defense, medium damage
        mage_factory = get_equipment_factory("mage")
        mage_weapon = mage_factory.create_weapon()
        mage_armor = mage_factory.create_armor()

        # Archer - medium defense, medium-high damage
        archer_factory = get_equipment_factory("archer")
        archer_weapon = archer_factory.create_weapon()
        archer_armor = archer_factory.create_armor()

        # Sprawdź logiczną spójność
        assert warrior_armor.defense() > archer_armor.defense() > mage_armor.defense()
        assert warrior_weapon.damage() > archer_weapon.damage() > mage_weapon.damage()

    def test_multiple_instances_different_objects(self):
        """Test czy każde wywołanie tworzy nowe obiekty"""
        factory = get_equipment_factory("warrior")

        weapon1 = factory.create_weapon()
        weapon2 = factory.create_weapon()

        armor1 = factory.create_armor()
        armor2 = factory.create_armor()

        # Powinny być różne instancje
        assert weapon1 is not weapon2
        assert armor1 is not armor2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
