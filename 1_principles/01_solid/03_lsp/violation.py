"""
Liskov Substitution Principle VIOLATION
Subklasa nie może zastąpić klasy bazowej
"""


class Bird:
    def fly(self):
        return "Flying"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Łamie kontrakt!


def make_bird_fly(bird):
    return bird.fly()


# PROBLEM: Penguin nie może zastąpić Bird

if __name__ == "__main__":
    sparrow = Sparrow()
    penguin = Penguin()

    print(make_bird_fly(sparrow))  # OK
    # print(make_bird_fly(penguin))  # CRASH! - łamie LSP
