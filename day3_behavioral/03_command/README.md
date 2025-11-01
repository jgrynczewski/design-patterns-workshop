# ⚡ Command - Undo/Redo Operations

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Command pattern - encapsulating requests as objects

## 🎯 Zadanie
Implementuj wzorzec Command do systemu undo/redo operacji na dokumentach w workflow używając wzorca Command, gdzie każda operacja jest enkapsulowana jako obiekt.

## 📋 Wymagania
- [ ] `Command` interface z metodami `execute()` i `undo()`
- [ ] `CreateDocumentCommand` - tworzenie nowego dokumentu
- [ ] `EditDocumentCommand` - edycja treści dokumentu
- [ ] `DeleteDocumentCommand` - usuwanie dokumentu
- [ ] `CommandInvoker` (DocumentManager) z historią komend
- [ ] Implementacja undo/redo z wykorzystaniem stosu komend
- [ ] Macro commands - grupowanie wielu operacji

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj Command interface i concrete commands
4. Zaimplementuj CommandInvoker z historią undo/redo
5. Uruchom testy: `python -m pytest test_command.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Każda komenda pamięta stan przed wykonaniem (dla undo)
- CommandInvoker przechowuje historię w stosie
- Undo cofa ostatnią komendę i przesuwa wskaźnik
- Redo ponownie wykonuje cofniętą komendę

## ⚡ Use Cases
- **Text Editors**: Undo/redo operacji edycji (VS Code, Word)
- **Database Transactions**: Rollback operacji
- **GUI Operations**: Cofanie akcji użytkownika
- **Game Actions**: Cofanie ruchów w grze

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Bezpośrednie wywołania bez możliwości cofnięcia ❌
class DocumentManager:
def create_document(self, title):
    doc = Document(title)
    self.documents.append(doc)
    # Brak możliwości undo ❌

def edit_document(self, doc_id, content):
    doc = self.find_document(doc_id)
    doc.content = content  # Stracona poprzednia treść ❌
    # Jak cofnąć tę operację? ❌
```

### ✅ Z wzorcem:

```python
# Enkapsulowane operacje z undo/redo ✅
manager = DocumentManager()
create_cmd = CreateDocumentCommand(manager, "Project Plan")
edit_cmd = EditDocumentCommand(manager, doc_id, "New content")

manager.execute_command(create_cmd)  # Dokument utworzony
manager.execute_command(edit_cmd)    # Dokument edytowany

manager.undo()  # Cofnij edycję ✅
manager.undo()  # Cofnij tworzenie ✅
manager.redo() # Ponów tworzenie ✅
```

Korzyść: Pełna kontrola nad historią operacji
