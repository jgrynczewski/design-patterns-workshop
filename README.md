# Design Patterns Workshop

Warsztat wzorców projektowych w Pythonie

![Tests](https://github.com/YOUR-ORG/design-patterns-workshop/workflows/Design%20Patterns%20Labs/badge.svg)

## 📊 Postęp

### 📚 Intro
| Lab | Temat | Punkty |
|-----|-------|--------|
| 01 | Hello World | 5 |

### 🎯 Principles - GRASP
| Lab | Temat | Punkty |
|-----|-------|--------|
| 02 | Low Coupling | 10 |

### 🎯 Principles - SOLID
| Lab | Temat | Punkty |
|-----|-------|--------|
| 03 | Open/Closed Principle | 10 |
| 04 | Dependency Inversion | 10 |

### 🏭 Creational Patterns
| Lab | Temat | Punkty |
|-----|-------|--------|
| 05 | Factory Method | 15 |
| 06 | Abstract Factory | 15 |
| 07 | Builder | 15 |
| 08 | Singleton | 15 |

### 🏗️ Structural Patterns
| Lab | Temat | Punkty |
|-----|-------|--------|
| 09 | Adapter | 15 |
| 10 | Decorator | 15 |
| 11 | Facade | 15 |

### 🎭 Behavioral Patterns
| Lab | Temat | Punkty |
|-----|-------|--------|
| 12 | Strategy | 15 |
| 13 | Template Method | 15 |
| 14 | Flyweight | 15 |
| 15 | Iterator | 15 |

**Razem: 0/200 pkt**

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
# Lab 01 - Intro: Hello World
cd 0_intro/01_hello
pytest -v

# Lab 05 - Factory Method
cd 2_creational/01_factory_method
pytest -v

# Lab 09 - Adapter
cd 3_structural/01_adapter
pytest -v

# Lab 12 - Strategy
cd 4_behavioral/02_strategy
pytest -v

# Wszystkie testy naraz
pytest --tb=short
```

---

## ✅ Workflow

1. Edytuj `starter.py` w folderze laba
2. Uruchom testy: `pytest -v`
3. Commit & push gdy testy przejdą
4. Sprawdź wyniki w GitHub Actions

---

## 📁 Struktura laba

- `README.md` - Polecenie i teoria
- `starter.py` - **Tu piszesz kod** (wypełnij luki)
- `tests.py` / `test_*.py` - Testy (nie edytuj)
- `problem.py` - Kod bez wzorca (antyprzykład)

**Rozwiązania:** Sprawdź gałąź `solutions` po skończeniu laba

---

## 💡 Wskazówki

- Jeden lab na raz
- Czytaj `README.md` w folderze laba
- Sprawdzaj `violation.py`/`problem.py` (kod bez wzorca - czego NIE robić)
- Testuj często (`pytest -v`)
- Utknąłeś? Sprawdź gałąź `solutions`
