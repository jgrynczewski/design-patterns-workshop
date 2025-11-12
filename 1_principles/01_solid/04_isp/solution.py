"""
Interface Segregation Principle SOLUTION
Małe, skupione interfejsy
"""

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax_document(self):
        pass


class SimplePrinter(Printable):
    def print_document(self):
        return "Printing"


class MultiFunctionPrinter(Printable, Scannable, Faxable):
    def print_document(self):
        return "Printing"

    def scan_document(self):
        return "Scanning"

    def fax_document(self):
        return "Faxing"


# ROZWIĄZANIE: Każda klasa implementuje tylko potrzebne interfejsy

if __name__ == "__main__":
    simple = SimplePrinter()
    multifunction = MultiFunctionPrinter()

    print(simple.print_document())  # OK
    print(multifunction.print_document())  # OK
    print(multifunction.scan_document())  # OK
    # simple nie ma scan_document() - nie jest zmuszony!
