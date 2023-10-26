# class Person:
#     pass


# p1 = Person()
# p1.level = 1
# p1.health = 100

# dict_p1 = {}
# dict_p1['level'] = 1
# dict_p1['health'] = 100

# print(f'{p1.health = }')
# print(f'{dict_p1["health"] = }')


# -------------------------
# class Person:
#     max_up = 3

#     def __init__(self):
#         self.level = 1
#         self.health = 100


# p1 = Person()
# p2 = Person()
# # print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
# # print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# # print(f'{Person.max_up = }, {Person.level = }, {Person.health = }')
# # # AttributeError: type object 'Person' has no attribute'level'
# Person.level = 100
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')
# --------------------
# class Person:
#     max_up = 3

#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100

#     def level_up(self):
#         self.level += 1

#     def change_health(self, dr, quantity):
#         self.health += quantity
#         dr.health -= quantity


# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# ------------------
# class User:
#     count = []

#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone


# u1 = User('One', '123-45-67')
# u2 = User('NoOne', '76-54-321')

# u1.count.append(42)
# u1.count.append(73)

# u2.counter = 256
# u2.count.append(u2.counter)
# # u2.count.append(u1.count[-1])
# # 42, 73
# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# # 256.73
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')

# ------------------------
# class Person:
#     __max_up = 3
#     _max_level = 80

#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3

#     def _check_level(self):
#         return self.level < self._max_level

#     def level_up(self):
#         if self._check_level():
#             self.level += 1

#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity

#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)


# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)

#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2

#     def add_many_up(self):
#         self.up += 1
#         self.up = min(self.up, self._Person__max_up * 2)


# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# p2 = Person('Маг', 'Тролль')


# print(f'{p1.health = }, {p2.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }')
# p2.change_health(p1, 10)
# print(f'{p1.health = }, {p2.health = }')
# print(p1.up, p2.up)
# p1.add_many_up()
# print(f'{p1.up = }')
# -------------
# class A:
#     def __init__(self):
#         print('Init class A')
#         self.data_a = 'A'


# class B:
#     def __init__(self):
#         print('Init class B')
#         self.data_b = 'B'


# class C:
#     def __init__(self):
#         print('Init class C')
#         self.data_c = 'C'


# class D:
#     def __init__(self):
#         print('Init class D')
#         self.data_d = 'D'


# class X1(A, C):
#     def __init__(self):
#         print('Init class X1')
#         super().__init__()


# class X2(B, D):
#     def __init__(self):
#         print('Init class X2')
#         super().__init__()


# class X3(A, D):
#     def __init__(self):
#         print('Init class X3')
#         super().__init__()


# class Z(X1, X2, X3):
#     def __init__(self):
#         print('Init class Z')
#         super().__init__()


# print(*Z.mro(), sep='\n')
# ---------------
class A:
    name = 'A'

    def call(self):
        print(f'I am {self.name}')


class B:
    name = 'B'

    def call(self):
        print(f'I am {self.name}')


class C:
    name = 'C'

    def call(self):
        print(f'I am {self.name}')


class D(C, A):
    pass


class E(D, B):
    pass


e = E()
e.call()
