# Business Logic - Czym jest logika biznesowa?

## Definicja
**Business Logic** = zasady, które istniałyby bez komputera
**Technical Logic** = jak komputer implementuje te zasady

## 🎯 Prosty test
**Pytanie:** "Czy ta zasada istniałaby bez komputera?"

**✅ BUSINESS LOGIC:**
- "Klient premium ma 20% zniżki"
- "Hasło musi mieć minimum 8 znaków"
- "Można zwrócić produkt w ciągu 30 dni"

**❌ TECHNICAL LOGIC:**
- "Zapisz do PostgreSQL"
- "Hashuj hasło SHA-256"
- "Serializuj do JSON"

## Dlaczego to ważne?
- **Separation of Concerns** - biznes oddzielony od techniki
- **Testowalność** — business rules bez infrastruktury
- **Zrozumiałość** — działowiec może zweryfikować kod

## W architekturze
- **Domain Layer** = business logic
- **Infrastructure Layer** = technical logic
- **Presentation Layer** = jak pokazać użytkownikowi

**Sprawdź przykłady:** `violation.py` vs `solution.py`
