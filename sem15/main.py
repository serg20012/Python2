# Задание №1
# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.

# import logging

# logging.basicConfig(filename='project.log', filemode='w',
#                     encoding='utf-8', level=logging.INFO)


# def div(x, y):
#     try:
#         result = x / y
#         return result
#     except ZeroDivisionError as e:
#         logging.error('Деление на ноль')
#         result = None
#         return result


# print(div(4, 0))


# Задание №2
# 📌 На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой
# функции.
import logging

FORMAT = '{levelname:<8} - {asctime}. записала сообщение: {msg}'

logging.basicConfig(filename='project2.log', format=FORMAT, style='{', filemode='w',
                    encoding='utf-8', level=logging.INFO)


def save_json(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            'args': args,
            'kwargs': kwargs,
            'result': result
        }
        logging.info(data)

        return result
    return wrapper


@save_json
def my_sum(num1, num2, *args, **kwargs):
    return num1 + num2


if __name__ == "__main__":
    result = my_sum(52, 5, 74, -84, www=False, d=True, z='stroka', y=145)
    print(result)


# # Задание №3
# # 📌 Доработаем задачу 2.
# # 📌 Сохраняйте в лог файл раздельно:
# # ○ уровень логирования,
# # ○ дату события,
# # ○ имя функции (не декоратора),
# # ○ аргументы вызова,
# # ○ результат.
