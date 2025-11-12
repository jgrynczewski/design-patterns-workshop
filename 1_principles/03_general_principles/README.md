  # General Programming Principles

  ## Przegląd zasad

  Te 4 fundamentalne zasady to podstawa dobrego programowania, niezależnie od paradygmatu czy języka.

  ## 1. DRY - Don't Repeat Yourself
  **Definicja:** Każda wiedza w systemie powinna mieć jedną, jednoznaczną reprezentację.

  **Dlaczego:** Duplikacja = więcej miejsc do błędów i zmian. Zmiany w jednym miejscu.

  **Kiedy łamiesz:** Copy-paste kod, powtarzające się walidacje, identyczne metody.

  **Sprawdź w kodzie:** `01_dry/violation.py`

  ## 2. KISS - Keep It Simple, Stupid
  **Definicja:** Rozwiązania powinny być jak najprostsze, ale nie prostsze.

  **Dlaczego:** Prostość = łatwiejsze zrozumienie, maintenance i debugging.

  **Kiedy łamiesz:** Over-engineering, niepotrzebna abstrakcja, skomplikowane warunki.

  **Sprawdź w kodzie:** `02_kiss/violation.py`

  ## 3. YAGNI - You Ain't Gonna Need It
  **Definicja:** Implementuj funkcjonalność tylko wtedy, gdy rzeczywiście jej potrzebujesz.

  **Dlaczego:** Spekulacyjny kod = overhead, complexity bez wartości biznesowej.

  **Kiedy łamiesz:** "Future-proofing", nieużywane abstrakcje, przygotowanie "na wszelki wypadek".

  **Sprawdź w kodzie:** `03_yagni/violation.py`

  ## 4. Separation of Concerns (SoC)
  **Definicja:** Różne aspekty programu powinny być oddzielone w różnych modułach.

  **Dlaczego:** Każdy moduł skupia się na jednym aspekcie. Łatwiejsze zmiany i testowanie.

  **Kiedy łamiesz:** Business logic z UI, mieszanie persistence z domeną.

  **Sprawdź w kodzie:** `04_separation_of_concerns/violation.py`

  ## 🎯 Workflow

  1. **Code Review** (15 min) - identyfikacja violations we wszystkich 4 zasadach
  2. **Refactoring** (20 min) - grupowe poprawianie przykładów
  3. **Dyskusja** (10 min) - kiedy złamać zasady? Trade-offs w real world

  ## 🔗 Powiązania

  - **DRY** ↔ SOLID SRP (jedna odpowiedzialność = jedna implementacja)
  - **KISS** ↔ GRASP High Cohesion (prostota w spójności)
  - **YAGNI** ↔ Agile (iteracyjny development)
  - **SoC** ↔ SOLID wszystkie zasady (separacja to klucz)

  Te zasady **uzupełniają** SOLID i GRASP - są podstawowym mindsetem przed stosowaniem wzorców.
