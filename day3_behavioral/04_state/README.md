# 🔄 State - Workflow States

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: State pattern - object behavior changes with internal state

## 🎯 Zadanie
Implementuj wzorzec State do zarządzania stanami dokumentów w workflow, gdzie dokument zmienia swoje zachowanie w zależności od aktualnego stanu.

## 📋 Wymagania
- [ ] `DocumentState` interface z metodami dla różnych akcji
- [ ] `DraftState` - stan projektu (można edytować, zapisać)
- [ ] `ReviewState` - stan przeglądu (można zatwierdzić, odrzucić)
- [ ] `ApprovedState` - stan zatwierdzony (można opublikować)
- [ ] `PublishedState` - stan opublikowany (tylko do odczytu)
- [ ] `DocumentContext` z automatycznymi przejściami między stanami
- [ ] Walidacja dozwolonych przejść między stanami

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj DocumentState interface i concrete states
4. Zaimplementuj DocumentContext z zarządzaniem stanami
5. Uruchom testy: `python -m pytest test_state.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Każdy stan definiuje dozwolone akcje w tym stanie
- Context deleguje akcje do aktualnego stanu
- Stan może zmieniać context na inny stan
- Użyj enum dla typów stanów

## ⚡ Use Cases
- **Document Workflow**: Draft → Review → Approved → Published
- **Order Processing**: Pending → Processing → Shipped → Delivered
- **Game States**: Menu → Playing → Paused → GameOver
- **Connection States**: Disconnected → Connecting → Connected

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Jeden wielki if/else w klasie ❌
class Document:
def edit(self, content):
    if self.status == "draft":
        self.content = content  # OK
    elif self.status == "review":
        raise Exception("Cannot edit in review") ❌
    elif self.status == "published":
        raise Exception("Cannot edit published") ❌
    # Dodanie nowego stanu = modyfikacja każdej metody ❌

def approve(self):
    if self.status == "draft":
        raise Exception("Must be in review") ❌
    elif self.status == "review":
        self.status = "approved"  # OK
    # Powtarzanie logiki w każdej metodzie ❌
```

### ✅ Z wzorcem:

```python
# Enkapsulowana logika stanów ✅
document = DocumentContext("My Document")
document.edit("Initial content")    # DraftState allows editing
document.submit_for_review()        # Transition to ReviewState

document.edit("More content")       # ReviewState blocks editing
# Raises: OperationNotAllowedError ✅

document.approve()                  # Transition to ApprovedState
document.publish()                  # Transition to PublishedState
# Clean state transitions with validation ✅
```

Korzyść: Czyste przejścia stanów bez skomplikowanych warunków
