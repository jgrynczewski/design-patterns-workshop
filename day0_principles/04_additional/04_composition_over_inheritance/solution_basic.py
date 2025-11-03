"""BASIC: Composition over Inheritance Solution - clean approach"""


# COMPONENTS - reusable behaviors
class Engine:
    def start(self):
        return "Engine started"


class ElectricMotor:
    def start(self):
        return "Electric motor started"


class FlightSystem:
    def fly(self):
        return "Flying in air"


# VEHICLES - compose behaviors
class Vehicle:
    def __init__(self, propulsion):
        self.propulsion = propulsion  # Composition!

    def start(self):
        return self.propulsion.start()


class Car(Vehicle):
    def __init__(self, propulsion, flight_system=None):
        super().__init__(propulsion)
        self.flight_system = flight_system  # Optional composition

    def drive(self):
        return "Driving on road"

    def fly(self):
        return self.flight_system.fly() if self.flight_system else "Cannot fly"


# EASY COMBINATIONS - no new classes needed!
regular_car = Car(Engine())
electric_car = Car(ElectricMotor())
flying_car = Car(Engine(), FlightSystem())
electric_flying_car = Car(ElectricMotor(), FlightSystem())

# RESULT: Flexible, reusable, no inheritance hierarchy explosion
# Kluczowa korzyść: Wszystkie kombinacje możliwe bez nowych klas. Komponenty reużywalne.
# Elastyczne kompozycje.
