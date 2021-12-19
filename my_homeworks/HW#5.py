import dataclasses
from collections import namedtuple


# 1
class Laptop:
    def __init__(self):
        self.battery = Battery("13%")


class Battery:
    def __init__(self, charge_percent):
        self.charge_percent = charge_percent


laptop = Laptop()
print(laptop.battery.charge_percent)


# 2
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self, length):
        self.length = length


g_string = GuitarString('90cm')
guitar = Guitar(g_string)
print(guitar.guitar_string.length)


# 3
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


# 4
class Pasta:
    vars = {'carbonara': ['bacon', 'parmesan', 'eggs'], 'bolognaise': ['forcemeat', 'tomatoes']}

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(cls.vars["carbonara"])

    @classmethod
    def bolognaise(cls):
        return cls(cls.vars["bolognaise"])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.carbonara()
print(pasta_2.ingredients)
pasta_3 = Pasta.bolognaise()
print(pasta_3.ingredients)


# 5
class Concert:
    max_visitors_num = 100

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self._visitors_count = Concert.max_visitors_num
        else:
            self._visitors_count = value


# Concert.max_visitor_num = 100
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)
concert.visitors_count = 10
print(concert.visitors_count)

# 6
# @dataclasses.dataclass
# class AddressBookDataClass:
#     key: int
#     name: str
#     phone_number: str
#     address: str
#     email: str
#     birthday: str
#     age: int
#
# adr_book1 = AddressBookDataClass(key=1,
#                                  name='Andrew',
#                                  phone_number='380674544323',
#                                  address='Balsaka 1',
#                                  email='mm@gmail.com',
#                                  birthday='01.01.1979',
#                                  age='43')
# print(adr_book1)

# 7
AddressBookDataClass = namedtuple('AddressBookDataClass',
                                  ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

adr_book2 = AddressBookDataClass(1, 'Andrew', '380674544323', 'Balsaka 1', 'mm@gmail.com', '01.01.1979', '43')
print(adr_book2)
print(adr_book2.phone_number)


# 8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return f'AddressBookDataClass(key={self.key}, name=\'{self.name}\', phone_number=\'{self.phone_number}\', address=\'{self.address}\', email=\'{self.email}\', birthday=\'{self.birthday}\', age=\'{self.age}\')'


adr_book3 = AddressBook(1, 'Andrew', '380674544323', 'Balsaka 1', 'mm@gmail.com', '01.01.1979', '43')
print(adr_book3)


# 9
class Person:

    def __init__(self, name, age, country):
        self.name = name
        self._age = age
        self.country = country

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


person = Person("John", 36, "USA")
print(person.age)
person.age = 42
print(person.age)


# 10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, 'Andrew')
setattr(student, 'email', 'mm@gmail.com')
print(getattr(student, 'email'))


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return ((self._temperature * 1.8) + 32)


temp_celc = Celsius(25)
print(temp_celc.temperature)
