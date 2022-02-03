from datetime import datetime
import os

#1. Rewrite the decorator "fare" from first task to use Class instead of function.

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


class Fare:
    def __init__(self, func):
        self.func = func

    def __call__(self, person):
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
        return self.func(person)


@Fare
def bridge(person):
    print(
        f'{person.name} passed the bridge with enough money. Current balance: {person.get_balance}. Tag: {person.tag}.')


if __name__ == '__main__':
    anna = Person(name='Anna', money=20, tag=True)
    bridge(anna)

#2*. Rewrite the decorator "logger" from fifth task to use Class instead of function and without passing args to decorator.

class Logger:
    def __init__(self, func, logfile='out.log'):
        self.func = func
        self.logfile = logfile

    def __call__(self):
        log = f'{self.func.__name__} was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger
def my_func():
    """
    This is my func
    """
    print(f'{my_func().__name__} is running')


my_func()