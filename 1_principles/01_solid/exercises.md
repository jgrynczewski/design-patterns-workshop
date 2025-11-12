# SOLID Principles - Ćwiczenia

## 🎯 Cel
Rozpoznawanie naruszeń zasad SOLID i proponowanie poprawek.

## 📋 Zadanie 1: Code Review (10 min)

Przejrzyj kod w folderach violation/ i solution/ dla każdej zasady:

1. **SRP**: `srp/violation.py` → `srp/solution.py`
- Ile odpowiedzialności ma klasa User?
- Jak podział wpływa na testowanie?

2. **OCP**: `ocp/violation.py` → `ocp/solution.py`
- Co musisz zmienić, żeby dodać nowy typ rabatu?
- Jak Strategy Desing Pattern rozwiązuje problem?

3. **LSP**: `lsp/violation.py` → `lsp/solution.py`
- Dlaczego Penguin łamie kontrakt Bird?
- Jak nowa hierarchia rozwiązuje problem?

4. **ISP**: `isp/violation.py` → `isp/solution.py`
- Ile metod musi implementować SimplePrinter?
- Jak małe interfejsy pomagają?

5. **DIP**: `dip/violation.py` → `dip/solution.py`
- Od czego zależy NotificationService?
- Jak abstrakcja rozwiązuje problem?

## 🔨 Zadanie 2: Refactoring Challenge (15 min)

Znajdź naruszenia SOLID w tym kodzie:

```python
class UserManager:
    def __init__(self):
        self.db_connection = MySQLConnection()
        self.email_client = SMTPClient()
    
    def create_user(self, user_type, name, email):
        # Validation
        if "@" not in email:
            raise ValueError("Invalid email")
        
        # Create user based on type
        if user_type == "admin":
            user = AdminUser(name, email)
        elif user_type == "regular":
            user = RegularUser(name, email)
        else:
            raise ValueError("Unknown user type")
        
        # Save to database
        self.db_connection.execute(
            f"INSERT INTO users VALUES ('{name}', '{email}')"
        )
        
        # Send email
        self.email_client.send(
            email,
            "Welcome!",
            "Thanks for joining!"
        )
        
        return user
```

Pytania:
- Które zasady SOLID są złamane?
- Jak byś refaktorował ten kod?
- Narysuj nową strukturę klas

✅ Sprawdź rozwiązania

Po wykonaniu zadań sprawdź kod w solution/ folderach i porównaj z własnymi pomysłami.

🚀 Następne kroki

Po opanowaniu SOLID przejdź do ../02_grasp/ dla wzorców projektowych GRASP.
