import csv
import random
import math
from typing import Callable


def quad_deco(func: Callable):
    def wrapper(a, b, c):
        with open('.\\sem9_DZ\\random.csv', 'r', encoding='utf-8') as f2:
            print(f2)

            return func(a, b, c)
    return wrapper


@quad_deco
def solve_quadratic_equation(a, b, c):
    a1 = math.sqrt(a)
    b1 = math.sqrt(b)
    c1 = math.sqrt(c)
    return a1, b1, c1


if __name__ == '__main__':

    a = 244
    b = 24
    c = 144
    roots = solve_quadratic_equation(a, b, c)

    print("Корни уравнения:", roots)
