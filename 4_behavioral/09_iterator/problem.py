"""
❌ PROBLEM: Bezpośredni dostęp do wewnętrznej struktury kolekcji

Rozwiązanie bez wzorca Iterator:
- Klient ma bezpośredni dostęp do wewnętrznej listy
- Naruszenie enkapsulacji - klient zna szczegóły implementacji
- Trudno zmienić wewnętrzną strukturę (np. z listy na drzewo)
- Niemożliwe dodanie różnych sposobów iteracji (forward, reverse, filtered)
- Klient odpowiedzialny za logikę przechodzenia przez kolekcję
"""

from typing import List


class Book:
    """Książka w bibliotece"""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.year})'


class BookCollection:
    """
    ❌ PROBLEM: Kolekcja książek z publicznym dostępem do listy

    Wystawia wewnętrzną listę books jako publiczny atrybut
    """

    def __init__(self):
        # ❌ PROBLEM: Publiczna lista - każdy może ją modyfikować!
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Dodaj książkę do kolekcji"""
        self.books.append(book)


# ❌ Przykład użycia
if __name__ == "__main__":
    # Tworzenie kolekcji
    collection = BookCollection()
    collection.add_book(Book("1984", "George Orwell", 1949))
    collection.add_book(Book("Brave New World", "Aldous Huxley", 1932))
    collection.add_book(Book("Fahrenheit 451", "Ray Bradbury", 1953))

    # ❌ PROBLEM 1: Klient musi znać wewnętrzną strukturę (lista)
    print("=== Iteracja przez książki ===")
    for i in range(len(collection.books)):  # ❌ Klient wie że to lista!
        print(collection.books[i])

    # ❌ PROBLEM 2: Bezpośredni dostęp do wewnętrznej struktury
    print(f"\nPierwsza książka: {collection.books[0]}")  # ❌ Bezpośredni dostęp!
    print(f"Liczba książek: {len(collection.books)}")  # ❌ Znamy implementację!

    # ❌ PROBLEM 3: Klient może modyfikować wewnętrzną strukturę!
    collection.books.clear()  # ❌ Możemy zniszczyć kolekcję!
    print(f"\nPo wyczyszczeniu: {len(collection.books)} książek")  # 0 - ups!

    # ❌ PROBLEM 4: Chcemy iterować od tyłu?
    collection.add_book(Book("Animal Farm", "George Orwell", 1945))
    collection.add_book(Book("Lord of the Flies", "William Golding", 1954))

    print("\n=== Iteracja od tyłu ===")
    for i in range(len(collection.books) - 1, -1, -1):  # ❌ Skomplikowana logika!
        print(collection.books[i])

    # ❌ PROBLEM 5: Chcemy iterować tylko po książkach z lat 50?
    print("\n=== Książki z lat 50 ===")
    for book in collection.books:  # ❌ Klient musi implementować filtrowanie!
        if 1950 <= book.year < 1960:
            print(book)

    # ❌ PROBLEM 6: Chcemy zmienić wewnętrzną strukturę z listy na drzewo?
    # Niemożliwe - wszystkie miejsca w kodzie klienta muszą się zmienić!
    # Wszędzie gdzie używamy collection.books[i] lub len(collection.books)


"""
Jakie problemy rozwiązuje Iterator?

1. ❌ Naruszenie enkapsulacji
   - Klient ma bezpośredni dostęp do wewnętrznej listy
   - Może modyfikować kolekcję (clear, append, remove)
   - Brak kontroli nad dostępem

2. ❌ Zależność od implementacji
   - Klient wie że to lista (używa indeksów, len())
   - Zmiana struktury (lista → drzewo) = breaking changes
   - Kod klienta związany z szczegółami implementacji

3. ❌ Duplikacja logiki iteracji
   - Każde miejsce w kodzie implementuje własną iterację
   - Iteracja od tyłu = skomplikowana logika w wielu miejscach
   - Filtrowanie = duplikacja kodu

4. ❌ Brak uniform interface
   - Różne kolekcje = różne sposoby iteracji
   - Lista: for i in range(len()), Dict: for key in dict.keys()
   - Trudno pisać kod generyczny

5. ❌ Niemożliwe różne sposoby iteracji
   - Chcemy forward, reverse, filtered iteratory?
   - Każdy sposób wymaga nowego kodu w kliencie
   - Brak reużycia

Jak Iterator to rozwiązuje?
1. Enkapsulacja - Iterator ukrywa wewnętrzną strukturę
2. Separacja - logika iteracji oddzielona od kolekcji
3. Uniform interface - has_next() i next() dla wszystkich
4. Różne iteratory - ForwardIterator, ReverseIterator, FilteredIterator
5. Możliwość zmiany implementacji kolekcji bez zmian w kliencie
"""
