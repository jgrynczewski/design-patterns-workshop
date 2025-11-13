# GRASP - General Responsibility Assignment Software Patterns
Ogólne wzorce przydzielania odpowiedzialności w oprogramowaniu

## Co to jest GRASP?

GRASP to zestaw 9 zasad, które pomagają **przypisywać odpowiedzialności** do klas w systemie obiektowym

## 1. Information Expert (Ekspert informacji)
**Definicja:** Przypisz odpowiedzialność klasie, która ma informacje potrzebne do realizacji zadania.

**Dlaczego:** Klasa która ma dane powinna je też przetwarzać - to naturalne i minimalizuje coupling.

**Kiedy łamiesz:** Gdy klasa A przetwarza dane z klasy B, zamiast klasy B, która powinna robić sama.

## 2. Creator (Kreator)
**Definicja:** Klasa A powinna tworzyć instancje klasy B, jeśli A zawiera, agreguje lub ściśle używa B.

**Dlaczego:** Twórca wie, kiedy i jak stworzyć obiekt. Redukuje dependencies.

**Kiedy łamiesz:** Gdy obiekty są tworzone przez klasy, które ich nie używają bezpośrednio.

## 3. Controller (Kontroler)
**Definicja:** Przypisz odpowiedzialność za obsługę use case klasie, która reprezentuje system, subsystem lub scenariusz użycia.

**Dlaczego:** Separuje logikę biznesową od warstwy prezentacji. Centralizuje orchestrację.

**Kiedy łamiesz:** Gdy UI klasy bezpośrednio manipulują obiektami domenowymi (logiką biznesową).

## 4. Low Coupling (Luźne sprzężenia)
**Definicja:** Minimalizuj zależności między klasami. Klasy powinny znać jak najmniej innych klas.

**Dlaczego:** Łatwiejsze zmiany, testing, reusability. Mniejsza prawdopodobieństwo wystąpienia efektu domina.

**Kiedy łamiesz:** Gdy klasa zna zbyt wiele konkretnych implementacji zamiast abstrakcji.

## 5. High Cohesion  (Wysoka spójność)
**Definicja:** Klasa powinna mieć spójną odpowiedzialność - wszystkie jej metody powinny współpracować w realizacji jednego celu.

**Dlaczego:** Łatwiejsza do zrozumienia, maintainability, reusability.

**Kiedy łamiesz:** Gdy klasa robi zbyt wiele niezależnych rzeczy.

## 6. Polymorphism (Polimorfizm)
**Definicja:** Użyj polimorfizmu zamiast if/else czy switch statements do obsługi wariantów zachowania.

**Dlaczego:** Kod jest łatwiejszy do rozbudowy. Dodanie nowych typów nie wymaga zmian w istniejącym kodzie.

**Kiedy łamiesz:** Gdy używasz type checking (isinstance, type) do różnych zachowań.

## 7. Pure Fabrication (Czysta fabrykacja)
**Definicja:** Stwórz klasę, która nie reprezentuje rzeczywistej koncepcji domenowej, ale jest potrzebna ze względów technicznych.

**Dlaczego:** Pozwala zachować wysoką kohezję (spójność) i luźne sprzeżenia.

**Kiedy łamiesz:** Gdy logika biznesowa ma techniczne odpowiedzialności (database, logging, etc.).

## 8. Indirection
**Definicja:** Wprowadź pośredni obiekt między dwoma komponentami, aby zmniejszyć bezpośrednie sprzężenia.

**Dlaczego:** Decoupling pozwala na niezależne zmiany. Łatwiejsze testing i podmiana implementacji.

**Kiedy łamiesz:** Gdy klasy bezpośrednio zależą od konkretnych implementacji zewnętrznych systemów.

## 9. Protected Variations (Chronione zmiany)
**Definicja:** Zabezpiecz stabilne elementy systemu przed wpływem niestabilnych elementów.

**Dlaczego:** System jest odporny na zmiany zewnętrzne. Łatwiejsze adaptowanie do nowych założeń.

**Kiedy łamiesz:** Gdy system bezpośrednio zależy od na przykład niestabilnych zewnętrznych APIs.

## 🔗 Powiązania z SOLID

- **Information Expert** ↔ Single Responsibility
- **Low Coupling** ↔ Dependency Inversion
- **Polymorphism** ↔ Open/Closed Principle
- **Protected Variations** ↔ Open/Closed + Interface Segregation

GRASP **kieruje** projektowaniem, SOLID **sprawdza** czy design jest dobry.
