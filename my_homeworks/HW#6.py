# Survival

import uuid
import time
from random import random, randint, choice
from abc import abstractmethod, ABC


class Animal(ABC):

    def __init__(self, name, force, power, speed):
        self.name = name
        self.force = force
        self.id = str(uuid.uuid4())
        self._max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest):
        pass


class Predator(Animal):

    def eat(self, forest):
        print(f"now {self.name}'s power: {self.current_power} points")
        prey = choice(forest._identificators)
        if self.id == prey:
            print(f"{self.name} chose himself, it's left without a dinner")
            print(f"now {self.name}'s power: {self.current_power} points")
        else:
            print(f'{self.name} tries to catch up {forest.animals[prey].name}')
            if self.speed > forest.animals[prey].speed:
                print(f'{self.name} caught up {forest.animals[prey].name}')
                print(f'{self.name} attacks {forest.animals[prey].name}')
                if self.force > forest.animals[prey].force:
                    print(f'{forest.animals[prey].name} is dead')
                    print(f'{self.name} eats {forest.animals[prey].name}')
                    forest.remove_animal(forest.animals[prey])
                    if self.current_power > 0.5 * self._max_power:
                        self.current_power = self._max_power
                    else:
                        self.current_power += 0.5 * self._max_power
                    print(f"now {self.name}'s power: {self.current_power} points")
                else:
                    print(f"{self.name} didn't have enough power, {forest.animals[prey].name} stayed alive")
                    if forest.animals[prey].current_power > 0.3 * forest.animals[prey]._max_power:
                        forest.animals[prey].current_power -= 0.3 * forest.animals[prey]._max_power
                        print(
                            f"now prey {forest.animals[prey].name}'s power: {forest.animals[prey].current_power} points")
                    else:
                        print(f"{forest.animals[prey].name}'s power has expired, it is dead")
                        forest.remove_animal(forest.animals[prey])
                    if self.current_power > 0.3 * self._max_power:
                        self.current_power -= 0.3 * self._max_power
                        print(f"now {self.name}'s power: {self.current_power} points")
                    else:
                        print(f"{self.name}'s power has expired, it is dead")
                        forest.remove_animal(forest.animals[self.id])
            else:
                print(f"the prey {forest.animals[prey].name} ran away from {self.name}")
                if forest.animals[prey].current_power > 0.3 * forest.animals[prey]._max_power:
                    forest.animals[prey].current_power -= 0.3 * forest.animals[prey]._max_power
                    print(f"now prey {forest.animals[prey].name}'s power: {forest.animals[prey].current_power} points")
                else:
                    print(f"prey {forest.animals[prey].name}'s power has expired, it is dead")
                    forest.remove_animal(forest.animals[prey])
                if self.current_power > 0.3 * self._max_power:
                    self.current_power -= 0.3 * self._max_power
                    print(f"now {self.name}'s power: {self.current_power} points")
                else:
                    print(f"{self.name}'s power has expired, it is dead")
                    forest.remove_animal(forest.animals[self.id])
        print('\n')


class Herbivores(Animal):

    def eat(self, forest):
        print(f"now {self.name}'s power: {self.current_power} points")
        if self.current_power > 0.5 * self._max_power:
            self.current_power = self._max_power
        else:
            self.current_power += 0.5 * self._max_power
        print(f'{self.name} eats...')
        print(f"now {self.name}'s power: {self.current_power} points")
        print('\n')


class Forest:

    def __init__(self):
        self.animals = dict()
        self.category = None
        self._identificators = list()

    def __iter__(self):
        return self

    def __next__(self):
        i = choice(self._identificators)
        return self.animals[i]

    def add_animal(self, animal):
        self._identificators.append(animal.id)
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        for i in range(len(self._identificators)):
            if animal.id == self._identificators[i]:
                del self.animals[animal.id]
                del self._identificators[i]
                break
            else:
                del self.animals[animal.id]

    def any_predator_left(self):
        for creature in self.animals.keys():
            if isinstance(self.animals[creature], Predator):
                return True
        return False


def animal_generator(value):
    wolf = Predator('wolf', randint(25, 100), randint(25, 100), randint(25, 100))
    bear = Predator('bear', randint(25, 100), randint(25, 100), randint(25, 100))
    fox = Predator('fox', randint(25, 100), randint(25, 100), randint(25, 100))
    hare = Herbivores('hare', randint(25, 100), randint(25, 100), randint(25, 100))
    squirrel = Herbivores('squirrel', randint(25, 100), randint(25, 100), randint(25, 100))
    snake = Predator('snake', randint(25, 100), randint(25, 100), randint(25, 100))
    mouse = Herbivores('mouse', randint(25, 100), randint(25, 100), randint(25, 100))
    hedgehog = Predator('hedgehog', randint(25, 100), randint(25, 100), randint(25, 100))
    moose = Herbivores('moose', randint(25, 100), randint(25, 100), randint(25, 100))
    beaver = Herbivores('beaver', randint(25, 100), randint(25, 100), randint(25, 100))
    while value >= 0:
        value -= 1
        yield choice([wolf, bear, fox, hare, squirrel, snake, mouse, hedgehog, moose, beaver])


if __name__ == "__main__":
    nature = animal_generator(10)

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        if not forest.any_predator_left():
            print("no predators left in the forest")
            break
        for animal in forest:
            animal.eat(forest)
        time.sleep(100)
