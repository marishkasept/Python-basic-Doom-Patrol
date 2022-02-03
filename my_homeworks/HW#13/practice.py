import time
from datetime import datetime
import os

# 1
BRIDGE_FEE = 15
TAG_PRICE = 30


class PassageProhibited(Exception):
    def __init__(self, name, message='has no money to pass the bridge'):
        self.message = message
        self.name = name
        self.custom_message = f'{name} {message}'

    def __str__(self):
        return self.custom_message


class Person:
    def __init__(self, name, money, tag=False):
        self.name = name
        self.money = money
        self.tag = tag

    @property
    def get_balance(self):
        return self.money

    @property
    def get_label(self):
        return self.tag


def fare(func):
    def inner(person):
        if person.get_balance >= BRIDGE_FEE and person.tag:
            person.money -= BRIDGE_FEE
        elif person.get_balance >= BRIDGE_FEE and not person.tag:
            if person.get_balance >= BRIDGE_FEE + TAG_PRICE:
                person.money -= BRIDGE_FEE + TAG_PRICE
                person.tag = True
            else:
                raise PassageProhibited(person.name)
        else:
            raise PassageProhibited(person.name)
        return func(person)

    return inner


@fare
def bridge(person):
    print(
        f'{person.name} passed the bridge with enough money. Current balance: {person.get_balance}. Tag: {person.tag}.')


if __name__ == '__main__':
    anna = Person(name='Anna', money=20, tag=True)
    bridge(anna)


# 2
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'{self.func.__name__} runtime is {end - start}')
        return result


@Timer
def some_function(delay):
    time.sleep(delay)


# some_function(3)


# 3
class WrongFactorialArgument(Exception):
    def __init__(self, num, message=' - wrong number to calculate factorial'):
        self.num = num
        self.message = message

    def __str__(self):
        return f'{self.num} {self.message}'


def argument_test_natural_number(func):
    def inner(num):
        if isinstance(num, int) and num >= 0:
            return func(num)
        else:
            raise WrongFactorialArgument(num)

    return inner


@argument_test_natural_number
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 4

def lst_to_str(func):
    def inner(len):
        result = func(len)
        str_res = " ".join([str(elem) for elem in result])
        return str_res

    return inner


@lst_to_str
def sequence(seq_len):
    lst = []
    for i in range(1, seq_len + 1):
        x = 0
        while i != x:
            lst.append(i)
            x += 1
    return lst[:seq_len]


print(sequence(7))


# 5

def logger(logfile='out.log'):
    def logging_decorator(func):
        def inner(*args, **kwargs):
            log = f'{func.__name__} was executed at {datetime.now()}\n'
            print(log)
            with open(logfile, 'a') as file:
                file.write(log)

        return inner

    return logging_decorator


@logger()
def my_func():
    """
    This is my func
    """
    print(f'{my_func().__name__} is running')


# my_func()

# 6

def file_rename(filename):
    def rename_decorator(func):
        def inner():
            old_filename = func()
            os.rename(old_filename, filename)

        return inner

    return rename_decorator


@file_rename('hello.txt')
def create_file():
    file_name = "copy.txt"
    file = open(file_name, "w")
    file.write('Your text goes here')
    file.close()
    return file_name

#create_file()

