# Задание
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ unittest,


import math
from random import randint
import unittest


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len(self):
        p = 2 * math.pi * self.radius
        return p

    def s(self):
        s = math.pi * self.radius ** 2
        return s


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle1 = Circle(5)
        self.circle2 = Circle(10)

    def test_len(self):
        self.assertEqual(self.circle1.len(), 31.41592653589793)
        self.assertEqual(self.circle2.len(), 62.83185307179586)

    def test_s(self):
        self.assertEqual(self.circle1.s(), 78.53981633974483)
        self.assertEqual(self.circle2.s(), 314.1592653589793)


if __name__ == '__main__':
    unittest.main()
