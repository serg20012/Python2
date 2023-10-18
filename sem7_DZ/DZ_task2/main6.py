# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён

import os
import random as rnd

letters = "qwertyuiopasdfghjklzxcvbnm"


def create(direct, exe, min_dlin=6, max_dlin=30, min_infa=256, max_infa=4096, max_fales=5):
    if not os.path.exists(direct):  # Проверка наличия директории
        print(f"Директории {direct} не существует.")
        return

    for i in range(1, max_fales+1):  # цикл на кол-во файлов
        file_name = ""
        # генерерация длины имени файла
        name_len = rnd.randint(min_dlin, max_dlin)
        for _ in range(name_len):  # цикл на генерацию имя файла по длине
            let = rnd.choice(letters)
            file_name = file_name + let
        file_name = os.path.join(
            direct, file_name + "." + exe)  # Полный путь к файлу
        if os.path.exists(file_name):  # Проверка существования файла с таким именем
            print(f"Файл {file_name} уже существует.")
            continue
        with open(file_name, 'wb') as f1:  # создание файла
            for _ in range(min_infa, max_infa):  # генерация информации в файл
                #    случайное количество байт
                num_bytes = rnd.randint(min_infa, max_infa)
                random_data = bytes([rnd.randint(0, 255)
                                    for _ in range(num_bytes)])
                f1.write(random_data)
        print(f"Создан файл: {file_name}")


def gen_files(extensions, num_files_per_extension):  # формирование расширение и кол-ва файлов
    for i in range(len(extensions)):
        extension = extensions[i]
        num_files = num_files_per_extension[i]
        create(direct, extension, max_fales=num_files)


# Пример использования
exe = ["xxx", "yyy", "ppp"]
kol_files = [2, 2, 2]  # Количество файлов для каждого расширения
direct = "./sem7_DZ/path"
gen_files(exe, kol_files)
