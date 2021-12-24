def calc_add(first, second):
    result = first + second
    with open("result.txt", "w") as file:
        file.write(f"{first} + {second} = {result}")

def calc_sub(first, second):
    result = first - second
    with open("result.txt", "w") as file:
        file.write(f"{first} - {second} = {result}")

def oper_recognition():
    first_num = int(input())
    operator = str(input())
    second_num = int(input())
    if operator == "+":
        calc_add(first_num, second_num)
    elif operator == "-":
        calc_sub(first_num, second_num)

