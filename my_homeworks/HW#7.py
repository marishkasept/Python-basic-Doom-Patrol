# # **Garden**
# We have only one garden. In the garden can have vegetables, fruits and pests.
# Each fruit or vegetable should have a stage of maturity (stages: None, Flowering, Green, Red).
# Pests can eat only green and red fruit or vegetable. Once pests eat the fruit, it should be removed.

# ## There is a Tomato with the following characteristics:
# 1. Number of tomatoes (Index)
# 2. Vegetable type

# ### A tomato can:
# 1. Grow (move to the next stage of maturation)
# 2. Provide information about your maturity

# ### There is a Tomato Bush that:
# 1. Contains a list of tomatoes that grow on it

# ### And:
# 1. Grow with tomatoes
# 2. Provide information on the maturity of all tomatoes
# 3. Provide harvest

# ## There is an Apple with the following characteristics:
# 1. Number of apples (Index)
# 2. Fruit type

# ### An apple can:
# 1. Grow (move to the next stage of maturation)
# 2. Provide information about your maturity

# ### There is an Apple Tree that:
# 1. Contains a list of apples that grow on it

# ### And:
# 1. Grow with apples
# 2. Provide information on the maturity of all apples
# 3. Provide harvest

# ## And there is also a Gardener who has:
# 1. Name
# 2. The plants he looks after

# ### And:
# 1. Take care of the plant
# 2. Poison the pests
# 2. Harvest from it

# ## And there is also a Pests who have:
# 1. Type
# 2. Quantity


# ## And:
# 1. Eat the plants

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
        print(f"There are {self.vegetables} vegetables, {self.fruits} and {self.pests} pests")
        print("\n")


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

    def __init__(self, tomato_index, tomato_type):
        self.tomato_index = tomato_index
        self.tomato_type = tomato_type
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def is_ripe(self):
        return self.stage == 3

    def grow_info(self):
        print(f"{self.tomato_type} - {self.tomato_index}: {stages[self.stage]}")

class TomatoBush:

    def __init__(self, number_of_tomatoes):
        self.all_tomatoes = [Tomato('Rose', index) for index in range(number_of_tomatoes)]

    def grow_all(self):
        for tomato in self.all_tomatoes:
            tomato.grow()
            tomato.grow_info()

    def is_all_ripe(self):
        return all([tomato.is_ripe() for tomato in self.all_tomatoes])

    def give_harvest(self):
         self.all_tomatoes = []

class Apple(Fruit):
    def __init__(self, apple_index, apple_type):
        self.apple_index = apple_index
        self.apple_type = apple_type
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def is_ripe(self):
        return self.stage == 3

    def grow_info(self):
        print(f"{self.apple_type} - {self.apple_index}: {stages[self.stage]}")

class AppleTree:
    def __init__(self, number_of_apples):
        self.all_apples = [Apple('Golden', index) for index in range(number_of_apples)]

    def grow_all(self):
        for apple in self.all_apples:
            apple.grow()
            apple.grow_info()

    def is_all_ripe(self):
        return all([apple.is_ripe() for apple in self.all_apples])

    def give_harvest(self):
        self.all_apples = []


apple_tree = AppleTree(3)
tomato_bush = TomatoBush(4)

apple_tree.grow_all()
tomato_bush.grow_all()






