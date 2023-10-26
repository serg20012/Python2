# Задание №1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math
from random import randint


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def len(self):
#         p = 2 * math.pi * self.radius
#         return p

#     def s(self):
#         s = math.pi * self.radius ** 2
#         return s


# c1 = Circle(4)
# print(c1.len())
# print(c1.s())

# Задание №2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


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


# c1 = Pryme(2)
# print(c1.per())
# print(c1.s())

# Задание №3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

# class Human:
#     def __init__(self, f1, f2, f3, age):
#         self.f1 = f1
#         self.f2 = f2
#         self.f3 = f3
#         self._age = age
#         self.female = 'm' or 'w'

#     def bithday(self):
#         self._age += 1

#     def get_age(self):
#         print(self._age)

#     def full_name(self):
#         print(f'{self.f1} {self.f3} {self.f2} {self._age}')

#     # def pol(self):
#     #     print(self.female)


# c1 = Human("Ivanov", "Ivan", "Ivanovich", 30)
# c1.get_age()
# c1.full_name()
# c1.bithday()
# c1.get_age()

# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

# class Human:
#     def __init__(self, f1, f2, f3, age):
#         self.f1 = f1
#         self.f2 = f2
#         self.f3 = f3
#         self._age = age
#         self.female = 'm' or 'w'

#     def bithday(self):
#         self._age += 1

#     def get_age(self):
#         print(self._age)

#     def full_name(self):
#         print(f'{self.f1} {self.f3} {self.f2} {self._age}')


# class Person(Human):
#     def __init__(self, f1, f2, f3, age, id):
#         super().__init__(f1, f2, f3, age)
#         if len(str(id)) == 6:
#             self.id = id
#         else:
#             self.id = randint(100_000, 999_999)

#     def sec_lev(self):
#         print(self.id)
#         summ = sum(int(i) for i in str(self.id))
#         self.sec_lev = summ % 7
#         return self.sec_lev


# c1 = Person("Ivanov", "Ivan", "Ivanovich", 30, 11111211)
# print(c1.sec_lev())


# Задание №5
# 📌 Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# class Fish:
#     def __init__(self, name, plavnik):
#         self.name = name
#         self.plavnik = plavnik

#     def unic(self):
#         print(f'{self.plavnik =}')


# class Bird:
#     def __init__(self, name, krily):
#         self.name = name
#         self.krily = krily

#     def unic(self):
#         print(self.krily)


# class Grass:
#     def __init__(self, name, listok):
#         self.name = name
#         self.listok = listok

#     def unic(self):
#         print(self.listok)


# c1 = Fish("akula", "treugol")
# c2 = Bird("vorobey", "prymie")
# c3 = Grass("sosna", "xvoy")
# print(c1.name)
# c1.unic()
# print(c2.name)
# c2.unic()
# print(c3.name)
# c3.unic()

# Задание №6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, unuc_property):
        self.name = name
        self.unuc_property = unuc_property

    def unic(self):
        print(f'{self.name} имеет {self.unuc_property}')


class Fish(Animal):
    def __init__(self, name, unuc_property):
        super().__init__(name, unuc_property)


class Bird(Animal):
    def __init__(self, name, unuc_property):
        super().__init__(name, unuc_property)


class Grass(Animal):
    def __init__(self, name, unuc_property):
        super().__init__(name, unuc_property)


fish = Fish("Акула", "треугольный плавник")
bird = Bird("vorobey", "прямые крылья")
grass = Grass("sosna", "зеленая хвоя")
print(fish.name)
fish.unic()

print(bird.name)
bird.unic()

print(grass.name)
grass.unic()
