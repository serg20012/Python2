# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

path_my = r"C:\Users\Dom-1floor\Documents\GB\Python2\less3\main.py"


def my_split(path: str) -> tuple:
    path1, name_full = path.rsplit("\\", 1)
    # print("1", path1)
    # print(name_full)
    name, ext = name_full.split(".")
    # print(name)
    # print(ext)
    my_dict = (path1, name, ext)
    return my_dict


print(my_split(path_my))
