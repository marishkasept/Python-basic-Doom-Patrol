# 1
class Vehicle:
    def __init__(self, max_speed, mileage, color):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

    def show_max_speed(self):
        print(f'My maximum speed is {self.max_speed}')


# 2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, color, free_seats_num):
        super().__init__(max_speed, mileage, color)
        self.free_seats_num = free_seats_num

    def take_seat(self):
        self.free_seats_num -= 1

    def seating_capacity(self):
        print(self.free_seats_num)


# 3
town_bus = Bus(130, 30, "red", 50)
print(type(town_bus))
# 4
school_bus = Bus(70, 15, "yellow", 75)
print(isinstance(school_bus, Vehicle))


# 5
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def show_number_of_students(self):
        print(f'Our school has {self.number_of_students} students')

    def get_school_id(self):
        print(f"It's school number {self.school_id}")


# 6
class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, color, free_seats_num, get_school_id, number_of_students):
        Bus.__init__(self, max_speed, mileage, color, free_seats_num)
        School.__init__(self, get_school_id, number_of_students)

    def bus_school_color(self):
        print(f'The color of the school bus is {self.color}')


# 7
class Bear:
    def __init__(self, fur_color, height, weight, sound="Aarrrgh"):
        self.fur_color = fur_color
        self.height = height
        self.weight = weight
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Wolf:
    def __init__(self, fur_color, height, weight, sound="Wooofoo"):
        self.fur_color = fur_color
        self.height = height
        self.weight = weight
        self.sound = sound

    def make_sound(self):
        print(self.sound)


misha = Bear('brown', 2., 120)
vova = Wolf('grey', 1.5, 75)

animals = (misha, vova)

for animal in animals:
    animal.make_sound()



