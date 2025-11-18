"""
Iterator Pattern - Book Collection

>>> # Test basic iteration
>>> collection = BookCollection()
>>> collection.add_book(Book("1984", "George Orwell", 1949))
>>> collection.add_book(Book("Brave New World", "Aldous Huxley", 1932))
>>> collection.add_book(Book("Fahrenheit 451", "Ray Bradbury", 1953))
>>> iterator = collection.create_iterator()
>>> iterator.has_next()
True
>>> book = iterator.next()
>>> book.title
'1984'

>>> # Test iterating through all books
>>> collection = BookCollection()
>>> collection.add_book(Book("Book 1", "Author 1", 2000))
>>> collection.add_book(Book("Book 2", "Author 2", 2001))
>>> iterator = collection.create_iterator()
>>> count = 0
>>> while iterator.has_next():
...     book = iterator.next()
...     count += 1
>>> count
2

>>> # Test has_next returns False at end
>>> collection = BookCollection()
>>> collection.add_book(Book("Only One", "Solo", 2020))
>>> iterator = collection.create_iterator()
>>> iterator.next()
<Book: "Only One" by Solo (2020)>
>>> iterator.has_next()
False
"""

from abc import ABC, abstractmethod
from typing import List


# Book Class - GOTOWE
# Product - obiekt przechowywany w kolekcji

class Book:
    """Książka w bibliotece"""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.year})'

    def __repr__(self) -> str:
        return f'<Book: "{self.title}" by {self.author} ({self.year})>'


# Iterator Interface - GOTOWE
# WZORZEC: Interfejs iteratora z uniform API

class Iterator(ABC):
    """Interfejs iteratora"""

    @abstractmethod
    def has_next(self) -> bool:
        """Sprawdź czy są jeszcze elementy do przeiterowania"""
        pass

    @abstractmethod
    def next(self):
        """Zwróć następny element i przesuń wskaźnik"""
        pass


# Concrete Iterator - DO IMPLEMENTACJI
# WZORZEC: Konkretny iterator enkapsulujący sposób przechodzenia przez kolekcję

# TODO: Zaimplementuj BookIterator
# KLUCZOWE dla wzorca Iterator:
# 1. KOMPOZYCJA: iterator przechowuje referencję do kolekcji (nie kopiuje!)
# 2. ENKAPSULACJA: ukrywa szczegóły iteracji (indeks, logika przechodzenia)
# 3. SEPARACJA: logika iteracji oddzielona od kolekcji
#
# Metody do zaimplementowania:
# - __init__(self, books: List[Book]) - przechowaj books, ustaw self.index = 0
# - has_next() -> bool - sprawdź czy self.index < len(self.books)
# - next() -> Book - zwróć self.books[self.index], zwiększ self.index o 1
#   (przed zwróceniem sprawdź has_next(), jeśli False - raise StopIteration)

class BookIterator:
    pass


# Aggregate (Collection) - CZĘŚCIOWO GOTOWE
# WZORZEC: Kolekcja dostarczająca iterator

class BookCollection:
    """Kolekcja książek z enkapsulacją wewnętrznej struktury"""

    def __init__(self):
        # ENKAPSULACJA: prywatna lista (konwencja _ w Pythonie)
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Dodaj książkę do kolekcji"""
        self._books.append(book)

    # TODO: Zaimplementuj create_iterator
    # Zwraca nowy BookIterator z self._books
    # To pozwala na wielokrotną iterację (każdy iterator ma własny stan)

    def create_iterator(self) -> Iterator:
        """Tworzy iterator dla tej kolekcji"""
        pass


# Przykład użycia - odkomentuj gdy zaimplementujesz:
# if __name__ == "__main__":
#     # Tworzenie kolekcji
#     collection = BookCollection()
#     collection.add_book(Book("1984", "George Orwell", 1949))
#     collection.add_book(Book("Brave New World", "Aldous Huxley", 1932))
#     collection.add_book(Book("Fahrenheit 451", "Ray Bradbury", 1953))
#
#     # Użycie iteratora - klient nie zna wewnętrznej struktury!
#     print("=== Iteracja przez książki ===")
#     iterator = collection.create_iterator()
#     while iterator.has_next():
#         book = iterator.next()
#         print(book)
#
#     # Wiele niezależnych iteratorów
#     print("\n=== Dwa niezależne iteratory ===")
#     iterator1 = collection.create_iterator()
#     iterator2 = collection.create_iterator()
#
#     print(f"Iterator 1: {iterator1.next()}")
#     print(f"Iterator 1: {iterator1.next()}")
#     print(f"Iterator 2: {iterator2.next()}")  # Zaczyna od początku!
