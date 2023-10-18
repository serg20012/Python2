# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from main4 import create


def gen_files(extensions, num_files_per_extension):
    for i in range(len(extensions)):
        extension = extensions[i]
        num_files = num_files_per_extension[i]
        create(extension, max_fales=num_files)


# Пример использования
exe = ["txt", "doc", "pdf"]
kol_files = [3, 2, 5]  # Количество файлов для каждого расширения
gen_files(exe, kol_files)
