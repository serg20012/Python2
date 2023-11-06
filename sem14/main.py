# Задание №1
# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

import doctest
import unittest
from string import ascii_lowercase as latin


def delete_test(text: str):
    '''
    >>> delete_test('hello')
    'hello'
    >>> delete_test('Hello')
    'hello'
    >>> delete_test('hello,')
    'hello'
    >>> delete_test('hello, мир!')
    'hello '
    >>> delete_test('Hello, World!')
    'hello world'
    '''
    result = ''
    text = text.lower()
    # latin = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        if char in latin or char == " ":
            result += char
    return result


res = delete_test('Hello, привет How, World!')
print(res)

# Задание №2
# 📌 Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

# doctest.testmod(verbose=True)


# Задание №3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
# from string import ascii_lowercase as latin
# import unittest


# class TestString(unittest.TestCase):
#     def test_not_change(self):
#         self.assertEqual(delete_test('hello'), 'hello')

#     def test_lower(self):
#         self.assertEqual(delete_test('Hello'), 'hello')

#     def test_punctuation(self):
#         self.assertEqual(delete_test('hello, !'), 'hello ')

#     def test_other_alphabet(self):
#         self.assertEqual(delete_test('Hello, мир!'), 'hello ')

#     def test_all(self):
#         self.assertEqual(delete_test('Hello, World, мир!'), 'hello world ')


# def delete_test(text: str):
#     result = ''
#     text = text.lower()
#     # latin = 'abcdefghijklmnopqrstuvwxyz'
#     for char in text:
#         if char in latin or char == " ":
#             result += char
#     return result


# unittest.main(verbosity=2)

# Задание №4
# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

# from string import ascii_lowercase as latin
# import pytest


# def test_not_change():
#     assert delete_test('hello') == 'hello'


# def test_lower():
#     assert delete_test('Hello') == 'hello'


# def test_punctuation():
#     assert delete_test('hello, !') == 'hello '


# def test_other_alphabet():
#     assert delete_test('Hello, мир!'), 'hello '


# def test_all():
#     assert delete_test('Hello, World, мир!') == 'hello world '


# def delete_test(text: str):
#     result = ''
#     text = text.lower()
#     # latin = 'abcdefghijklmnopqrstuvwxyz'
#     for char in text:
#         if char in latin or char == " ":
#             result += char
#     return result


# if __name__ == '__main__':
#     pytest.main()


# Задание №5
# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.
# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

# import random
# import unittest


# class Pryme:
#     def __init__(self, x, y=None):
#         self.x = x
#         if y:
#             self.y = y
#         else:
#             self.y = x

#     def per(self):
#         p = self.x + self.x + self.y + self.y
#         print(p)
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

#     def __eq__(self, other) -> bool:
#         return self.x == other.x and self.y == other.y


# class TestPryme(unittest.TestCase):
#     def setUp(self) -> None:
#         self.r1 = Pryme(3, 5)
#         self.r2 = Pryme(4, 6)
#         self.r3 = Pryme(1, 1)

#     def test_add_perimetr(self):
#         self.assertEqual(self.r1 + self.r2, Pryme(3, 15))

#     def test_created_object(self):  # Проверка создания объекта.
#         self.assertEqual(Pryme(3, 5), self.r1)

#     def test_perimetr(self):
#         self.assertEqual(self.r1.per(), 16)

#     def test_square(self):
#         self.assertEqual(self.r1.s(), 15)


# unittest.main(verbosity=2)

# c1 = Pryme(3, 5)
# # c2 = Pryme(14, 14)
# print(c1.per())
# # c3 = c1-c2
# # print(c3.per())
# # print(c3.x, c3.y)

# Задание №6
# 📌 На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

# import pytest
# import json


# class UserError(Exception):
#     pass


# class LevelError(UserError):
#     pass


# class AccessError(UserError):
#     def __str__(self) -> str:
#         return ' net usera '


# class User:
#     def __init__(self, name, id, level):
#         self.name = name
#         self.id = id
#         self.level = level

#     def __repr__(self) -> str:
#         return f'User({self.name}, {self.id}, {self.level})'

#     def __eq__(self, owner) -> bool:
#         if self.name == owner.name and self.id == owner.id:
#             return True
#         else:
#             return False

#     def __hash__(self) -> int:
#         return hash((self.name, self.id))


# file_name = "task4"


# class SignIn:

#     def __init__(self) -> None:
#         self.temp_user = None
#         self.set_user = set()

#     def text_json(self, file_name):
#         with open(f'.\\sem14\\{file_name}.json', 'r', encoding='utf-8') as f2:
#             data = json.load(f2)

#         for level, value in data.items():
#             for id, name in value.items():
#                 self.set_user.add(User(name, id, level))

#         return self.set_user

#     def sign_in(self, my_name, my_id):
#         new_user = User(my_name, my_id, 0)
#         if new_user not in self.set_user:
#             raise AccessError
#         else:
#             for user in self.set_user:
#                 if user == new_user:
#                     self.temp_user = user
#                     return self.temp_user

#     def add(self, name, id, lvl):
#         if lvl < self.temp_user.level:
#             raise LevelError
#         else:
#             new_user = User(name, id, 1)
#             self.set_user.add(new_user)
#         return new_user

#     def show(self):
#         return self.set_user


# @pytest.fixture
# def data():
#     sg1 = SignIn()
#     sg2 = SignIn()
#     user1 = User('vova', '788', 0)
#     user2 = User('pety', '25', 3)


# @pytest.fixture()
# def set_user():
#     user_set = {
#         User("serg", "123", "1"),
#         User("Pupkin", "34", "1"),
#         User("vova", "788", "3"),
#         User("dasa", "789", "5")
#     }
#     return user_set


# def test_sign_in():
#     sign = SignIn()
#     sign.text_json(file_name)
#     result = sign.sign_in('vova', '788')
#     assert result == User('vova', '788', '3')


# def test_load(set_user):
#     sign_in = SignIn()
#     res = sign_in.text_json(file_name)
#     assert res == set_user


# def test_1():
#     assert 1 == 1


# if __name__ == '__main__':
#     pytest.main()
