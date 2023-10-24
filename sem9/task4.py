# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        my_dict = {}

        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
                my_dict[i] = result
            return my_dict
        return wrapper
    return deco


@count(5)
def my_sum(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    result = my_sum(2, 5)
    print(result)
