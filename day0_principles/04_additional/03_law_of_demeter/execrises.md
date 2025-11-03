# Law of Demeter - Ćwiczenia

## 🎯 Cel
Nauka rozpoznawania łańcuchów wywołań i refaktoryzacji do delegacji.

## 📋 Zadanie 1: Policz kropki (5 min)

**W `violation_basic.py` znajdź:**
1. Ile kropek ma każde wyrażenie?
2. Które linie łamią "zasadę jednej kropki"?
3. Co kod musi "wiedzieć" o strukturze obiektów?

**W `solution_basic.py` zobacz:**
4. Jak każdy obiekt deleguje odpowiedzialność?
5. Ile kropek ma teraz każde wywołanie?

## 🔨 Zadanie 2: Refaktoryzacja łańcuchów (10 min)

**Przerefaktoryzuj ten kod zgodnie z Law of Demeter:**

```python
class User:
  def __init__(self, profile):
      self.profile = profile

class Profile:
  def __init__(self, settings):
      self.settings = settings

class Settings:
  def __init__(self, theme):
      self.theme = theme

class ThemeManager:
  def get_user_theme_color(self, user):
      # VIOLATION: Łańcuch wywołań
      return user.profile.settings.theme.primary_color

  def is_dark_mode(self, user):
      # VIOLATION: Łańcuch wywołań
      return user.profile.settings.theme.dark_mode_enabled
```

Zadanie: Dodaj metody delegujące, żeby każde wywołanie miało max 1 kropkę.

💡 Zadanie 3: Identyfikuj violations (5 min)

Które z tych łamią Law of Demeter?

```python
# A
order.calculate_total()

# B
order.customer.address.city.name

# C  
user.get_email()

# D
document.format.font.size

# E
cart.add_item(product)

# F
payment.gateway.provider.process()
```

Odpowiedź: B, D, F łamią (więcej niż 1 kropka)

🎯 Zadanie 4: "Przyjaciele" obiektu (5 min)

Z kim może rozmawiać metoda OrderService.process_order(order, payment)?

- Samego siebie (self)
- Parametry (order, payment)
- Pola klasy (self.repository)
- Utworzone obiekty (new Calculator())

Nie może: order.customer.address.validate() ← zbyt daleko!

✅ Sprawdź rozwiązania

Porównaj swoje refaktoryzacje z solution.py
