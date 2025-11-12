# 🔌 ISP - Worker System

**Difficulty**: easy
**Time**: 10 minutes
**Focus**: Interface Segregation Principle

## 🎯 Zadanie
Podziel gruby interfejs `Worker` na małe: `Workable`, `Eatable`, `Sleepable`.

## 📋 Wymagania
- [ ] `Eatable` - interfejs z `eat()`
- [ ] `Sleepable` - interfejs z `sleep()`
- [ ] `Human` - dziedziczy po wszystkich 3
- [ ] `Robot` - dziedziczy TYLKO po `Workable`

## 🚀 Jak zacząć
```bash
cd day0_principles/01_solid/04_isp
pytest test_isp.py -v
```

## 💡 ISP w pigułce

**Many client-specific interfaces > one general-purpose interface**

❌ **Źle** (gruby interfejs):
```python
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass   # Robot nie je! ❌
    @abstractmethod
    def sleep(self): pass # Robot nie śpi! ❌

class Robot(Worker):
    def eat(self): raise NotImplementedError  # Zmuszony!
    def sleep(self): raise NotImplementedError
```

✅ **Dobrze** (małe interfejsy):
```python
class Workable(ABC):
    def work(self): pass

class Eatable(ABC):
    def eat(self): pass

class Robot(Workable):  # Tylko to, co potrzebuje ✅
    def work(self): ...

class Human(Workable, Eatable, Sleepable):
    def work(self): ...
    def eat(self): ...
```

**Korzyść**: Robot nie implementuje eat()/sleep() - nie jest zmuszony.

Sprawdź `solution_isp.py` po wykonaniu.
