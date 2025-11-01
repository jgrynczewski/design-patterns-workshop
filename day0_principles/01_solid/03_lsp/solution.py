"""
Liskov Substitution Principle SOLUTION
Podklasy mogą zastąpić klasę bazową
"""


class Bird:
    def move(self):
        return "Moving"


class FlyingBird(Bird):
    def fly(self):
        return "Flying"

    def move(self):
        return self.fly()


class SwimmingBird(Bird):
    def swim(self):
        return "Swimming"

    def move(self):
        return self.swim()


class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow flying"


class Penguin(SwimmingBird):
    def swim(self):
        return "Penguin swimming"


def make_bird_move(bird):
    return bird.move()


# ROZWIĄZANIE: Wszystkie podklasy mogą zastąpić Bird

if __name__ == "__main__":
    sparrow = Sparrow()
    penguin = Penguin()

    print(make_bird_move(sparrow))  # "Sparrow flying"
    print(make_bird_move(penguin))  # "Penguin swimming"
    # Oba działają! LSP zachowane
