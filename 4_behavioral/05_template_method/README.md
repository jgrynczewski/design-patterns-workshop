# 📄 Template Method - Document Generation

**Poziom**: Łatwy  
**Cel**: Template Method - szkielet algorytmu z customizowalnymi krokami

## 🎯 Zadanie
Zaimplementuj wzorzec Template Method dla generatorów dokumentów. Template method definiuje szkielet procesu (header → body → signature → footer), a subklasy implementują konkretne kroki.

## ✅ Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `DocumentGenerator` z template method `generate_document()`
- [ ] 3 metody abstrakcyjne: `create_header()`, `create_body()`, `create_footer()`
- [ ] 1 hook method: `add_signature()` (opcjonalny, domyślnie pusty)
- [ ] `ReportDocument` - implementuje primitive operations
- [ ] `EmailDocument` - implementuje primitive operations + nadpisuje hook

## 🚀 Jak zacząć
1. Przejrzyj `problem.py` - zobacz duplikację szkieletu
   ```bash
   python problem.py
   ```
2. Otwórz `starter.py`
3. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest tests.py -v`
4. Klasa `DocumentGenerator` jest częściowo gotowa
5. Zaimplementuj:
   - `generate_document()` - template method (szkielet algorytmu)
   - `ReportDocument` - konkretny generator
   - `EmailDocument` - konkretny generator z nadpisanym hookiem
6. Uruchom testy ponownie (teraz powinny przejść)

## 💡 Podpowiedzi
- **Template method**: Metoda w base class definiująca szkielet (NIE abstract)
- **Primitive operations**: Metody abstrakcyjne - MUSZĄ być zaimplementowane
- **Hook methods**: Metody z domyślną implementacją - MOGĄ być nadpisane
- **Subklasy**: Implementują tylko konkretne kroki, NIE nadpisują template method

## 📝 Przykład użycia
```python
# Stwórz generatory
report = ReportDocument("Q4 Sales Report")
email = EmailDocument("Meeting Reminder")

# Użyj template method - ten sam szkielet dla obu
doc1 = report.generate_document()  # header → body → (brak signature) → footer
doc2 = email.generate_document()   # header → body → signature → footer
```

## 📊 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Duplikacja szkieletu w każdej klasie
class ReportDocument:
    def generate_document(self):
        # Szkielet algorytmu skopiowany ❌
        result = self.create_header()
        result += self.create_body()
        result += self.add_signature()  # Duplikacja!
        result += self.create_footer()
        return result

class EmailDocument:
    def generate_document(self):
        # Ten sam szkielet, ale skopiowany ❌
        result = self.create_header()    # Duplikacja!
        result += self.create_body()
        result += self.add_signature()
        result += self.create_footer()
        return result
```

### ✅ Z wzorcem (Template Method):
```python
# Szkielet w base class - DRY ✅
class DocumentGenerator(ABC):
    def generate_document(self):  # Template method
        result = self.create_header()    # Wywołuje abstract
        result += self.create_body()     # Wywołuje abstract
        result += self.add_signature()   # Wywołuje hook
        result += self.create_footer()   # Wywołuje abstract
        return result

# Subklasy tylko implementują kroki ✅
class ReportDocument(DocumentGenerator):
    def create_header(self): return "REPORT HEADER"
    def create_body(self): return "Report content"
    def create_footer(self): return "End of Report"
    # add_signature() - używa domyślnej (pusty)

class EmailDocument(DocumentGenerator):
    def create_header(self): return "EMAIL HEADER"
    def create_body(self): return "Email content"
    def create_footer(self): return "Automated email"
    def add_signature(self): return "Best regards"  # Nadpisuje hook
```

**Korzyść**: Szkielet w jednym miejscu, łatwa modyfikacja, gwarancja spójności.

## 🎯 Use Cases
- **Report Generation**: Różne raporty (PDF, HTML, TXT) z tym samym flow
- **Data Processing**: ETL pipelines - extract → transform → load
- **Testing Frameworks**: setUp → test → tearDown
- **Cooking Recipes**: gather → prepare → cook → serve
