# Задание №5
#   Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
#   Ключ словаря - загадка, значение - список с отгадками.
#   Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.

from task4_new import my_zag
__all__ = ["my_zag2"]


def my_zag2():
    dict_zag = {
        "что синего цвета ": ["небо", "море", "цветок"],
        "города России: ": ["Питер", "Москва", "Вронеж"],
        "типы данных: ": ["строка", "список", "кортеж"]
    }
    for key, value in dict_zag.items():
        my_zag(key, value, 3)

    return None


if __name__ == '__main__':
    my_zag2()
