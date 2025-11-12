# 📄 Template Method - Document Templates

**Difficulty**: easy \
**Time**: 15 minutes \
**Focus**: Template Method pattern - algorithm skeleton with customizable steps

## 🎯 Zadanie
Implementuj wzorzec Template Method do generowania różnych typów dokumentów w workflow, gdzie szkielet procesu jest stały, ale szczegóły implementacji różnią się między typami
dokumentów.

## 📋 Wymagania
- [ ] `DocumentGenerator` abstract class z template method `generate_document()`
- [ ] `ProjectReportGenerator` - generator raportów projektowych
- [ ] `MeetingNotesGenerator` - generator notatek ze spotkań
- [ ] `TechnicalSpecGenerator` - generator specyfikacji technicznych
- [ ] Wspólny szkielet: header → content → validation → footer
- [ ] Hooks (opcjonalne kroki) dla dodatkowej customizacji
- [ ] Różne formaty wyjściowe (text, markdown, html)

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom doctests: `python -m doctest starter.py -v`
3. Zaimplementuj DocumentGenerator abstract class z template method
4. Zaimplementuj concrete generators z własnymi krokami
5. Uruchom testy: `python -m pytest test_template_method.py -v`
6. Commit gdy wszystkie testy przechodzą ✅

## 💡 Podpowiedź
- Template method definiuje szkielet algorytmu w base class
- Abstract methods to primitive operations (muszą być zaimplementowane)
- Hook methods to opcjonalne rozszerzenia (domyślnie puste)
- Concrete classes implementują tylko specyficzne kroki

## ⚡ Use Cases
- **Report Generation**: Różne typy raportów z tym samym formatem
- **Data Processing**: ETL pipelines z różnymi źródłami
- **Testing Frameworks**: Test lifecycle z różnymi implementacjami
- **Build Systems**: Kompilacja z różnymi krokami dla różnych języków

## 🔄 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Duplikacja kodu w każdym generatorze ❌
class ProjectReportGenerator:
def generate(self):
    # Wspólny kod kopiowany wszędzie ❌
    header = self.create_header()
    content = self.create_content()
    validation = self.validate_content(content)
    footer = self.create_footer()
    return self.format_document(header, content, footer)

class MeetingNotesGenerator:
    def generate(self):
        # Ten sam szkielet, ale nieco inny ❌
        header = self.create_header()  # Duplikacja!
        content = self.create_content()
        validation = self.validate_content(content)
        footer = self.create_footer()
        return self.format_document(header, content, footer)
```

### ✅ Z wzorcem:

```python
# Wspólny szkielet w base class ✅
class DocumentGenerator:
    def generate_document(self):  # Template method
        header = self.create_header()
        content = self.create_content()      # Abstract
        self.validate_content(content)       # Hook
        footer = self.create_footer()        # Abstract
        return self.format_output(header, content, footer)

# Tylko specyficzne kroki w subclass ✅
report_gen = ProjectReportGenerator("Q4 Results")
meeting_gen = MeetingNotesGenerator("Daily Standup")

report = report_gen.generate_document()    # Używa template method
notes = meeting_gen.generate_document()    # Ten sam szkielet, inna implementacja
```

Korzyść: Eliminacja duplikacji kodu przy zachowaniu elastyczności
