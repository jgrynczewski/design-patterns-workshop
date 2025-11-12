"""BASIC: Composition over Inheritance Violation - tylko istota problemu"""


class Vehicle:
    def start(self):
        return "Engine started"


class Car(Vehicle):
    def drive(self):
        return "Driving on road"


class ElectricCar(Car):
    def start(self):
        return "Electric motor started"  # OK so far


class FlyingCar(Car):
    def fly(self):
        return "Flying in air"


# PROBLEM: How to create ElectricFlyingCar?
class ElectricFlyingCar(ElectricCar, FlyingCar):  # Multiple inheritance mess
    pass


class Boat(Vehicle):
    def sail(self):
        return "Sailing on water"


# PROBLEM: How to add electric boats? Another inheritance chain?
class ElectricBoat(Boat):
    def start(self):
        return "Electric motor started"  # Duplicate code!

# PROBLEM: Rigid hierarchy, duplicate code, hard to combine features
# Kluczowy problem: Każda kombinacja cech wymaga nowej klasy. Multiple inheritance jest problematyczne.
# Duplikacja kodu.
