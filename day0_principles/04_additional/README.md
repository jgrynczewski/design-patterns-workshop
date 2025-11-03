# Additional Programming Principles

## Przegląd dodatkowych zasad

Te 5 praktycznych zasad uzupełniają SOLID i GRASP. Skupiają się na **jasności kodu** i **dobrych praktykach**.

## 1. Business Logic - Czym jest logika biznesowa?
**Definicja:** Rozróżnienie między zasadami biznesowymi a szczegółami technicznymi.

**Kluczowe pytanie:** "Czy ta zasada istniałaby bez komputera?"

**Sprawdź:** `01_business_logic/`

## 2. Tell, Don't Ask
**Definicja:** Mów obiektom co mają robić, zamiast pytać o ich stan.

**Dlaczego:** Obiekt sam zarządza swoim stanem i zachowaniem.

**Sprawdź:** `02_tell_dont_ask/`

## 3. Law of Demeter
**Definicja:** Obiekt powinien rozmawiać tylko ze swoimi "przyjaciółmi".

**Zasada:** Nie więcej niż jedna kropka: `object.method()` ✅, `object.field.method()` ❌

**Sprawdź:** `03_law_of_demeter/`

## 4. Composition over Inheritance
**Definicja:** Buduj zachowanie przez składanie obiektów, nie dziedziczenie.

**Dlaczego:** Elastyczność > sztywna hierarchia klas.

**Sprawdź:** `04_composition_over_inheritance/`

## 5. Dependency Injection
**Definicja:** Przekazuj zależności z zewnątrz, zamiast tworzyć je wewnątrz.

**Dlaczego:** Testowanie, flexibility, loose coupling.

**Sprawdź:** `05_dependency_injection/`

## 🎯 Workflow

**Recommended approach:**
1. **Business Logic** (10 min) - fundamenty myślenia o kodzie
2. **Tell Don't Ask** (10 min) - OOP mindset
3. **Law of Demeter** (10 min) - clean interfaces
4. **Composition over Inheritance** (15 min) - design choices
5. **Dependency Injection** (15 min) - advanced techniques

**Total: 60 minutes**

## 🔗 Powiązania z poprzednimi zasadami

- **Business Logic** → fundament dla SOLID SRP
- **Tell Don't Ask** → GRASP Information Expert
- **Law of Demeter** → SOLID Interface Segregation
- **Composition** → SOLID Open/Closed Principle
- **Dependency Injection** → SOLID Dependency Inversion

Te zasady **wzmacniają** fundamenty z SOLID i GRASP.

Kluczowe elementy:
- ✅ Bardzo krótkie definicje - 1 zdanie max
- ✅ Praktyczne pytania - "Czy istniałaby bez komputera?"
- ✅ Konkretne przykłady — jedna kropka vs dwie
- ✅ Jasne powiązania — jak łączy się z SOLID/GRASP
- ✅ Realny timing - 60 min total
