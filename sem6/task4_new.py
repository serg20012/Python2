# Задание №4
#   Создайте модуль с функцией внутри.
#   Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
#   Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

def my_zag(zag, var, popit) -> str:
    print("zagadka: ", zag)
    for i in range(popit):
        otvet = input(f'Попытка номер {popit-i} BB ответ: ')
        if otvet in var:
            print("OK!")
            i += 1
            return i
        else:
            print(f' неверно осталось {popit-i-1}')

    return 0


if __name__ == '__main__':
    zag = input("BB zag: ")
    var = input("3 варианта правильного ответа ").split()
    popit = int(input("кол-во попыток "))
    print(my_zag(zag, var, popit))
