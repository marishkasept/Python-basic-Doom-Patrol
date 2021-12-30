def calc_add(first, second):
    result = first + second
    with open("result.txt", "w") as file:
        file.write(f"{first} + {second} = {result}")


def calc_sub(first, second):
    result = first - second
    with open("result.txt", "w") as file:
        file.write(f"{first} - {second} = {result}")


def oper_recognition():
    first_num = int(input("Enter first number: "))
    operator = str(input("Enter operator: "))
    second_num = int(input("Enter second number: "))
    if operator == "+":
        calc_add(first_num, second_num)
    elif operator == "-":
        calc_sub(first_num, second_num)
    print("Your result is in the result.txt file")
    print("\n")
