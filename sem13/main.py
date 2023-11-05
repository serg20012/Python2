# Задание №1
# 📌 Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.
# def get_numeric_input():
#     while True:
#         data = input("Введите число: ")
#         try:
#             data = float(data)
#             return data
#         except ValueError:
#             print("Ошибка: введите целое или вещественное число.")


# if __name__ == '__main__':
#     print(get_numeric_input())

# Задание №2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.
# def get_dict_value(dictionary, key):
#     default_value = None
#     try:
#         return dictionary[key]
#     except KeyError:
#         print("Ошибка: нет ключа.")
#         return default_value


# dict1 = {"a": 1, "b": 2}
# print(get_dict_value(dict1, "aa"))

# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.
import json


class UserError(Exception):
    pass


class LevelError(UserError):
    pass


class AccessError(UserError):
    def __str__(self) -> str:
        return ' net usera '

# Задание №4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level

    # def __str__(self) -> str:
    #     return f'{self.name} {self.id} {self.level}'

    def __repr__(self) -> str:
        return f'User({self.name}, {self.id}, {self.level})'

    def __eq__(self, owner) -> bool:
        if self.name == owner.name and self.id == owner.id:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.name, self.id))


file_name = "task4"


# def text_json(file_name):
#     set_user = set()
#     with open(f'.\sem13\{file_name}.json', 'r', encoding='utf-8') as f2:
#         data = json.load(f2)

#     for level, value in data.items():
#         for id, name in value.items():
#             set_user.add(User(name, id, level))
#     return set_user


# print(text_json(file_name))

# Задание №5
# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


class SignIn:

    def __init__(self) -> None:
        self.temp_user = None
        self.set_user = set()

    def text_json(self, file_name):
        with open(f'.\sem13\{file_name}.json', 'r', encoding='utf-8') as f2:
            data = json.load(f2)

        for level, value in data.items():
            for id, name in value.items():
                self.set_user.add(User(name, id, level))

        return self.set_user

    def sign_in(self, my_name, my_id):
        new_user = User(my_name, my_id, 0)
        if new_user not in self.set_user:
            raise AccessError
        else:
            for user in self.set_user:
                if user == new_user:
                    self.temp_user = user
                    return self.temp_user

    def add(self, name, id, lvl):
        if lvl < self.temp_user.level:
            raise LevelError
        else:
            new_user = User(name, id, 1)
            self.set_user.add(new_user)
        return new_user

    def show(self):
        return self.set_user


sign_in1 = SignIn()
sign_in1.text_json(file_name)

print(sign_in1.sign_in('vova', '788'))
print(sign_in1.add('pety', '25', '3'))
print(sign_in1.show())
