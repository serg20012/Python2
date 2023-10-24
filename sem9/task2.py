# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов.


from random import randint


def my_main(func: Callable):
    START = 1
    STOP = 100
    POPIT_START = 1
    POPITR_STOP = 10

    def wrapper(x, y):
        if x not in range(START, STOP+1):
            x = randint(1, 100)
            print("ispr")
        if y not in range(POPIT_START, POPITR_STOP+1):
            y = randint(1, 10)
        return func(x, y)
    return wrapper


@my_main
def game(x, y):
    for _ in range(y):
        num = int(input("Vvedite chislo: "))
        if num == x:
            print(" yes ")
            break
        elif num > x:
            print("y vas bolshe")
        else:
            print("y vas menche")
    else:
        print(" end ")


game(105, 5)
