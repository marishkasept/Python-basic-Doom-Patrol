# 1. double_result

def double_result(func):
    def inner(*args):
        return func(*args) * 2

    return inner


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20


# 2. only_odd_parameters

def only_odd_parameters(func):
    def inner(*args):
        for arg in args:
            if arg % 2 == 0:
                return "Please use only odd numbers!"
        return func(*args)

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(3, 2, 1))  # "Please use only odd numbers!"
print(multiply(3, 5, 1, 7, 1))  # 105


# 3.* logged

def logged(func):
    def inner(*args, **kwargs):
        result = "("
        for k in args:
            result += f"{k}, "
        result = result[:-2]
        result += ")"
        print(f"you called {func.__name__}{result}")
        print(f"it returned {func(*args, **kwargs)}")

    return inner


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)  # you called func(4, 4, 4)


# it returned 6


# 4. type_check

def type_check(correct_type):
    def wrapper(func):
        def inner(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                return f"Wrong Type: {type(arg)}"

        return inner

    return wrapper


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(
    ['Not', 'A', 'String']))  # "Wrong Type: list" should be printed, since non-str passed to decorated function
