# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
print(os.getcwd())


def info_dir(my_path=os.getcwd()):
    my_dict = {}
    for dir_path, dir_name, ﬁle_name in os.walk(my_path):
        temp_f = []
        temp_d = []
        print(f'{dir_path = }\n{dir_name = }\n{ﬁle_name = }\n')

        # Рассчитываем размер файлов
        for filename in file_name:
            file_path = os.path.join(dir_path, filename)
            s = str((f'{filename} {os.path.getsize(file_path)}'))
            temp_f.append(s)

        # Рассчитываем размер директории с учетом всех файлов и поддиректорий
        for dirname in dir_name:
            d_path = os.path.join(dir_path, dirname)
            s1 = str(f'{dirname} {dir_size(d_path)}')
            temp_d.append(s1)

        # Добавляем новые данные в словарь
        my_dict[dir_path] = {
            'directories': temp_d,
            'files': temp_f
        }
    print(my_dict)
    # Сохраняем обновленные данные в файл

    with open(f'{my_path}\\result2.json', 'w', encoding='utf-8') as f2:
        json.dump(my_dict, f2, ensure_ascii=False,
                  indent=4, sort_keys=True)


def dir_size(d_path):  # функция подсчета размера директории
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(d_path):
        for f_name in file_name:
            filepath = os.path.join(dir_path, f_name)
            total_size += os.path.getsize(filepath)
    return total_size


info_dir('.\\sem8_DZ')
