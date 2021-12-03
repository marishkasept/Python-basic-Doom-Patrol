from functools import reduce

# Intro
print("#1")
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))
print("#2")
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
print("#3")
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
print("#4")
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# String formatting
print("#5")
print("Anna has {} apples and {} peaches.".format(5, 3))
print("#6")
print("Anna has {1} apples and {0} peaches.".format("eight", "two"))
print("#7")
print("Anna has {apple_quant} apples and {peach_quant} peaches.".format(apple_quant=8, peach_quant=2))
print("#8")
print("Anna has {0:5} apples and {1:3} peaches.".format("zero", 2))
print("#9")
apple = 5
peach = "four"
print(f"Anna has {apple} apples and {peach} peaches.")
print("#10")
print(f"Anna has %d apples and %s peaches." % (apple, peach))
print("#11")
fruits = {"apple_num": apple, "peach_num": peach}
print(f"Anna has %(apple_num)d apples and %(peach_num)s peaches." % fruits)
# Comprehensions
print("#12")
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
print("#13")
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
print("#14")
dict_comprehension1 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension1)
print("#15")
dict_comprehension2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension2)
print("#16")
d1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d1[x] = x ** 3
print(d1)
print("#17")
d2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d2[x] = x ** 3
    else:
        d2[x] = x
print(d2)
# Lambda
print("#18")
a = 7
b = 5
c = 6
lmbd_check = lambda x, y: x if x < y else y
print(lmbd_check(a, b))
print("#19")


def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(a, b, c))
print("#20")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
print("#21")
print(sorted(lst_to_sort, reverse=True))
print("#22")
lmb_map = lambda x: x * 2
print(list(map(lmb_map, lst_to_sort)))
print("#23")
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = []
for num in range(3):
    list_C.append(list_A[num] ** list_B[num])
print(list_C)
print("#24")
print(reduce(lambda x, y: x + y, lst_to_sort))
print("#25")
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))
print("#26")
lst_of_b = [b for b in range(-10, 10)]
print(list(filter(lambda x: x < 0, lst_of_b)))
print("#27")
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]


def filt_common(x):
    if x in list_2:
        return True


new_list = list(filter(filt_common, list_1))
print(new_list)
