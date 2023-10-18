# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint as rnd

# это координаты ферзей:
# rastanovka = [[1, 2], [1, 4], [1, 6], [2, 8], [2, 2], [3, 5], [4, 8], [8, 6]]
#               0,      1,       2,      3        4,     5,      6,      7
rastanovka = [[1, 2], [1, 4], [1, 6], [2, 8], [2, 2]]
#               0,      1,       2,      3        4,     5,      6,      7

BOARD_SIZE = 5


def proverka(queen_positions: list) -> bool:
    # заполнение матрицы BOARD_SIZE х BOARD_SIZE  "0" пустые клетки "1" где стоит ферзь
    doska = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for x, y in rastanovka:
        doska[x-1][y-1] = 1
    # # # проверочная печать доски
    # for row in doska:
    #     print(row)
    # print("-------------------")
    #  проверка по горизонтали
    for x in doska:
        if sum(x) > 1:
            return False
    #  проверка по вертикали
    for x in range(BOARD_SIZE):
        sum_ver = 0
        for y in range(BOARD_SIZE):
            sum_ver = sum_ver+doska[y][x]
            if sum_ver > 1:
                return False
    # проверка по диагонали
    for i in range(BOARD_SIZE):
        for j in range(i+1, BOARD_SIZE):
            x1, y1 = queen_positions[i]
            x2, y2 = queen_positions[j]
            if abs(x1-x2) == abs(y1-y2):
                return False
    return True


result = 0
count = 0
while result < 4:  # цикл проверки до 4 вариантов
    for i in range(BOARD_SIZE):
        x = rnd(1, BOARD_SIZE)
        y = rnd(1, BOARD_SIZE)
        rastanovka[i] = [x, y]
    count += 1
    if proverka(rastanovka):
        print(f"Допустимая расстановка {rastanovka}")
        result += 1

print(f"Попыток проверки: {count}")
