"""
Interface Segregation Principle VIOLATION
Fat interface zmuszający do implementacji niepotrzebnych metod
"""

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def fax_document(self):
        pass


class SimplePrinter(Printer):
    def print_document(self):
        return "Printing"

    def scan_document(self):
        raise NotImplementedError("Cannot scan")  # Zmuszony do implementacji!

    def fax_document(self):
        raise NotImplementedError("Cannot fax")  # Zmuszony do implementacji!


# PROBLEM: SimplePrinter musi implementować metody, których nie potrzebuje

if __name__ == "__main__":
    printer = SimplePrinter()

    print(printer.print_document())  # OK
    # printer.scan_document()  # NotImplementedError!
    # printer.fax_document()   # NotImplementedError!
