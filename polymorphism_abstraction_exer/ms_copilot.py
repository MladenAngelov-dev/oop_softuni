
from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity

class Vegetable(Food):
    pass

class Fruit(Food):
    pass

class Meat(Food):
    pass

class Seed(Food):
    pass

class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if isinstance(food, Vegetable) and not isinstance(food, Seed):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        elif isinstance(food, Fruit) and not isinstance(food, Seed):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        elif isinstance(food, Meat):
            self.weight += food.quantity * self.weight_increase_per_food()
            self.food_eaten += food.quantity
            return None
        elif isinstance(food, Seed):
            self.weight += food.quantity * self.weight_increase_per_food()
            self.food_eaten += food.quantity
            return None
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    @abstractmethod
    def weight_increase_per_food(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight:.2f}, {self.food_eaten}]"


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def make_sound(self):
        return "Tweet"

    def weight_increase_per_food(self):
        return 0.25


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def make_sound(self):
        return "Roar"

    def weight_increase_per_food(self):
        return 0.40


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def weight_increase_per_food(self):
        return 0.35


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def weight_increase_per_food(self):
        return 0.10


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def weight_increase_per_food(self):
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def weight_increase_per_food(self):
        return 0.30

    def feed(self, food: Food):
        if isinstance(food, Vegetable) and not isinstance(food, Seed):
            self.weight += food.quantity * self.weight_increase_per_food()
            self.food_eaten += food.quantity
            return None
        elif isinstance(food, Meat):
            self.weight += food.quantity * self.weight_increase_per_food()
            self.food_eaten += food.quantity
            return None
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def weight_increase_per_food(self):
        return 1.00

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.weight += food.quantity * self.weight_increase_per_food()
            self.food_eaten += food.quantity
            return None
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
