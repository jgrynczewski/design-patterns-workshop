# 🔗 Chain of Responsibility - Approval Chain

**Difficulty**: medium \
**Time**: 15 minutes \
**Focus**: Chain of Responsibility pattern - passing requests through handler chain

## 🎯 Zadanie
Implementuj wzorzec Chain of Responsibility do systemu akceptacji wydatków w workflow, gdzie różni aprovers mają różne limity autoryzacji.

## 📋 Wymagania
- [ ] `ApprovalHandler` abstract class z metodą `handle_request()`
- [ ] `TeamLeadApprover` - zatwierdza do 1000 PLN
- [ ] `ManagerApprover` - zatwierdza do 5000 PLN
- [ ] `DirectorApprover` - zatwierdza do 25000 PLN
- [ ] `CEOApprover` - zatwierdza wszystko
- [ ] `ExpenseRequest` z kwotą, opisem i priorytetem
- [ ] Automatyczne przekazywanie w górę łańcucha gdy limit przekroczony
- [ ] Logowanie decyzji każdego handler'a

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj ApprovalHandler abstract class
4. Zaimplementuj concrete handlers z różnymi limitami
5. Uruchom testy: `python -m pytest test_chain_of_responsibility.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Każdy handler sprawdza czy może obsłużyć request
- Jeśli nie może - przekazuje do następnego w łańcuchu
- Łańcuch kończy się gdy handler obsłuży request lub zabraknie handlers
- Użyj enum dla statusów zatwierdzenia

## ⚡ Use Cases
- **Expense Approval**: Różne poziomy autoryzacji wydatków
- **Document Review**: Różne poziomy przeglądu dokumentów
- **Support Tickets**: Eskalacja problemów do wyższych poziomów
- **Security Clearance**: Różne poziomy dostępu do danych

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Skomplikowana logika if/else ❌
def approve_expense(amount, request_type):
    if amount <= 1000:
        return team_lead_approve(amount, request_type)
    elif amount <= 5000:
        if team_lead_available():
            result = team_lead_approve(amount, request_type)
            if not result: return manager_approve(amount, request_type) ❌
        else:
            return manager_approve(amount, request_type)
    elif amount <= 25000:
        # Jeszcze więcej zagnieżdżonych warunków ❌
        return complex_approval_logic(amount, request_type)
    # Dodanie nowego poziomu = przepisanie całej funkcji ❌
```

### ✅ Z wzorcem:

```python
# Elastyczny łańcuch handlers ✅
team_lead = TeamLeadApprover()
manager = ManagerApprover()
director = DirectorApprover()
ceo = CEOApprover()

# Budowanie łańcucha
team_lead.set_next(manager).set_next(director).set_next(ceo)

# Prosty request processing ✅
expense1 = ExpenseRequest(800, "Team lunch", Priority.LOW)
expense2 = ExpenseRequest(15000, "New server", Priority.HIGH)

result1 = team_lead.handle_request(expense1)  # Team lead approves
result2 = team_lead.handle_request(expense2)  # Goes to director
# Nowy poziom = nowa klasa (zero zmian w istniejącym kodzie) ✅
```

Korzyść: Elastyczny łańcuch przetwarzania bez skomplikowanych warunków
