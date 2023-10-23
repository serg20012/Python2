# Задание №1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json

file_name = "new_res"


def text_json(name: str):
    my_dict = {}
    with open(name, 'r', encoding='utf-8') as f:
        for le in f:
            key, val = le.split()
            key = key.capitalize()
            val = float(val)
            my_dict[key] = val
        print(my_dict)

    with open(f'.\sem8\{name}.json', 'w') as f2:
        json.dump(my_dict, f2, ensure_ascii=False, indent=2)


text_json(file_name)
