# 👥 Mediator - Team Collaboration

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Mediator pattern - centralized communication between objects

## 🎯 Zadanie
Implementuj wzorzec Mediator do systemu komunikacji zespołu w workflow, gdzie różni członkowie zespołu komunikują się przez centralny mediator zamiast bezpośrednio ze sobą.

## 📋 Wymagania
- [ ] `TeamMediator` interface z metodami komunikacyjnymi
- [ ] `WorkflowMediator` - konkretny mediator zarządzający komunikacją
- [ ] `TeamMember` abstract class dla członków zespołu
- [ ] `Developer`, `Designer`, `ProjectManager`, `Tester` - różne role
- [ ] Różne typy wiadomości: task assignment, status update, question, announcement
- [ ] Filtering wiadomości na podstawie roli i typu
- [ ] Historia komunikacji i notyfikacje

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj TeamMediator interface i WorkflowMediator
4. Zaimplementuj TeamMember abstract class i concrete members
5. Uruchom testy: `python -m pytest test_mediator.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Mediator zarządza wszystką komunikacją między team members
- Team members znają tylko mediator, nie inne members
- Mediator może filtrować, routować i logować wiadomości
- Użyj enum dla typów wiadomości i ról

## ⚡ Use Cases
- **Chat Systems**: Centralna obsługa wiadomości w zespole
- **Air Traffic Control**: Koordynacja komunikacji między samolotami
- **UI Components**: Komunikacja między komponentami przez controller
- **Workflow Systems**: Koordynacja zadań między różnymi rolami

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Bezpośrednia komunikacja wszystkich ze wszystkimi ❌
class Developer:
    def notify_task_complete(self):
        self.project_manager.task_completed(self.current_task) ❌
        self.tester.ready_for_testing(self.current_task) ❌
        self.designer.update_status(self.current_task) ❌
        # Każda zmiana wymaga aktualizacji wszystkich związków ❌

class Designer:
    def send_mockup(self):
        self.developer.new_mockup_available() ❌
        self.project_manager.design_ready() ❌
        # Tight coupling między wszystkimi klasami ❌
```

### ✅ Z wzorcem:

```python
# Centralna komunikacja przez mediator ✅
mediator = WorkflowMediator()

developer = Developer("John", mediator)
designer = Designer("Alice", mediator)
tester = Tester("Bob", mediator)
pm = ProjectManager("Sarah", mediator)

# Rejestracja w mediator
mediator.add_team_member(developer)
mediator.add_team_member(designer)

# Komunikacja przez mediator ✅
developer.send_message("Task completed: Login feature", MessageType.STATUS_UPDATE)
# Mediator automatycznie powiadomi odpowiednie osoby ✅

designer.send_message("New mockups ready", MessageType.ANNOUNCEMENT)
# Mediator filtruje i routuje wiadomości ✅
# Loose coupling - łatwe dodawanie nowych ról ✅
```

Korzyść: Centralna kontrola komunikacji bez bezpośrednich zależności
