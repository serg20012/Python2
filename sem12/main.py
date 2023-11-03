# Задание №1
# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

# class Factorial:
#     history = []

#     def __init__(self, k):
#         self.k = k

#     def calculate_factorial(self, n):
#         result = 1
#         for i in range(1, n + 1):
#             result *= i

#         if len(self.history) >= self.k:
#             self.history.pop(0)
#         self.history.append(result)
#         return result

#     def get_history(self):
#         return self.history

# f = Factorial(3)

# print(f.calculate_factorial(2))
# print(f.calculate_factorial(3))
# print(f.calculate_factorial(4))
# print(f.calculate_factorial(5))
# print(f.calculate_factorial(6))
# print(f.calculate_factorial(10))
# print(f.get_history())

# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

# import json


# class Factorial:

#     def __init__(self, k):
#         self.k = k
#         self.history = []

#     def calculate_factorial(self, n):
#         result = 1
#         for i in range(1, n + 1):
#             result *= i

#         if len(self.history) >= self.k:
#             self.history.pop(0)
#         self.history.append((n, result))
#         return result

#     def get_history(self):
#         return self.history

#     def __enter__(self):
#         print('Enter')
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         my_dict = {}
#         for n, result in self.history:
#             my_dict[n] = result
#         print(my_dict)
#         with open('factorial.json', 'w', encoding='utf-8') as f1:
#             print('Exit')
#             json.dump(my_dict, f1)


# with Factorial(3) as f:
#     print(f.calculate_factorial(2))
#     print(f.calculate_factorial(3))
#     print(f.calculate_factorial(4))
#     print(f.calculate_factorial(5))
#     print(f.calculate_factorial(6))
#     print(f.calculate_factorial(10))
#     print(f.get_history())

# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

# class Factorial:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.start, self.stop, self.step = args
#         elif len(args) == 2:
#             self.start, self.stop = args
#             self.step = 1
#         else:
#             self.start = 1
#             self.stop = args[0]
#             self.step = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.start < self.stop:
#             result = 1
#             for i in range(1, self.start+1):
#                 result *= i
#             self.start += self.step
#             return result
#         raise StopIteration


# f = Factorial(3, 10, 2)
# for i in f:
#     print(i)

# print(f.calculate_factorial(1, 5, 1))

# with Factorial(3) as f:
#     print(f.calculate_factorial(2))
#     print(f.calculate_factorial(3))
#     print(f.calculate_factorial(4))
#     print(f.calculate_factorial(5))
#     print(f.calculate_factorial(6))
#     print(f.calculate_factorial(10))
#     print(f.get_history())

# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.


import random


class Pryme:
    def __init__(self, x, y=None):
        self._x = x
        if y:
            self._y = y
        else:
            self._y = x

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("Недопустимое значение x")
        else:
            self._x = value

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("Недопустимое значение y")
        else:
            self._y = value

    def per(self):
        p = self._x + self._x + self._y + self._y
        return p

    def s(self):
        s = self._x*self._y
        return s

    def __add__(self, other):
        x3 = self._x
        new_per = self.per() + other.per()
        y3 = (new_per - 2 * x3) / 2
        return Pryme(x3, y3)

    def __sub__(self, other):
        new_per = self.per() - other.per()
        if new_per <= 0:
            raise ValueError("Отрицательный или нулевой периметр недопустим.")
        else:
            x3 = 0
            y3 = 0
            while x3 <= 0 or y3 <= 0:
                x3 = random.randint(1, new_per)
                y3 = (new_per - 2 * x3) / 2
            return Pryme(x3, y3)


c1 = Pryme(25, 7)
c2 = Pryme(14, 14)
c3 = Pryme(-100, 50)
print(c3.x)
# print(c3.x, c1.y)
