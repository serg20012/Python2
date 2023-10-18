# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 5
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random as rnd

letters = "qwertyuiopasdfghjklzxcvbnm"


def create(exe, min_dlin=6, max_dlin=30, min_infa=256, max_infa=4096, max_fales=5):
    for i in range(1, max_fales+1):  # цикл на кол-во файлов
        file_name = ""
        # генерерация длины имени файла
        name_len = rnd.randint(min_dlin, max_dlin)
        for _ in range(name_len):  # цикл на генерацию имя файла по длине
            # print(name_len)
            let = rnd.choice(letters)
            # print(type(let))
            file_name = file_name + let
            # print(let)
            # print(file_name)
            # input()
        file_name = file_name+"."+exe  # присоединение переадного расширения "exe" к имени
        # print(file_name)
        with open(file_name, 'wb') as f1:  # создание файла
            for _ in range(min_infa, max_infa):  # генерация информации в файл
                #    случайное количество байт
                num_bytes = rnd.randint(min_infa, max_infa)

                random_data = bytes([rnd.randint(0, 255)
                                    for _ in range(num_bytes)])
                f1.write(random_data)
        print(f"Создан файл: {file_name}")

if __name__ == '__main__':
    create("txt")
