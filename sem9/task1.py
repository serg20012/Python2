# Задание №1 # 📌 Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable
from random import randint


def my_main(x: int, y: int) -> Callable[[], None]:
    def game():
        for i in range(y):
            num = int(input("Vvedite chislo: "))
            if num == x:
                print(" yes ")
                break
            elif num > x:
                print("bolshe")
            else:
                print("menche")
        else:
            print(" end ")
    return game


if __name__ == '__main__':
    x = randint(1, 100)
    y = randint(1, 10)
    print(y)

    result = my_main(x, y)
    result()

    print(x)
