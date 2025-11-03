# Static vs Runtime

## Definicja
**Static** = określone **przed uruchomieniem** programu
**Runtime** = określone **podczas działania** programu

## 🎯 Prosty test
**Pytanie:** "Czy to wiadomo przed uruchomieniem?"

**✅ STATIC (compile time):**
- "Klasa User ma metodę get_name()"
- "Metoda przyjmuje 2 parametry"  
- "Import modułu json"

**❌ RUNTIME (execution time):**
- "Użytkownik wprowadził email 'test@gmail.com'"
- "Plik istnieje na dysku"
- "API zwróciło błąd 500"

## Konteksty w kodzie
**Static binding** - wiadomo która metoda zostanie wywołana  
**Dynamic binding** - zależy od typu obiektu w runtime

**Static typing** - `def process(user: User)` (typ wiadomy)  
**Dynamic typing** - `def process(data)` (typ w runtime)

## Dlaczego ważne?
- **Static** = łatwiejsze debugowanie, lepsze IDE support
- **Runtime** = większa elastyczność, polimorfizm
- **Design patterns** często wykorzystują runtime decisions

**Sprawdź przykłady:** `static_example.py` vs `runtime_example.py`
