class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

    def _get_info(self):
        print(f'Hello: {self.__age}')

    def __get_secret(self):
        print(f'pass: {self.__age}')

    def hello(self):
        self.__get_secret()




person = Person('Bob', 'Super', 29)
# print(person.name)
# print(person._surname)
# print(person.__age)
# person._get_info()
person.hello()
