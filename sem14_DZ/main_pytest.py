# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ pytest.

import math
from random import randint
import pytest


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len(self):
        p = 2 * math.pi * self.radius
        return p

    def s(self):
        s = math.pi * self.radius ** 2
        return s


def test_len():
    circle1 = Circle(5)
    circle2 = Circle(10)
    assert circle1.len() == 31.41592653589793
    assert circle2.len() == 62.83185307179586


def test_s():
    circle1 = Circle(5)
    circle2 = Circle(10)
    assert circle1.s() == 78.53981633974483
    assert circle2.s() == 314.1592653589793
