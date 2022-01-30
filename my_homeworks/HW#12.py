# 1. double_result
def double_result(func):
    result = func()
    return result * 2


def add(a, b):
    return a + b

print(add(5, 5))


@double_result
def add(a, b):
    return a + b

print(add(5, 5))
