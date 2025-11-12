"""
Interface Segregation Principle - Worker System - SOLUTION

>>> human = Human("Alice")
>>> human.work()
'Alice is working'
>>> human.eat()
'Alice is eating'

>>> robot = Robot("R2D2")
>>> robot.work()
'R2D2 is working'
"""

from abc import ABC, abstractmethod


class Workable(ABC):
    """Interfejs dla wszystkiego, co może pracować"""

    @abstractmethod
    def work(self) -> str:
        pass


class Eatable(ABC):
    """Interfejs dla wszystkiego, co może jeść"""

    @abstractmethod
    def eat(self) -> str:
        pass


class Sleepable(ABC):
    """Interfejs dla wszystkiego, co może spać"""

    @abstractmethod
    def sleep(self) -> str:
        pass


class Human(Workable, Eatable, Sleepable):
    """Człowiek - pracuje, je, śpi"""

    def __init__(self, name: str):
        self.name = name

    def work(self) -> str:
        return f"{self.name} is working"

    def eat(self) -> str:
        return f"{self.name} is eating"

    def sleep(self) -> str:
        return f"{self.name} is sleeping"


class Robot(Workable):
    """Robot - tylko pracuje, nie je, nie śpi"""

    def __init__(self, name: str):
        self.name = name

    def work(self) -> str:
        return f"{self.name} is working"


if __name__ == "__main__":
    print("=== ISP: Małe interfejsy ===\n")

    human = Human("Alice")
    print(human.work())
    print(human.eat())
    print(human.sleep())
    print()

    robot = Robot("R2D2")
    print(robot.work())
    # robot.eat()  # Robot nie ma eat() - ISP!
    print("\nISP: Robot nie musi implementować eat()/sleep()")
