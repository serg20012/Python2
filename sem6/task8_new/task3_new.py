# Задание №3
#   Улучшаем задачу 2.
#   Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
#   Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
#   Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.
from task2_new import find_
from sys import argv

# print("ok")
a, b, popit = (int(arg) for arg in argv[1:])
# a, b, popit = map(int, argv[1:4])

print(a, b, popit)


if __name__ == '__main__':
    if find_(a, b, popit):
        print("Ugadal!")
    else:
        print("Ne ugadal")
