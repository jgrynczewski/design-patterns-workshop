# 📄 SRP - Report System

**Difficulty**: easy
**Time**: 10 minutes
**Focus**: Single Responsibility Principle

## 🎯 Zadanie
Zaimplementuj `ReportPrinter` - oddziel prezentację od danych.

## 📋 Wymagania
- [ ] `ReportPrinter.print_to_console(report)` - zwraca sformatowany string
- [ ] `ReportPrinter.save_to_file(report, filename)` - zapisuje do pliku
- [ ] Format: `"=== {title} ===\n{lines}"`

## 🚀 Jak zacząć
```bash
cd day0_principles/01_solid/01_srp

# Implementuj ReportPrinter w starter.py
# Uruchom testy
pytest test_srp.py -v
```

## 💡 SRP w pigułce

**Single Responsibility = jeden powód do zmiany**

❌ **Źle** (2 odpowiedzialności):
```python
class Report:
    def generate_content(self): ...
    def print_to_console(self): ...  # Inna odpowiedzialność!
    def save_to_file(self): ...      # Inna odpowiedzialność!
```
Powody do zmiany: (1) zmiana struktury danych, (2) zmiana formatu prezentacji

✅ **Dobrze** (1 odpowiedzialność każda):
```python
class Report:
    def get_title(self): ...  # TYLKO dane

class ReportPrinter:
    def print_to_console(self, report): ...  # TYLKO prezentacja
    def save_to_file(self, report, file): ...
```

**Korzyść**: Zmiana formatu prezentacji nie dotyka Report.

Sprawdź `solution_srp.py` po wykonaniu.
