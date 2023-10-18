# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

# import random as rnd
# from sys import argv  # вызов с терминала!!!

# user_data = argv[1:]
# # print(type(user_data))
# # print(user_data)
# strok, my_name = user_data
# strok = int(strok)
# print(strok)
# print(my_name)

# print(type(strok))
# print(type(my_name))

# START = -1_000
# STOP = 1_001


# def my_file(strok: int, my_name: str):
#     with open(my_name, 'w', encoding='utf-8') as f:
#         for _ in range(strok):
#             my_int = rnd.randint(START, STOP)
#             my_float = rnd.uniform(START, STOP)
#             my_strok = str(f'{my_int}|{my_float}')
#             print(my_strok)
#             print(my_strok, file=f)


# my_file(strok, my_name)


# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

# import random as rnd
# glasn = "aeiou"
# letters = "qwertyuiopasdfghjklzxcvbnm"


# def gen_names(file_name, num_names):
#     with open(file_name, 'w', encoding='utf-8') as f:
#         for _ in range(num_names):
#             name_len = rnd.randint(4, 7)
#             flag = 1
#             while flag == 1:
#                 name = ""
#                 for _ in range(name_len):
#                     let = rnd.choice(letters)
#                     name += "".join(rnd.choice(letters))
#                     name = name + let
#                     if len(name) == name_len and any(let in glasn for let in name):
#                         name = name.capitalize()
#                         print(name, file=f)
#                         flag = 0


# num_names = 5 # количество имен в файле
# file_name = "my_name.txt"
# gen_names(file_name, num_names)


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

file_name = "my_num.txt"
file_name2 = "my_name.txt"
with open(file_name, 'r', encoding='utf-8') as f1, \
    open(file_name2, 'r', encoding='utf-8') as f2,\
        open("new_res", 'w', encoding='utf-8') as f3:
    # print(res)
    # print(res)

    num = list(f1)
    name = list(f2)
    num_len = len(num)
    name_len = len(name)
    k1 = k2 = 0  # поправочный коэффициент

    for i in range(max(num_len, name_len)):
        # проверка на достижение конца файла и применение коэффициента
        if i == num_len:
            k1 = num_len
        elif i == name_len:
            k2 = name_len

        a, b = map(float, num[i-k1][:-1].split("|"))
        if "\n" in name[i-k2]:
            name[i-k2] = name[i-k2][:-1]

        if a*b > 0:
            res = name[i-k2].upper()
            res2 = round(a*b)
            f3.write(f'{res} {res2} \n')

        if a*b < 0:
            res = name[i-k2].lower()
            res2 = abs(a*b)
            f3.write(f'{res} {res2} \n')
        print(res, " ", res2)
        input()
