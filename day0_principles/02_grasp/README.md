# GRASP - General Responsibility Assignment Software Patterns

## Co to jest GRASP?

GRASP to zestaw 9 zasad, które pomagają **przypisywać odpowiedzialności** do klas w systemie obiektowym. W przeciwieństwie do SOLID (które mówią "jak" projektować), GRASP mówi
"**kto** powinien być odpowiedzialny za co".

## 1. Information Expert
**Definicja:** Przypisz odpowiedzialność klasie, która ma informacje potrzebne do jej realizacji.

**Dlaczego:** Klasa która ma dane powinna je też przetwarzać - to naturalne i minimalizuje coupling.

**Kiedy łamiesz:** Gdy klasa A przetwarza dane z klasy B, zamiast żeby B robiła to sama.

**Sprawdź w kodzie:** `01_information_expert/violation.py` linia 8-15

## 2. Creator
**Definicja:** Klasa A powinna tworzyć instancje klasy B, jeśli A zawiera, agreguje lub ściśle używa B.

**Dlaczego:** Twórca wie, kiedy i jak stworzyć obiekt. Redukuje dependencies.

**Kiedy łamiesz:** Gdy obiekty są tworzone przez klasy, które ich nie używają bezpośrednio.

**Sprawdź w kodzie:** `02_creator/violation.py` linia 6-12

## 3. Controller
**Definicja:** Przypisz odpowiedzialność za obsługę use case klasie, która reprezentuje system, subsystem lub scenariusz użycia.

**Dlaczego:** Separuje logikę biznesową od warstwy prezentacji. Centralizuje orchestrację.

**Kiedy łamiesz:** Gdy UI klasy bezpośrednio manipulują domain objects.

**Sprawdź w kodzie:** `03_controller/violation.py` linia 10-18

## 4. Low Coupling
**Definicja:** Minimalizuj zależności między klasami. Klasy powinny znać jak najmniej innych klas.

**Dlaczego:** Łatwiejsze zmiany, testing, reusability. Mniejsze ripple effects.

**Kiedy łamiesz:** Gdy klasa zna zbyt wiele konkretnych implementacji zamiast abstrakcji.

**Sprawdź w kodzie:** `04_low_coupling/violation.py` linia 12-19

## 5. High Cohesion
**Definicja:** Klasa powinna mieć spójną odpowiedzialność - wszystkie jej metody powinny współpracować w realizacji jednego celu.

**Dlaczego:** Łatwiejsza do zrozumienia, maintainability, reusability.

**Kiedy łamiesz:** Gdy klasa robi zbyt wiele niezależnych rzeczy.

**Sprawdź w kodzie:** `05_high_cohesion/violation.py` linia 8-17

## 6. Polymorphism
**Definicja:** Użyj polimorfizmu zamiast if/else czy switch statements do obsługi wariantów zachowania.

**Dlaczego:** Kod jest bardziej extensible. Dodanie nowych typów nie wymaga zmian w istniejącym kodzie.

**Kiedy łamiesz:** Gdy używasz type checking (isinstance, type) do różnych zachowań.

**Sprawdź w kodzie:** `06_polymorphism/violation.py` linia 9-16

## 7. Pure Fabrication
**Definicja:** Stwórz klasę, która nie reprezentuje rzeczywistej koncepcji domenowej, ale jest potrzebna ze względów technicznych.

**Dlaczego:** Pozwala zachować wysoką kohezję i niskie coupling w domain objects.

**Kiedy łamiesz:** Gdy domain objects mają techniczne odpowiedzialności (database, logging, etc.).

**Sprawdź w kodzie:** `07_pure_fabrication/violation.py` linia 10-17

## 8. Indirection
**Definicja:** Wprowadź pośredni obiekt między dwoma komponentami, aby zmniejszyć bezpośrednie coupling.

**Dlaczego:** Decoupling pozwala na niezależne zmiany. Łatwiejsze testing i swapping implementations.

**Kiedy łamiesz:** Gdy klasy bezpośrednio zależą od konkretnych implementacji zewnętrznych systemów.

**Sprawdź w kodzie:** `08_indirection/violation.py` linia 8-16

## 9. Protected Variations
**Definicja:** Zabezpiecz stabilne elementy systemu przed wpływem niestabilnych elementów przez stworzenie interface.

**Dlaczego:** System jest odporny na zmiany zewnętrzne. Łatwiejsze adaptowanie do nowych requirements.

**Kiedy łamiesz:** Gdy system bezpośrednio zależy od niestabilnych external APIs czy volatile requirements.

**Sprawdź w kodzie:** `09_protected_variations/violation.py` linia 12-20

## 🎯 Workflow z GRASP

1. **Przegląd violations** (20 min) - wspólne identyfikowanie problemów
2. **Parowe ćwiczenia** (15 min) - refactoring w exercises.md
3. **Dyskusja solutions** (10 min) - porównanie z wzorcowymi rozwiązaniami

## 🔗 Powiązania z SOLID

- **Information Expert** ↔ Single Responsibility
- **Low Coupling** ↔ Dependency Inversion
- **Polymorphism** ↔ Open/Closed Principle
- **Protected Variations** ↔ Open/Closed + Interface Segregation

GRASP **kieruje** projektowaniem, SOLID **sprawdza** czy design jest dobry.
