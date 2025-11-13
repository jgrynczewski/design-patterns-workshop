# Design Patterns Workshop

Warsztat wzorców projektowych w Pythonie

![Tests](https://github.com/YOUR-ORG/design-patterns-workshop/workflows/Design%20Patterns%20Labs/badge.svg)

## 📊 Postęp

| Lab | Temat | Punkty |
|-----|-------|--------|
| 01 | Intro: Kalkulator | 10 |
| 02 | GRASP: Low Coupling | 10 |
| 03 | SOLID: OCP | 10 |

**Razem: 0/30 pkt**

---

## 🚀 Start

```bash
git clone <repo-url>
cd design-patterns-workshop
pip install -r requirements.txt
```

---

## 🧪 Testowanie

```bash
# Lab 01 - Intro
cd 0_intro/01_hello
pytest -v

# Lab 02 - GRASP Low Coupling
cd 1_principles/01_grasp/04_low_coupling
pytest -v

# Lab 03 - SOLID OCP
cd 1_principles/02_solid/02_ocp
pytest -v
```

---

## ✅ Workflow

1. Edytuj `starter.py` w folderze laba
2. Uruchom testy: `pytest -v`
3. Commit & push gdy testy przejdą
4. Sprawdź wyniki w GitHub Actions

---

## 📁 Struktura laba

- `README.md` - Polecenie
- `starter.py` - Tu piszesz kod
- `test_*.py` - Testy (nie edytuj)
- `solution.py` - Rozwiązanie (sprawdź po zrobieniu)
- `violation.py` - Antyprzykład

---

## 💡 Wskazówki

- Jeden lab na raz
- Czytaj `README.md` w folderze laba
- Sprawdzaj `violation.py` (czego NIE robić)
- Testuj często
