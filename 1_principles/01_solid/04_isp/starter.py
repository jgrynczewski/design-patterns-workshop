"""
Interface Segregation Principle - Worker System

>>> human = Human("Alice")
>>> human.work()
'Alice is working'
>>> human.eat()
'Alice is eating'
>>> human.sleep()
'Alice is sleeping'

>>> robot = Robot("R2D2")
>>> robot.work()
'R2D2 is working'
"""

from abc import ABC, abstractmethod


# TODO: Zdefiniuj małe, wyspecjalizowane interfejsy
# Hint: Workable - tylko work()
# Hint: Eatable - tylko eat()
# Hint: Sleepable - tylko sleep()

class Workable(ABC):
    """Interfejs dla wszystkiego, co może pracować"""

    @abstractmethod
    def work(self) -> str:
        pass


# TODO: Dodaj Eatable
# Hint: @abstractmethod def eat() -> str

class Eatable:
    pass


# TODO: Dodaj Sleepable
# Hint: @abstractmethod def sleep() -> str

class Sleepable:
    pass


# TODO: Zaimplementuj Human
# Hint: Dziedziczy po Workable, Eatable, Sleepable
# Hint: work() zwraca "{name} is working"
# Hint: eat() zwraca "{name} is eating"
# Hint: sleep() zwraca "{name} is sleeping"

class Human:
    pass


# TODO: Zaimplementuj Robot
# Hint: Dziedziczy TYLKO po Workable (nie je, nie śpi)
# Hint: work() zwraca "{name} is working"

class Robot:
    pass


# ISP: Robot nie jest zmuszony implementować eat()/sleep()
# Małe, wyspecjalizowane interfejsy zamiast jednego grubego
