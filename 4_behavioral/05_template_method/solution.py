"""
Template Method Pattern - Document Generation

>>> # Test Report Document
>>> report = ReportDocument("Q4 Sales")
>>> doc = report.generate_document()
>>> "REPORT" in doc
True
>>> "Q4 Sales" in doc
True
>>> "End of Report" in doc
True

>>> # Test Email Document
>>> email = EmailDocument("Meeting Reminder")
>>> doc = email.generate_document()
>>> "Subject: Meeting Reminder" in doc
True
>>> "Dear User" in doc
True
>>> "automated email" in doc
True

>>> # Test hook method - signature
>>> report = ReportDocument("Test")
>>> report.add_signature()  # Hook method - domyślnie pusta implementacja
''
>>> email = EmailDocument("Test")
>>> email.add_signature()  # Email ma własną implementację
'Best regards,\\nThe Team'
"""

from abc import ABC, abstractmethod


# Document Generator - ROZWIĄZANIE
# WZORZEC: Base class z template method

class DocumentGenerator(ABC):
    """
    Bazowa klasa dla generatorów dokumentów

    KLUCZOWE dla wzorca Template Method:
    1. TEMPLATE METHOD: generate_document() definiuje szkielet (NIE jest abstract)
    2. PRIMITIVE OPERATIONS: create_header/body/footer (SĄ abstract)
    3. HOOK METHOD: add_signature() (ma domyślną implementację)
    """

    def __init__(self, title: str):
        self.title = title

    def generate_document(self) -> str:
        """
        TEMPLATE METHOD - definiuje szkielet algorytmu

        KLUCZOWE: Ta metoda NIE jest abstrakcyjna - definiuje flow
        Subklasy NIE nadpisują tej metody, tylko implementują kroki
        """
        # Szkielet algorytmu - zawsze te same kroki w tej samej kolejności
        header = self.create_header()  # Primitive operation
        body = self.create_body()  # Primitive operation
        signature = self.add_signature()  # Hook method (opcjonalny)
        footer = self.create_footer()  # Primitive operation

        # Składanie dokumentu
        result = header + "\n\n" + body

        if signature:  # Dodaj signature tylko jeśli nie jest pusty
            result += "\n\n" + signature

        result += "\n\n" + footer

        return result

    @abstractmethod
    def create_header(self) -> str:
        """Stwórz nagłówek - ABSTRACT (primitive operation)"""
        pass

    @abstractmethod
    def create_body(self) -> str:
        """Stwórz główną treść - ABSTRACT (primitive operation)"""
        pass

    @abstractmethod
    def create_footer(self) -> str:
        """Stwórz stopkę - ABSTRACT (primitive operation)"""
        pass

    def add_signature(self) -> str:
        """
        Hook method - opcjonalny podpis

        KLUCZOWE: Ma domyślną implementację (pusty string)
        Subklasy MOGĄ nadpisać, ale nie muszą
        """
        return ""  # Domyślnie brak podpisu


# Concrete Generators - ROZWIĄZANIE
# WZORZEC: Konkretne implementacje primitive operations

class ReportDocument(DocumentGenerator):
    """
    Generator raportów

    Implementuje tylko primitive operations (3 metody abstrakcyjne)
    Używa domyślnej implementacji hook method (add_signature)
    """

    def create_header(self) -> str:
        """Implementacja primitive operation - nagłówek raportu"""
        return (
            "=" * 50 + "\n"
            f"REPORT: {self.title}\n" +
            "=" * 50
        )

    def create_body(self) -> str:
        """Implementacja primitive operation - treść raportu"""
        return (
            "This is the main body of the report.\n"
            f"Report details for: {self.title}"
        )

    def create_footer(self) -> str:
        """Implementacja primitive operation - stopka raportu"""
        return (
            "-" * 50 + "\n"
            "End of Report\n" +
            "-" * 50
        )

    # NIE nadpisuje add_signature() - używa domyślnej (pusty string)


class EmailDocument(DocumentGenerator):
    """
    Generator emaili

    Implementuje primitive operations (3 metody abstrakcyjne)
    NADPISUJE hook method (add_signature) - dodaje podpis
    """

    def create_header(self) -> str:
        """Implementacja primitive operation - nagłówek emaila"""
        return (
            "From: system@example.com\n"
            f"Subject: {self.title}\n" +
            "=" * 40
        )

    def create_body(self) -> str:
        """Implementacja primitive operation - treść emaila"""
        return (
            "Dear User,\n\n"
            f"This email is regarding: {self.title}"
        )

    def create_footer(self) -> str:
        """Implementacja primitive operation - stopka emaila"""
        return (
            "-" * 40 + "\n"
            "This is an automated email.\n" +
            "-" * 40
        )

    def add_signature(self) -> str:
        """
        NADPISANIE hook method - email ma podpis

        KLUCZOWE: Hook method może być nadpisany jeśli potrzeba
        """
        return "Best regards,\nThe Team"


# Przykład użycia
if __name__ == "__main__":
    print("=== REPORT DOCUMENT ===")
    report = ReportDocument("Q4 Sales Report")
    print(report.generate_document())

    print("\n" + "=" * 60 + "\n")

    print("=== EMAIL DOCUMENT ===")
    email = EmailDocument("Meeting Reminder")
    print(email.generate_document())

    # KLUCZOWE: Wszyscy używają tego samego flow (generate_document)
    # ale każdy ma własne szczegóły implementacji kroków
