# Задание №1
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.
# a=10
# print(type(a))
# b = 10.5
# print(type(b))
# c = "привет"
# print(type(c))
# d = True
# print(type(d))
# e1 = [1,2,3]
# print(type(e1))
# d1 = (1,2,3)
# print(type(d1))

# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
# import sys
# data = [10, False, 10, "hello"  "hello", 3.14, True, (1, 2, 3)]
# for i, j in enumerate(data, start=1):
#     print(f"{i}, {j}, id {id(j)}, размер: {sys.getsizeof(j)}, хеш {hash(j)}", sep=" ")
#     print("целое" if isinstance(j, int) else " не целое")
#     print("строчка" if isinstance(j, str) else " не строка")

# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# def sistem(x: int, metod: int) -> str:
#     res = ""
#     while x:
#         res = str(x % metod) + res
#         x = x // metod
#     return res


# x = int(input("Введите число: "))
# metod = int(input("Введите систему исчисления: "))
# print(bin(x))
# print(oct(x))
# print(sistem(x, metod))

# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import math
# diameter = float(input("Введите диаметр:? "))
# if diameter > 1000:
#     print("Диаметр не должен превышать 1000.")
# else:
#     radius = diameter / 2
#     # Вычисление площади круга
#     print(math.pi)
#     s = math.pi * (radius ** 2)
#     print("{:.42f}".format(math.pi * (radius ** 2)))
#     print("Площадь круга: {:.42f}".format(s))
#     # Вычисление длины окружности
#     dlin = 2 * math.pi * radius
#     print("Длина окружности: {:.42f}".format(dlin))

# Задание №5
# ✔ Напишите программу, которая решает  квадратные уравнения даже если
# дискриминант отрицательный. Используйте комплексные числа
# для извлечения квадратного корня.
# import cmath
# # Ввод коэффициентов уравнения
# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))

# # Вычисление дискриминанта
# D = b**2 - 4*a*c

# # Вычисление комплексных корней
# x1 = (-b + cmath.sqrt(D)) / (2*a)
# x2 = (-b - cmath.sqrt(D)) / (2*a)
# print(D)
# print("Корень x1:", x1)
# print("Корень x2:", x2)
