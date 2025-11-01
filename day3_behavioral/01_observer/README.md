# 👀 Observer - Workflow Notifications

**Difficulty**: easy \
**Time**: 15 minutes \
**Focus**: Observer pattern - one-to-many dependency

## 🎯 Zadanie
Implementuj system powiadomień o zmianach statusu zadań w workflow używając wzorca Observer, gdzie wiele kanałów powiadomień reaguje na zmiany.

## 📋 Wymagania
- [ ] `Observer` interface z metodą `notify(task, old_status, new_status)`
- [ ] `WorkflowTask` (subject) z metodami `add_observer()`, `remove_observer()`, `set_status()`
- [ ] `EmailNotifier` - wysyła powiadomienia email
- [ ] `SlackNotifier` - wysyła do kanału Slack
- [ ] `SMSNotifier` - wysyła SMS do managerów
- [ ] `DashboardNotifier` - aktualizuje dashboard
- [ ] Automatyczne powiadomienia przy zmianie statusu

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj Observer interface i concrete observers
4. Zaimplementuj WorkflowTask z notification system
5. Uruchom testy: `python -m pytest test_observer.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- WorkflowTask przechowuje listę observers
- Przy `set_status()` powiadom wszystkich observers
- Każdy observer implementuje swoją logikę powiadomień
- Użyj enum dla statusów: ASSIGNED, IN_PROGRESS, REVIEW, COMPLETED

## 📬 Use Cases
- **Project Management**: Powiadomienia o zmianach statusu
- **E-commerce**: Tracking zamówień (ordered → shipped → delivered)
- **CI/CD**: Build notifications (started → success → deployed)

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Twardo zakodowane powiadomienia ❌
def update_task_status(task, new_status):
  task.status = new_status

  # Każda zmiana = modyfikacja kodu ❌
  send_email(task.assignee, f"Task {task.id} is now {new_status}")
  post_to_slack(f"#project", f"Task {task.id} status: {new_status}")
  send_sms(task.manager, f"Task update: {new_status}")
  update_dashboard(task.id, new_status)

  # Dodanie nowego kanału = modyfikacja funkcji ❌
```

### ✅ Z wzorcem:

```python
# Dynamiczne powiadomienia ✅
task = WorkflowTask("Fix bug", "ASSIGNED")
task.add_observer(EmailNotifier(user_email))
task.add_observer(SlackNotifier("#dev-team"))
task.add_observer(DashboardNotifier())

task.set_status("IN_PROGRESS")  # Wszyscy observers są powiadomieni! ✅
# Nowy kanał = nowy observer (zero zmian w WorkflowTask) ✅
```

Korzyść: Loose coupling między subject a observers
