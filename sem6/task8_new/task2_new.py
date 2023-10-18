# Задание №2
#   Создайте модуль с функцией внутри.
#   Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
#   Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
#   Функция выводит подсказки “больше” и “меньше”.
#   Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.
from random import randint

__all__ = ["find"]


def find_(a: int, b: int, popit: int) -> bool:
    number = randint(a, b)
    print(number)  # загаданное число для проверки
    for i in range(1, popit+1):
        our_num = int(input(f'Попытка номер {i} BB chislo: '))
        if our_num > number:
            print("загаданное число меньше")
        elif our_num < number:
            print("загаданное число больше")
        else:
            return True
        if i == popit:
            return False


if __name__ == '__main__':
    a, b, popit = map(int, input("BB start, stop, popit: ").split())
    print(find_(a, b, popit))
