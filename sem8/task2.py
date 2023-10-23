# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в # JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json

file_name = "new_res"


def secret():
    # Загрузка существующих данных из существующего файла
    my_dict_itog = {}
    namef = 'task2'
    with open(f'.\sem8\{namef}.json', 'r', encoding='utf-8') as f2:
        my_dict_itog = json.load(f2)

    while True:
        # Запрашиваем имя пользователя
        name = input("Name: ")
        if not name:  # Если введено пустое имя или пробел, выходим из цикла
            break
        id = input("id: ")
        # Проверка наличия ИД в существующих данных если есть в начало цикла
        if any(id in level_data for level_data in my_dict_itog.values()):
            print("id already in base, input again")
            continue
        level = input("level 1-7: ")
        # Добавляем новые данные в словарь
        if level in my_dict_itog:
            # Если уровень доступа есть добовлаем в этот словарь
            my_dict_itog[level].update({id: name})
        else:
            # иначе создаем новый
            my_dict_itog[level] = {id: name}

    # Сохраняем обновленные данные в файл
    with open(f'.\sem8\{namef}.json', 'w', encoding='utf-8') as f2:
        json.dump(my_dict_itog, f2, ensure_ascii=False,
                  indent=2, sort_keys=True)


# Запускаем функцию для выполнения
secret()
