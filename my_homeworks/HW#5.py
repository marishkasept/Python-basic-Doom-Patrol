#1
class Laptop:
    def __init__(self):
        self.battery = Battery("13%")

class Battery:
    def __init__(self, charge_percent):
        self.charge_percent = charge_percent

laptop = Laptop()
print(laptop.battery.charge_percent)

#2
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string

class GuitarString:
    def __init__(self, length):
        self.length = length

g_string = GuitarString('90cm')
guitar = Guitar(g_string)
print(guitar.guitar_string.length)

#3
class Calc:
    def __init__(self, first_num, second_num, third_num):
        self.first_num = first_num
        self.second_num = second_num
        self.third_num = third_num

    @staticmethod
    def add_nums(first_num, second_num, third_num):
        return first_num + second_num + third_num

calc = Calc(1, 2, 3)
print(Calc.add_nums(1, 2, 3))

#4

