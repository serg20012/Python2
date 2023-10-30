from random import choices


# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#     # принтим только в учебных целях, а не для реальных задач
#         print(
#             f'Создал {self} со свойствами:\n' f'{self.name = },\t{self.equipment = },\t{self.life= }')


# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
# ----------------
class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман')
print('Создаём третий раз')
u_3 = User(name='Стэнц')
# ----------------
# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance


# # print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# # print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a * b
# print(f'{c = }\t{type(c) = }')

# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self, name: str):
#         self.name = name


# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(f'{a.name = }\n{b.name = }')

# -----------------
# import sys


# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')

#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')


# u_1 = User('Спенглер')
# print(u_1.name)
# print(sys.getrefcount(u_1))
# u_2 = u_1
# print(sys.getrefcount(u_1), sys.getrefcount(u_2))
# print(u_1.name)
# del u_1
# print(sys.getrefcount(u_2))
# print('Завершение работы')
# -------------------


# class Closet:
#     CLOTHES = ('брюки', 'рубашка', 'костюм',
#                'футболка', 'перчатки', 'носки', 'туфли')

#     def __init__(self, count: int, storeroom=None):
#         self.count = count
#         if storeroom is None:
#             self.storeroom = choices(self.CLOTHES, k=count)
#         else:
#             self.storeroom = storeroom

#     def __str__(self):
#         names = ', '.join(self.storeroom)
#         return f'Осталось вещей в шкафу {self.count}:\n{names}'

#     def __rshift__(self, other):
#         shift = self.count if other > self.count else other
#         self.count -= shift
#         return Closet(self.count, choices(self.storeroom, k=self.count))


# storeroom2 = Closet(10)
# print(storeroom2)
# for _ in range(4):
#     storeroom2 = storeroom2 >> 3
#     print(storeroom2)
#     input()
