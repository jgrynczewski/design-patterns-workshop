  # SOLID Principles

  ## Overview
  SOLID to akronim 5 fundamentalnych zasad programowania obiektowego, które pomagają tworzyć kod łatwiejszy do utrzymania, rozszerzania i testowania.

  ## S - Single Responsibility Principle (SRP)
  **Definicja:** Klasa powinna mieć tylko jeden powód do zmiany.

  **Dlaczego:** Łatwiejsze utrzymanie (maintenance), testowanie, luźniejsze sprzężenia (looser coupling) między komponentami.

  **Kiedy łamiesz:** Klasa robi więcej niż jedną rzecz (np. zarządza danymi + wysyła emaile + loguje).

  ## O - Open/Closed Principle (OCP)
  **Definicja:** Klasy powinny być otwarte na rozszerzenia, zamknięte na modyfikacje.

  **Dlaczego:** Nowe "funkcje" (rozszerzenia kodu) dodajesz bez zmiany istniejącego kodu.

  **Kiedy łamiesz:** Dodanie nowego typu wymaga modyfikacji istniejącej klasy (if/else chains).

  ## L - Liskov Substitution Principle (LSP)
  **Definicja:** Obiekty klasy bazowej powinny być zastępowalne obiektami podklas.

  **Dlaczego:** Polimorfizm działa poprawnie, bez niespodzianek.

  **Kiedy łamiesz:** Podklasa zmienia zachowanie klasy bazowej w sposób łamiący kontrakt.

  ## I - Interface Segregation Principle (ISP)
  **Definicja:** Klasy nie powinny być zmuszane do implementacji interfejsów, których nie używają.

  **Dlaczego:** Mniejsze, bardziej spójne interfejsy.

  **Kiedy łamiesz:** "Fat interfaces" z metodami, które większość implementacji nie potrzebuje.

  ## D - Dependency Inversion Principle (DIP)
  **Definicja:** Moduły wysokiego poziomu nie powinny zależeć od modułów niskiego poziomu. Oba powinny zależeć od abstrakcji.

  **Dlaczego:** Luźno powiązane komponenty, łatwiejsze testowanie.

  **Kiedy łamiesz:** Hardcoded dependencies, direct instantiation konkretnych klas.
