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
import json


def save_json(func):
    with open('.\sem9\\task3.json', 'r', encoding='utf-8') as f2:
        my_dict = json.load(f2)
        print(my_dict)
    # input()

    def wrapper(*args, **kwargs):
        my_dict.update({'args': args, **kwargs})
        result = func(*args, ** kwargs)
        print(result)
        my_dict.update({f'{args[0]} + {args[1]} result': result})

        with open(f'.\sem9\\task3.json', 'w', encoding='utf-8') as f2:
            json.dump(my_dict, f2, ensure_ascii=False, indent=4)
        return result
    return wrapper


@save_json
def my_sum(num1, num2, *args, **kwargs):
    return num1 + num2


if __name__ == "__main__":
    result = my_sum(2, 5, 74, -84, www=False, d=True, z='stroka', y=145)
    print(result)
