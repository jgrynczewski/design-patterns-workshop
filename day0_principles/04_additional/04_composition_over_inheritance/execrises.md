# Composition over Inheritance - Ćwiczenia

## 🎯 Cel
Nauka rozpoznawania problemów dziedziczenia i refaktoryzacji do kompozycji.

## 📋 Zadanie 1: Policz klasy (5 min)

**W `violation_basic.py` policz:**
1. Ile klas potrzebujesz dla wszystkich kombinacji?
2. Co się stanie jak dodasz nowy typ silnika (HybridMotor)?
3. Ile nowych klas musisz stworzyć?

**W `solution_basic.py` zobacz:**
4. Ile kombinacji możesz stworzyć bez dodawania klas?
5. Jak łatwo dodać nowy komponent?

## 🔨 Zadanie 2: Refaktoryzacja (10 min)

**Przerefaktoryzuj z dziedziczenia na kompozycję:**

```python
class Document:
    def format(self):
        return "Basic formatting"

class BoldDocument(Document):
    def format(self):
        return "Bold formatting"

class ItalicDocument(Document):
    def format(self):
        return "Italic formatting"

class BoldItalicDocument(BoldDocument, ItalicDocument):  # Problem!
    def format(self):
        return "Bold and italic formatting"

class UnderlineDocument(Document):
    def format(self):
        return "Underline formatting"
```

# Pytanie: Jak stworzyć BoldItalicUnderlineDocument?

Zadanie: Użyj kompozycji zamiast dziedziczenia.

💡 Zadanie 3: IS-A vs HAS-A (5 min)

Które relacje to dziedziczenie (IS-A), a które kompozycja (HAS-A)?

# A: Car and Engine
# B: Dog and Animal  
# C: House and Room
# D: Student and Person
# E: Computer and CPU
# F: Manager and Employee

Odpowiedź:
- Dziedziczenie (IS-A): B (Dog IS-A Animal), D (Student IS-A Person)
- Kompozycja (HAS-A): A (Car HAS-A Engine), C (House HAS-A Room), E (Computer HAS-A CPU)
- Zależy od kontekstu: F (Manager może IS-A Employee lub HAS-A Employee)

🎯 Zadanie 4: Projektowanie (10 min)

Zaprojektuj system pojazdu, który może:
- Mieć różne silniki (spalinowy, elektryczny, hybrydowy)
- Różne rodzaje kół (letnie, zimowe, terenowe)
- Opcjonalne wyposażenie (klimatyzacja, GPS, radio)

Pytania:
1. Ile klas potrzebujesz przy dziedziczeniu?
2. Jak rozwiążesz to kompozycją?
3. Którą metodę wybierasz i dlaczego?

✅ Sprawdź rozwiązania

Porównaj swoje projekty z solution.py
