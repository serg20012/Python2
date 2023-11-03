# from collections import defaultdict


# class Storage:
#     def __init__(self):
#         self.storage = defaultdict(list)

#     def __str__(self):
#         txt = '\n'.join((f'{k}: {v}' for k, v in
#                          self.storage.items()))
#         return f'Объекты хранилища по типам:\n{txt}'

#     def __call__(self, value):
#         self.storage[type(value)].append(value)
#         return f'К типу {type(value)} добавлен {value}'


# s = Storage()
# print(s(42))
# print(s(72))
# print(s('Hello world!'))
# print(s(0))
# print(s)

# ----------------
# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.first < self.stop:
#             self.first, self.second = self.second, self.first + self.second
#             if self.start <= self.first < self.stop:
#                 return self.first
#         raise StopIteration


# fib = Fibonacci(20, 100)
# for num in fib:  # TypeError: 'Fibonacci' object is not iterable
#     print(num)


# # ----------------
# class Iter:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         for i in range(self.start, self.stop):
#             print(i)
#             input()
#             return chr(i)
#         raise StopIteration


# chars = Iter(65, 91)
# for c in chars:
#     print(c)
# --------------------

# import sqlite3

# connection = sqlite3.connect('sqlite.db')
# cursor = connection.cursor()
# cursor.execute("""create table if not exists users(name,
# age);""")
# cursor.execute("""insert into users values ('Гвидо', 66);""")
# connection.commit()
# connection.close()
# --------------
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = 0

#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value
#         else:
#             raise ValueError(
#                 f'Новый возраст должен быть больше текущего: {self._age}')

#     @age.deleter
#     def age(self):
#         self._age = "kkkk:"


# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло много лет. Изобретена технология перерождения.')
# del user.age
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# --------------

class Student:
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __str__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'


std1 = Student('Шурик', 7, 1, 12)
print(std1)
