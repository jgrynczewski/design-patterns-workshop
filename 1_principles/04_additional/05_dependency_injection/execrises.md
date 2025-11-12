# Dependency Injection - Ćwiczenia

## 🎯 Cel
Nauka rozpoznawania hard dependencies i refaktoryzacji do Dependency Injection.

## 📋 Zadanie 1: Znajdź hard dependencies (5 min)

**W `violation_basic.py` znajdź:**
1. Gdzie tworzą się zależności wewnątrz klasy?
2. Dlaczego nie można testować tej klasy w izolacji?
3. Co się stanie jak zmienisz bazę z PostgreSQL na MySQL?

**W `solution_basic.py` zobacz:**
4. Jak zależności są przekazywane?
5. Jak łatwo zmienić implementację?

## 🔨 Zadanie 2: Refaktoryzacja (10 min)

**Przerefaktoryzuj z hard dependencies na DI:**

```python
class ReportGenerator:
    def __init__(self):
        # Hard dependencies
        self.db = MySQLConnection("localhost", "reports_db")
        self.email = SMTPSender("smtp.company.com", 587)
        self.pdf = PDFGenerator("/tmp/reports")
    
    def generate_monthly_report(self, month):
        data = self.db.get_monthly_data(month)
        pdf_path = self.pdf.create_report(data)
        self.email.send_report("manager@company.com", pdf_path)
        return pdf_path

class MySQLConnection:
    def __init__(self, host, database):
        self.host = host
        self.database = database
    
    def get_monthly_data(self, month):
        return f"Data for {month}"

class SMTPSender:
    def __init__(self, server, port):
        self.server = server
        self.port = port

    def send_report(self, email, attachment):
        return f"Sent to {email}"

class PDFGenerator:
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def create_report(self, data):
        return f"{self.output_dir}/report.pdf"
```

Zadanie: Użyj constructor injection

💡 Zadanie 3: Typy injection (5 min)

Zidentyfikuj typ Dependency Injection:

```python
# A: Constructor Injection
class Service:
    def __init__(self, dependency):
        self.dependency = dependency

# B: Setter Injection  
class Service:
    def set_dependency(self, dependency):
        self.dependency = dependency

# C: Hard Dependency
class Service:
    def __init__(self):
        self.dependency = ConcreteImplementation()

# D: Method Injection
class Service:
    def process(self, dependency, data):
        return dependency.handle(data)
```

Odpowiedź: A-Constructor, B-Setter, C-Hard Dependency, D-Method Injection

🎯 Zadanie 4: Testing benefits (10 min)

Napisz test dla refaktoryzowanej klasy ReportGenerator:

# Jak testować hard dependencies? (trudne)
# Jak testować z DI? (łatwe z mockami)

```python
class MockDatabase:
    def get_monthly_data(self, month):
        return "test data"

class MockEmailSender:
    def send_report(self, email, attachment):
        return "email sent"

class MockPDFGenerator:
    def create_report(self, data):
        return "test.pdf"
```

# Zadanie: Napisz test używając mocków

🔧 Zadanie 5: DI Container (bonus - 10 min)

Zaprojektuj prosty DI container:

```python
class DIContainer:
    def __init__(self):
        self._services = {}
        self._factories = {}
    
    def register(self, interface, implementation):
        # Jak zarejestrować service?
        pass
    
    def get(self, interface):
        # Jak pobrać service?
        pass
```

# Zadanie: Zaimplementuj basic DI container

✅ Sprawdź rozwiązania

Porównaj swoje refaktoryzacje z solution.py
