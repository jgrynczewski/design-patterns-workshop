"""
Testy dla Iterator Pattern - Book Collection
"""

import pytest
from starter import Book, Iterator, BookIterator, BookCollection


class TestBook:
    """Testy klasy Book"""

    def test_book_creation(self):
        """Test tworzenia książki"""
        book = Book("1984", "George Orwell", 1949)

        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.year == 1949

    def test_book_str_representation(self):
        """Test reprezentacji string książki"""
        book = Book("Brave New World", "Aldous Huxley", 1932)

        str_repr = str(book)
        assert "Brave New World" in str_repr
        assert "Aldous Huxley" in str_repr
        assert "1932" in str_repr


class TestBookIterator:
    """Testy iteratora książek"""

    def test_iterator_implements_interface(self):
        """Test że BookIterator implementuje Iterator interface"""
        books = [Book("Test", "Author", 2000)]
        iterator = BookIterator(books)

        assert isinstance(iterator, Iterator)

    def test_has_next_with_elements(self):
        """Test has_next gdy są elementy"""
        books = [
            Book("Book 1", "Author 1", 2000),
            Book("Book 2", "Author 2", 2001)
        ]
        iterator = BookIterator(books)

        assert iterator.has_next() is True

    def test_has_next_without_elements(self):
        """Test has_next gdy nie ma elementów"""
        books = []
        iterator = BookIterator(books)

        assert iterator.has_next() is False

    def test_next_returns_correct_book(self):
        """Test że next() zwraca poprawną książkę"""
        books = [
            Book("First", "Author 1", 2000),
            Book("Second", "Author 2", 2001)
        ]
        iterator = BookIterator(books)

        first_book = iterator.next()
        assert first_book.title == "First"

        second_book = iterator.next()
        assert second_book.title == "Second"

    def test_next_advances_position(self):
        """Test że next() przesuwa pozycję iteratora"""
        books = [Book("Book 1", "Author 1", 2000)]
        iterator = BookIterator(books)

        assert iterator.has_next() is True
        iterator.next()
        assert iterator.has_next() is False

    def test_next_raises_stop_iteration(self):
        """Test że next() rzuca StopIteration na końcu"""
        books = [Book("Only One", "Author", 2000)]
        iterator = BookIterator(books)

        iterator.next()  # Pobierz jedyny element

        with pytest.raises(StopIteration):
            iterator.next()  # Powinno rzucić wyjątek

    def test_iterate_through_all_books(self):
        """Test iteracji przez wszystkie książki"""
        books = [
            Book("Book 1", "Author 1", 2000),
            Book("Book 2", "Author 2", 2001),
            Book("Book 3", "Author 3", 2002)
        ]
        iterator = BookIterator(books)

        collected_titles = []
        while iterator.has_next():
            book = iterator.next()
            collected_titles.append(book.title)

        assert collected_titles == ["Book 1", "Book 2", "Book 3"]

    def test_iterator_holds_reference_not_copy(self):
        """Test że iterator przechowuje referencję, nie kopię"""
        books = [Book("Original", "Author", 2000)]
        iterator = BookIterator(books)

        # Modyfikacja oryginalnej listy
        books.append(Book("Added", "Author 2", 2001))

        # Iterator powinien zobaczyć zmianę (ma referencję)
        count = 0
        while iterator.has_next():
            iterator.next()
            count += 1

        assert count == 2  # Widzi nowo dodaną książkę


class TestBookCollection:
    """Testy kolekcji książek"""

    def test_collection_creation(self):
        """Test tworzenia kolekcji"""
        collection = BookCollection()

        assert collection is not None

    def test_add_book(self):
        """Test dodawania książki do kolekcji"""
        collection = BookCollection()
        book = Book("Test Book", "Test Author", 2000)

        collection.add_book(book)

        iterator = collection.create_iterator()
        assert iterator.has_next() is True

    def test_create_iterator(self):
        """Test tworzenia iteratora"""
        collection = BookCollection()
        collection.add_book(Book("Book", "Author", 2000))

        iterator = collection.create_iterator()

        assert isinstance(iterator, Iterator)
        assert iterator.has_next() is True

    def test_multiple_independent_iterators(self):
        """Test że każdy iterator ma niezależny stan"""
        collection = BookCollection()
        collection.add_book(Book("Book 1", "Author 1", 2000))
        collection.add_book(Book("Book 2", "Author 2", 2001))
        collection.add_book(Book("Book 3", "Author 3", 2002))

        iterator1 = collection.create_iterator()
        iterator2 = collection.create_iterator()

        # Iterator 1 przesuń o 2 pozycje
        iterator1.next()
        iterator1.next()

        # Iterator 2 powinien nadal być na początku
        book = iterator2.next()
        assert book.title == "Book 1"

    def test_encapsulation_no_direct_access(self):
        """Test że kolekcja enkapsuluje wewnętrzną strukturę"""
        collection = BookCollection()

        # Nie powinno być publicznego atrybutu books
        assert not hasattr(collection, 'books')
        # Powinien być prywatny atrybut _books
        assert hasattr(collection, '_books')

    def test_empty_collection_iterator(self):
        """Test iteratora dla pustej kolekcji"""
        collection = BookCollection()

        iterator = collection.create_iterator()

        assert iterator.has_next() is False

        with pytest.raises(StopIteration):
            iterator.next()


class TestIteratorPattern:
    """Testy wzorca Iterator"""

    def test_iterator_hides_internal_structure(self):
        """Test że iterator ukrywa wewnętrzną strukturę"""
        collection = BookCollection()
        collection.add_book(Book("Book", "Author", 2000))

        iterator = collection.create_iterator()

        # Klient nie powinien znać szczegółów (np. że to lista z indeksem)
        # Używa tylko has_next() i next()
        assert hasattr(iterator, 'has_next')
        assert hasattr(iterator, 'next')

    def test_separation_of_concerns(self):
        """Test separacji odpowiedzialności"""
        collection = BookCollection()
        collection.add_book(Book("Book", "Author", 2000))

        # Kolekcja tworzy iteratory
        iterator = collection.create_iterator()

        # Iterator odpowiada za iterację
        # Kolekcja odpowiada za przechowywanie
        assert isinstance(iterator, BookIterator)
        assert isinstance(collection, BookCollection)

    def test_uniform_interface(self):
        """Test uniform interface iteratora"""
        books = [Book("Book", "Author", 2000)]
        iterator = BookIterator(books)

        # Każdy iterator ma ten sam interfejs
        assert callable(getattr(iterator, 'has_next', None))
        assert callable(getattr(iterator, 'next', None))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
