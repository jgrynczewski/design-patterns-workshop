# 💾 Memento - Workflow Snapshots

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Memento pattern - capturing and restoring object state

## 🎯 Zadanie
Implementuj wzorzec Memento do systemu snapshots workflow, gdzie możesz zapisywać i przywracać stany dokumentów oraz całych projektów w różnych momentach czasu.

## 📋 Wymagania
- [ ] `DocumentMemento` - snapshot stanu pojedynczego dokumentu
- [ ] `ProjectMemento` - snapshot stanu całego projektu
- [ ] `DocumentOriginator` - zarządza stanem dokumentu i tworzy mementos
- [ ] `ProjectOriginator` - zarządza stanem projektu
- [ ] `WorkflowCaretaker` - przechowuje i zarządza historią snapshots
- [ ] Automatyczne snapshots przy ważnych operacjach
- [ ] Named snapshots z opisami i tagami
- [ ] Rollback do określonych punktów w czasie

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj Memento classes dla różnych obiektów
4. Zaimplementuj Originator classes z save/restore
5. Uruchom testy: `python -m pytest test_memento.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Memento przechowuje immutable snapshot stanu
- Originator tworzy mementos i może przywrócić stan z memento
- Caretaker zarządza kolekcją mementos (nie zna ich zawartości)
- Użyj timestamp i metadata dla każdego snapshot

## ⚡ Use Cases
- **Version Control**: Git commits i rollback do poprzednich wersji
- **Game States**: Save/load gry w różnych punktach
- **Document Editing**: Undo/redo z historią zmian
- **Database Backups**: Snapshots bazy danych przed krytycznymi operacjami

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Ręczne kopiowanie stanu ❌
class Document:
    def save_state(self):
        # Trzeba pamiętać o kopiowaniu każdego pola ❌
        return {
            'title': self.title,
            'content': self.content,
            'metadata': self.metadata.copy(),  # Easy to forget .copy()
            'version': self.version
            # Dodanie nowego pola = trzeba pamiętać o update ❌
        }
    
    def restore_state(self, state):
        # Trzeba ręcznie przypisać każde pole ❌
        self.title = state['title']
        self.content = state['content']
        # Łatwo zapomnieć o niektórych polach ❌
```

### ✅ Z wzorcem:

```python
# Enkapsulowane snapshots ✅
caretaker = WorkflowCaretaker()
document = DocumentOriginator("Project Plan")

# Automatyczne snapshots
document.edit("Initial draft")
caretaker.save_snapshot(document, "Initial version")

document.edit("Added requirements section")
caretaker.save_snapshot(document, "Requirements added")

document.edit("Corrupted data...")  # Oops!

# Łatwy rollback ✅
caretaker.restore_snapshot(document, "Requirements added")
print(document.content)  # "Added requirements section"

# Named snapshots z metadata ✅
caretaker.create_milestone(document, "Final Review", ["review", "final"])
# Bezpieczne przywracanie bez knowledge memento internals ✅
```

Korzyść: Bezpieczne snapshots bez narażania wewnętrznej struktury
