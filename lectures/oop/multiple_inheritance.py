class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def print_info(self):
        print(f'I am {self.name} {self.last_name}')

    def learning(self):
        print(f'Learning: {self.subject}')


class Student:
    def __init__(self, subject):
        self.subject = subject

    def learning(self):
        print(f'Learning: {self.subject}')


class Resident(Person, Student):
    def __init__(self, name, last_name, subject):
        Person.__init__(self, name, last_name)
        Student.__init__(self, subject)


# mike = Resident('Mike', 'Super', 'Math')
# mike.print_info()
# mike.learning()

class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())
