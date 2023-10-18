# Задание №7
#   Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
#   Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
#   Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
#   Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
#   Проверку года на високосность вынести в отдельную
# защищённую функцию.


# user_data = input("BB date d формате DD.MM.YYYY: ")


def my_data(user_data):
    day, mounth, year = map(int, user_data.split("."))
    # print(type(day), day)
    # print(type(mounth), mounth)
    # print(type(year), year)

    if day not in range(1, 32) or mounth not in range(1, 13) or year not in range(1, 10_000):
        print("1")
        return False
    elif mounth in [4, 6, 9, 11] and day > 30:
        return False
    elif mounth == 2:
        if _leap_year(year) is False and day >= 29:
            return False
        else:
            return True
    else:
        # print("10")
        return True  # Fkce


def _leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Visok ")
        return True
    else:
        print("Ne Visok")
        return False


if __name__ == '__main__':
    user_data = "29.02.2020"

    print(my_data(user_data))
