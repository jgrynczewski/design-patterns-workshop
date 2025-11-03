  # Separation of Concerns (SoC)

  ## Definicja
  Różne aspekty programu (concerns) powinny być oddzielone w różnych modułach/klasach.

  ## Dlaczego stosować SoC?
  - **Łatwiejsze utrzymanie**: Zmiana jednego aspektu nie wpływa na inne
  - **Lepsza testowalność**: Każdy concern można testować osobno
  - **Większa elastyczność**: Można zmieniać implementację jednego aspektu bez wpływu na inne
  - **Czytelność kodu**: Każda klasa ma jasno określoną odpowiedzialność

  ## Główne concerns do rozdzielenia:
  - **Presentation Layer** (UI/kontrolery) - jak dane są prezentowane
  - **Business Logic** (domena) - reguły biznesowe i logika aplikacji
  - **Data Access** (persistence) - jak dane są przechowywane i pobierane
  - **Infrastructure** (logging, email, cache) - aspekty techniczne

  ## Typowe naruszenia:
  - Business logic zmieszana z UI kodem
  - Klasy domenowe zawierające SQL queries
  - Controllers zawierające reguły biznesowe
  - Persistence logic w presentation layer

  ## Kiedy łamiesz SoC:
  ❌ Klasa `User` zawiera kod do wysyłania emaili i zapisywania do bazy
  ❌ Controller bezpośrednio manipuluje bazą danych
  ❌ HTML templates zawierają business logic
  ❌ Domain objects znają szczegóły frameworka

  ## Przykłady w kodzie:
  - **Violation**: `violation.py` - User class robi wszystko
  - **Solution**: `solution.py` - Oddzielone warstwy
  - **Exercises**: `exercises.md` - Praktyczne refaktoryzowanie

  ## Powiązania z SOLID:
  - **SRP**: Jedna odpowiedzialność = jeden concern
  - **DIP**: Separation przez abstrakcje i dependency injection
  - **OCP**: Nowe concerns dodajesz bez zmiany istniejących
