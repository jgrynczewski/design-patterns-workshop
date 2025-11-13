# 👋 Intro - Prosty Kalkulator

**Poziom**: bardzo łatwy  
**Cel**: Weryfikacja środowiska

## 🎯 Zadanie
Zaimplementuj dwie proste funkcje, żeby sprawdzić, że środowisko działa poprawnie.

## 📋 Wymagania
- [ ] Przechodzą doctesty
- [ ] Przechodzą testy jednostkowe (pytest)
- [ ] Funkcje działają z liczbami dodatnimi, ujemnymi i zerem

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Uruchom testy (powinny failować):
   - Doctests: `python -m doctest starter.py -v`
   - Pytest: `pytest` (lub `pytest -v` dla bardziej szczegółowego outputu)
3. Zaimplementuj funkcje `add()` i `multiply()`
4. Uruchom testy ponownie (teraz powinny przejść)
5. Gdy wszystkie testy przechodzą:
   ```bash
   git add .
   git commit -m "Complete Lab 01 - Calculator"
   git push
   ```
6. Sprawdź wynik w GitHub:
   - Wejdź w zakładkę **Actions** w swoim repo
   - Znajdź job "Lab 01 - Intro: Calculator"
   - ✅ Zielony = zadanie zaliczone!

## 💡 Podpowiedź
- Sprawdź doctests w `starter.py` - pokazują oczekiwane zachowanie
- `add(a, b)` powinno zwrócić sumę: `a + b`
- `multiply(a, b)` powinno zwrócić iloczyn: `a * b`

## ✅ Kryteria sukcesu
Wszystkie testy przechodzą (zielone ✅).

Jeśli tak, środowisko działa poprawnie. 🎉
