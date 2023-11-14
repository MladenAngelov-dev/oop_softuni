from project.animals.animal import Animal, Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENT = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENT = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD = ["Meat", "Vegetable"]
    WEIGHT_INCREMENT = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENT = 1.0

    def make_sound(self):
        return "ROAR!!!"

