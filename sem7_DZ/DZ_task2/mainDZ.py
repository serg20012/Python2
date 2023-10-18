# Задание
# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os


def gr_name(namedst, num, exescr, exedst, stname, endname, dir):
    num_name = 0  # начало счетчика для номера файла

    for filename in os.listdir(dir):
        if filename.endswith(exescr):  # проверка на подходимость по расширению
            # забираем только имя, без расширения
            name_0 = filename.split(".")[0]
            # первая часть имя
            name_0 = name_0[stname-1:endname]

            num_name += 1  # формируем порядковый номер
            # из порядкового номера делаем вторую часть имя
            name_1 = formir_num(num_name, num)
            # итоговое имя файла
            newname = name_0 + name_1 + namedst + "." + exedst

            old_path = os.path.join(dir, filename)
            new_path = os.path.join(dir, newname)
            os.rename(old_path, new_path)
            print(f"Файл {filename} переименован в {newname}")
            print(newname)
            print(filename)


def formir_num(x: int, y) -> str:
    num_str = str(x)
    num_digits = len(num_str)
    # print(f"Количество знаков в числе {x}: {num_digits} а надо {y}")
    while y > num_digits:
        x = str(x)
        x = "0"+x
        num_digits += 1
        # print(x, num_digits)
        # input()
    return x


# Пример использования
dir = "./sem7_DZ/path_DZ"
namedst = '_any'
num = 3
exescr = 'txt'
exedst = 'doc'
scrname = 3
endname = 6
print(os.getcwd())
gr_name(namedst, num, exescr, exedst, scrname, endname, dir)

# formir_num(5, 3)
