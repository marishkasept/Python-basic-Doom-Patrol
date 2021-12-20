from abc import ABC, abstractmethod

stages = {0: 'None', 1: 'Flowering', 2: 'Green', 3: 'Red'}

class GardenMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Garden(metaclass=GardenMeta):

    def __init__(self, vegetables, fruits, pests):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests

    def see_the_garden(self):
        print(f"There are {self.vegetables.number_of_fruits} {self.vegetables.all_fruits[0].veg_type if self.vegetables.number_of_fruits > 0 else ''} tomato vegetables, {self.fruits.number_of_fruits} {self.fruits.all_fruits[0].fruit_type if self.fruits.number_of_fruits > 0 else ''}apple fruits and {', '.join(pest.pest_type for pest in self.pests)} pests in the garden")


class Vegetable(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def grow_info(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Fruit(ABC):

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def grow_info(self):
        pass

    @abstractmethod
    def is_ripe(self):
        pass


class Tomato(Vegetable):
    name = 'tomato'

    def __init__(self, tomato_index, veg_type):
        self.index = tomato_index
        self.veg_type = veg_type
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def is_ripe(self):
        return self.stage == 3

    def grow_info(self):
        print(f"{self.veg_type} tomato - {self.index}: {stages[self.stage]}")

class TomatoBush:

    def __init__(self, number_of_fruits):
        self.number_of_fruits = number_of_fruits
        self.all_fruits = [Tomato(index, 'Rose') for index in range(number_of_fruits)]

    def grow_all(self):
        for tomato in self.all_fruits:
            tomato.grow()
            tomato.grow_info()

    def is_all_ripe(self):
        return all([tomato.is_ripe() for tomato in self.all_fruits])

    def give_harvest(self):
        self.all_fruits = []
        self.number_of_fruits = 0

class Apple(Fruit):
    name = 'apple'

    def __init__(self, apple_index, fruit_type):
        self.index = apple_index
        self.fruit_type = fruit_type
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def is_ripe(self):
        return self.stage == 3

    def grow_info(self):
        print(f"{self.fruit_type} apple - {self.index}: {stages[self.stage]}")

class AppleTree:
    def __init__(self, number_of_fruits):
        self.number_of_fruits = number_of_fruits
        self.all_fruits = [Apple(index, 'Golden') for index in range(number_of_fruits)]

    def grow_all(self):
        for apple in self.all_fruits:
            apple.grow()
            apple.grow_info()

    def is_all_ripe(self):
        return all([apple.is_ripe() for apple in self.all_fruits])

    def give_harvest(self):
        self.all_fruits = []
        self.number_of_fruits = 0


class Gardener:
    def __init__(self, name, plants_to_care):
        self.name = name
        self.plants_to_care = plants_to_care

    def take_care(self):
        print(f'{self.name} is watering the plants...')
        for plant in self.plants_to_care:
            plant.grow_all()

    def take_harvest(self):
        for plant in self.plants_to_care:
            if plant.is_all_ripe():
                print("Harvest is done")
                plant.give_harvest()
            else:
                print("Not ready to harvest")

    def poison_pests(self, pests):
        print(f'The {pests.pest_type}s are dead')
        pests.are_alive = False



class Pests:
    def __init__(self, pest_type, pest_quantity, plants):
        self.pest_type = pest_type
        self.pest_quantity = pest_quantity
        self.plants = plants
        self.how_many_fed = 0
        self.are_alive = True

    def eat_plants(self):
        for plant in self.plants:
            if self.how_many_fed == self.pest_quantity or not self.are_alive:
                break
            elif plant.number_of_fruits < 1:
                continue

            i = 0
            while i < plant.number_of_fruits:
                if self.how_many_fed == self.pest_quantity:
                    break
                if plant.all_fruits[i].stage > 1:
                    print(f'{self.pest_type} ate {plant.all_fruits[i].name}')
                    plant.all_fruits.pop(i)
                    plant.number_of_fruits -= 1
                    for j in range(plant.number_of_fruits):
                        plant.all_fruits[j].index = j
                    self.how_many_fed += 1
                else:
                    i += 1


apple_tree = AppleTree(3)
tomato_bush = TomatoBush(4)

apple_tree.grow_all()
tomato_bush.grow_all()

for i in range(1):
    apple_tree.grow_all()
    tomato_bush.grow_all()

gardener = Gardener('Marcus', [apple_tree, tomato_bush])

gardener.take_care()
gardener.take_harvest()

print('There are:', 'no' if tomato_bush.number_of_fruits < 1 else '', ' tomato, '.join(tomato.veg_type for tomato in tomato_bush.all_fruits), 'tomato on the bush')
print('There are:', 'no' if apple_tree.number_of_fruits < 1 else '', ' apple, '.join(apple.fruit_type for apple in apple_tree.all_fruits), 'apple on the tree')

apple_tree1 = AppleTree(4)
tomato_bush1 = TomatoBush(7)

gardener.plants_to_care = [apple_tree1, tomato_bush1]
gardener.take_care()
apple_tree1.grow_all()

print('There are: ', ' tomato, '.join(tomato.veg_type for tomato in tomato_bush1.all_fruits), 'tomato on the bush')
print('There are: ', ' apple, '.join(apple.fruit_type for apple in apple_tree1.all_fruits), 'apple on the tree')


bugs = Pests('bug', 3, [tomato_bush1, apple_tree1])
bugs.eat_plants()

tomato_bush1.grow_all()

print('There are: ', ' tomato, '.join(tomato.veg_type for tomato in tomato_bush1.all_fruits), 'tomato on the bush')
print('There are: ', ' apple, '.join(apple.fruit_type for apple in apple_tree1.all_fruits), 'apple on the tree')


snails = Pests('snail', 2, [apple_tree1, tomato_bush1])
snails.eat_plants()
snails.eat_plants()
snails.eat_plants()

print('There are: ', ' tomato, '.join(tomato.veg_type for tomato in tomato_bush1.all_fruits), 'tomato on the bush')
print('There are: ', ' apple, '.join(apple.fruit_type for apple in apple_tree1.all_fruits), 'apple on the tree')

garden = Garden(tomato_bush1, apple_tree1, [bugs, snails])
garden.see_the_garden()

gardener.poison_pests(snails)
