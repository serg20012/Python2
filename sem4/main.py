# Задание №1
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.
# text = "сьешь еще этих мягких французских булок"


# def func1(text: str) -> None:
#     text2 = text.split(" ")
#     text2 = sorted(text2)
#     print(text2)
#     x = max(len(word) for word in text2)
#     # print(x)
#     for i, word in enumerate(text2, start=1):
#         res = i, word
#         print(f'{i} {word:>{x}}')


# func1(text)

# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# text = "Привет как дела?"


# def perevod(text: str) -> list:
#     # sort_text = text.split("")
#     # print(sort_text)
#     sort_text = sorted(text, reverse=True)
#     print(sort_text)
#     redy_list = []
#     for i in sort_text:
#         # print(i)
#         if ord(i) not in redy_list:
#             redy_list.append(ord(i))
#     return redy_list


# # x = (sorted(set([ord(char) for char in text]), reverse=True))
# # print(*x)
# # x = set(x)
# # x = sorted(x, reverse=True)
# # print(x)
# # x = sorted(set(ord(char) for char in text), reverse=True)
# # print(x)
# # def func_sort(text):
# #     list=[]
# #     return unique_codes
# print(perevod(text))

# # Пример использования функции
# result = func_sort(text)
# print(result)

# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением —  целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# text = "1050 1045"


# def perevod(text: str) -> dict[str, int]:
#     dict1 = {}
#     num = text.split()
#     # print(num)
#     start = int(min(num))
#     # print(type(start))
#     end = int(max(num))
#     # print(start, end)
#     for i in range(start, end + 1):
#         print(i)
#         char = chr(i)
#         dict1[char] = i
#         print(dict1)
#         # input()
#     return dict1


# print(perevod(text))

# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# list1 = [244, 600, 250, 152, 546, 456]


# def sort_my(lst: list):
#     for i in range(len(list1)-1):
#         print(range(len(list1)-1))
#         for j in range(len(list1)-1-i):
#             print(range(len(list1)-1-i))
#             if list1[j] > list1[j+1]:
#                 list1[j+1], list1[j] = list1[j], list1[j+1]
#     return list1


# sort_my(list1)
# print(list1)

# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии
# name = "Иванов", "Петров", "Сидоров", "Пушкин"
# zp = [275, 150, 200, 350]
# nadbavka = "10.25%"


# def ras(name: list[str], zp: list[int], nadbavka: str) -> dict[str, int]:
#     tabl = {}
#     nadbavka = nadbavka.replace("%", "")
#     nadbavka = float(nadbavka)
#     for i in range(len(name)):
#         res = zp[i]/100*nadbavka+zp[i]
#         tabl[name[i]] = res
#     return tabl


# # ras (name, zp, nadbavka)
# print(ras(name, zp, nadbavka))

# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
#      0  1   2   3   4  5   6   7
zp = [10, 10, 20, 3, 43, 45, 65, 34]
index = list(map(int, input("BB index: ").split()))

# def tabl(zp: list[int], index: list[int]) -> int:
# start = min(index)
# end = max(index)
# if start < 0:
#     start = -1
# if end > len(zp):
#     end = len(zp)
# print(start, end)
# res = 0
# for i in range(start+1, end):
#     res = res + zp[i]
# # print(sum(zp[start:end]))
# return res
# print(tabl(zp, index))

# вариант 2


def tabl2(zp: list[int], index: list[int]) -> int:
    start = min(index)
    end = max(index)
    if start < 0:
        start = -1
    if end > len(zp):
        end = len(zp)
    return sum(zp[start+1:end])


print(tabl2(zp, index))
