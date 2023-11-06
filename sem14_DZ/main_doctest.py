# Задание
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# Задание №1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math
from random import randint
import doctest


class Circle:
    """
    Represents a circle with a given radius.

    >>> circle1 = Circle(4)
    >>> circle1.len()
    25.132741228718345
    >>> circle1.s()
    50.26548245743669
    """

    def __init__(self, radius):
        self.radius = radius

    def len(self):
        p = 2 * math.pi * self.radius
        return p

    def s(self):
        s = math.pi * self.radius ** 2
        return s


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# c1 = Circle(4)
# print(c1.len())
# print(c1.s())
