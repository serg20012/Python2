# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import csv
import json

import random
import math
from typing import Callable


def quad_deco(func: Callable):
    def wrapper(a, b, c):
        my_result = []
        with open('.\\sem9_DZ\\random.csv', 'r', newline='', encoding='utf-8') as f2:
            my_dict = csv.reader(f2)
            for line in my_dict:
                a, b, c = map(int, line)
                result = func(a, b, c)
                my_result.append(result)

            with open('.\sem9_DZ\\main.json', 'w', encoding='utf-8') as f3:
                json.dump(my_result, f3, ensure_ascii=False, indent=4)
    return wrapper


@quad_deco
def solve_quadratic_equation(a, b, c):
    a1 = math.sqrt(a)
    b1 = math.sqrt(b)
    c1 = math.sqrt(c)
    return a1, b1, c1


# Генерация случайных чисел и запись их в CSV файл


def generate_csv(num_rows):
    with open('.\\sem9_DZ\\random.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Генерация случайных чисел и запись в файл
        for _ in range(num_rows):
            num1 = random.randint(1, 1000)
            num2 = random.randint(1, 1000)
            num3 = random.randint(1, 1000)
            csvwriter.writerow([num1, num2, num3])


if __name__ == '__main__':

    # Количество строк
    num_rows = random.randint(10, 100)

    # Вызов функции для генерации CSV файла
    generate_csv(num_rows)

    a = 244
    b = 24
    c = 144
    roots = solve_quadratic_equation(a, b, c)

    print("Корни уравнения:", roots)
