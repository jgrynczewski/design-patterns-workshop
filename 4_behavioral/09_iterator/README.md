# 📚 Iterator - Book Collection

**Poziom**: Średni
**Czas**: 15 minut
**Cel**: Iterator - sekwencyjny dostęp do elementów kolekcji bez ujawniania struktury

## 🎯 Zadanie
Zaimplementuj wzorzec Iterator dla kolekcji książek. Iterator enkapsuluje sposób przechodzenia przez kolekcję, ukrywając jej wewnętrzną strukturę.

## ✅ Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] `Iterator` interface z metodami `has_next()` i `next()`
- [ ] `BookIterator` implementujący Iterator
- [ ] `BookCollection.create_iterator()` zwracający iterator
- [ ] Enkapsulacja - brak bezpośredniego dostępu do wewnętrznej listy

## 🚀 Jak zacząć
1. Przejrzyj `problem.py` - zobacz problem bez iteratora
   ```bash
   python problem.py
   ```
2. Otwórz `starter.py`
3. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v` dla bardziej szczegółowego outputu)
4. Klasy `Book` i `Iterator` są już gotowe
5. Zaimplementuj:
   - `BookIterator` - konkretny iterator
   - `BookCollection.create_iterator()` - fabryka iteratora
6. Uruchom testy ponownie (teraz powinny przejść)

## 💡 Podpowiedzi
- **Kompozycja**: Iterator przechowuje referencję do kolekcji
- **Enkapsulacja**: Ukrywa wewnętrzną strukturę (lista, drzewo, etc.)
- **Separacja**: Logika iteracji oddzielona od kolekcji
- **Uniform interface**: has_next() i next() dla wszystkich iteratorów
- Iterator nie kopiuje kolekcji - tylko przechowuje referencję

## 📝 Przykład użycia
```python
# Stwórz kolekcję
collection = BookCollection()
collection.add_book(Book("1984", "George Orwell", 1949))
collection.add_book(Book("Brave New World", "Aldous Huxley", 1932))

# Użyj iteratora
iterator = collection.create_iterator()
while iterator.has_next():
    book = iterator.next()
    print(book)
```

## 📊 Wzorzec w akcji

### ❌ Bez wzorca:
```python
# Bezpośredni dostęp do wewnętrznej struktury
class BookCollection:
    def __init__(self):
        self.books = []  # Publiczna lista ❌

# Klient musi znać szczegóły implementacji
for i in range(len(collection.books)):  # ❌
    print(collection.books[i])

collection.books.clear()  # ❌ Może zniszczyć kolekcję!
```

### ✅ Z wzorcem (Iterator):
```python
# Enkapsulacja wewnętrznej struktury
class BookCollection:
    def __init__(self):
        self._books = []  # Prywatna ✅

    def create_iterator(self):
        return BookIterator(self._books)

# Klient nie zna struktury
iterator = collection.create_iterator()
while iterator.has_next():  # Uniform interface ✅
    print(iterator.next())
```

**Korzyść**: Zmiana wewnętrznej struktury (lista → drzewo) nie wymaga zmian w kliencie.

## 🎯 Use Cases
- **Kolekcje danych**: Przechodzenie przez różne struktury danych
- **Różne sposoby iteracji**: Forward, reverse, filtered iteratory
- **Enkapsulacja**: Ukrycie szczegółów implementacji przed klientem
- **Lazy loading**: Ładowanie elementów na żądanie

## 🐍 Iterator w Pythonie

W Pythonie wzorzec Iterator jest wbudowany w język jako **protokół iteratora**. Mapowanie klasycznego wzorca na struktury Pythona:
- `create_iterator()` → `__iter__()`
- `next()` → `__next__()`
- `has_next()` → sprawdzanie przez `StopIteration`

W tym ćwiczeniu używamy klasycznego podejścia GoF, aby skupić się na istocie wzorca bez dodatkowej złożoności protokołu Pythona.
