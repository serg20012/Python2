# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

# import time


# class MyStr(str):
#     """ Класс Моя Строка, где будут доступны возможности str и долоплнительно хранится имя автора и время создания"""
#     def __new__(cls, value, name):
#         """Создание экземпляра класса"""
#         instance = super().__new__(cls, value)
#         instance.name = name
#         instance.tme = time.time()
#         return instance


# s = MyStr('Привет', 'Вася')
# print(s.upper())
# print(f'{s.name = }')
# print(f'{s.tme = }')
# print(MyStr.__doc__)

# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра


# class Arhiv():
#     list_number = []
#     list_string = []

#     def __init__(self, number, string):
#         self.value = number
#         self.name = string
#         Arhiv.list_number.append(number)
#         Arhiv.list_string.append(string)


# my_archiv1 = Arhiv(42, 'Привет')
# print(my_archiv1.list_number)  # Вывод: [42]
# print(my_archiv1.list_string)  # Вывод: ['Привет']

# my_archiv2 = Arhiv(12, 'второй')
# print(my_archiv2.list_number)  # Вывод: [42, 12]
# print(my_archiv2.list_string)  # Вывод: ['Привет', 'второй']

# my_archiv3 = Arhiv(13, 'третий')
# print(my_archiv3.list_number)  # Вывод: [42, 12, 13]
# print(my_archiv3.list_string)  # Вывод: ['Привет', 'второй', 'третий']

# Задание №4
# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.

# class Arhiv():
#     list_number = []
#     list_string = []

#     def __init__(self, number, string):
#         self.value = number
#         self.name = string
#         Arhiv.list_number.append(number)
#         Arhiv.list_string.append(string)

#     def __repr__(self):
#         return f'Экземпляр класса Arhiv({self.value}, {self.name})'

#     def __str__(self):
#         return f' что то Arhiv({self.value}, {self.name})'


# my_archiv1 = Arhiv(42, 'Привет')

# print(my_archiv1)
# print(repr(my_archiv1))
# print(my_archiv1.__str__)

# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

# import random


# class Pryme:
#     def __init__(self, x, y=None):
#         self.x = x
#         if y:
#             self.y = y
#         else:
#             self.y = x

#     def per(self):
#         p = self.x + self.x + self.y + self.y
#         return p

#     def s(self):
#         s = self.x*self.y
#         return s

#     def __add__(self, other):
#         x3 = self.x
#         new_per = self.per() + other.per()
#         y3 = (new_per - 2 * x3) / 2
#         return Pryme(x3, y3)

#     def __sub__(self, other):
#         new_per = self.per() - other.per()
#         if new_per <= 0:
#             raise ValueError("Отрицательный или нулевой периметр недопустим.")
#         else:
#             x3 = 0
#             y3 = 0
#             while x3 <= 0 or y3 <= 0:
#                 x3 = random.randint(1, new_per)
#                 y3 = (new_per - 2 * x3) / 2
#             return Pryme(x3, y3)


# c1 = Pryme(25, 7)
# c2 = Pryme(14, 14)
# c3 = c1-c2
# print(c3.per())
# print(c3.x, c3.y)

# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

# import random


# class Pryme:
#     def __init__(self, x, y=None):
#         self.x = x
#         if y:
#             self.y = y
#         else:
#             self.y = x

#     def per(self):
#         p = self.x + self.x + self.y + self.y
#         return p

#     def s(self):
#         s = self.x*self.y
#         return s

#     def __add__(self, other):
#         x3 = self.x
#         new_per = self.per() + other.per()
#         y3 = (new_per - 2 * x3) / 2
#         return Pryme(x3, y3)

#     def __sub__(self, other):
#         new_per = self.per() - other.per()
#         if new_per <= 0:
#             raise ValueError("Отрицательный или нулевой периметр недопустим.")
#         else:
#             x3 = 0
#             y3 = 0
#             while x3 <= 0 or y3 <= 0:
#                 x3 = random.randint(1, new_per)
#                 y3 = (new_per - 2 * x3) / 2
#             return Pryme(x3, y3)

#     def __eq__(self, other):
#         return self.s() == other.s()


# c1 = Pryme(10, 10)
# c2 = Pryme(50, 2)
# print(c1.s())
# print(c2.s())
# # c3 = c1-c2
# print(c1 == c2)
