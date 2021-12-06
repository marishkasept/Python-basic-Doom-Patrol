class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def print_info(self):
        print(f'I am {self.name} {self.last_name}')


class Student(Person):
    def __init__(self, name, last_name, subject):
        super().__init__(name, last_name)
        self.subject = subject

    def learning(self):
        print(f'Learning: {self.subject}')

    def print_info(self):
        print(f'I am {self.name} {self.last_name}')
        print('I am 29 years old')

class Test:
    pass


mike = Student('Mike', 'Super', 'Math')
test = Test()
# print(mike.name)
# mike.print_info()
# mike.learning()
print(isinstance(test, Person))
print(isinstance(False, bool))

print(issubclass(Test, Student))