import math
from multiprocessing import Process


# 2. Write a program that will calculate two quadratic equations (6x² + 11x - 35 = 0. and 5x² - 2x - 9 = 0.)
# at the same time, set all the parameters of the equation in variables. (multiprocessing)

def quad_eq(a, b, c):
    discr = b ** 2 - 4 * a * c
    print("D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("No roots")


a1 = 6
b1 = 11
c1 = -35
a2 = 5
b2 = -2
c2 = -9

if __name__ == '__main__':
    process1 = Process(target=quad_eq(float(a1), float(b1), float(c1)))
    process2 = Process(target=quad_eq(float(a2), float(b2), float(c2)))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
