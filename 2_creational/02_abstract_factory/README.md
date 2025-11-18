# 🏭 Abstract Factory - Equipment Systems RPG

**Difficulty**: średni  
**Time**: 15 minutes  
**Focus**: Abstract Factory pattern + product families

## 🎯 Zadanie
Implementuj wzorzec Abstract Factory do tworzenia spójnych zestawów ekwipunku dla różnych klas bohaterów w grze RPG.

## 📋 Wymagania
- [ ] `EquipmentFactory` jako abstract factory interface
- [ ] `WarriorEquipmentFactory` tworzy heavy armor + melee weapons
- [ ] `MageEquipmentFactory` tworzy light armor + magic weapons
- [ ] `ArcherEquipmentFactory` tworzy medium armor + ranged weapons
- [ ] Każda fabryka produkuje spójny zestaw (weapon + armor)
- [ ] `get_equipment_factory()` helper function

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Sprawdź `# %% Hints` section dla technical tips
3. Uruchom doctests: `python -m doctest starter.py -v`
4. Zaimplementuj abstract factory interface
5. Zaimplementuj concrete factories
6. Uruchom testy: `python -m pytest test_abstract_factory.py -v`
7. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź (Conceptual)
- **Abstract Factory** tworzy **families** of related objects
- Warrior factory = spójny zestaw dla tanków (wysokie damage + obrona)
- Mage factory = spójny zestaw dla casterów (średnie damage + niska obrona)
- Archer factory = spójny zestaw dla ranged (średnie-wysokie damage + średnia obrona)
- Każda fabryka gwarantuje compatibility między produktami

## 🎮 Product Families
- **Warrior**: Heavy Armor + Sword (tank build)
- **Mage**: Light Robe + Staff (caster build)
- **Archer**: Leather Armor + Bow (ranged build)

## 2. Abstract Factory

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Niespójne zestawy, łatwo o błędy
weapon = create_weapon("sword")      # Heavy weapon
armor = create_armor("light_robe")   # Light armor - nie pasuje! ❌
shield = create_shield("magic")      # Magic shield - chaos!
```

✅ Z wzorcem:
```python
# Spójne familie produktów
factory = get_equipment_factory("warrior")
weapon = factory.create_weapon()  # Heavy sword ✅
armor = factory.create_armor()    # Heavy armor ✅  
# Wszystko pasuje do siebie automatycznie!
```

Korzyść: Gwarantuje spójność między powiązanymi obiektami
