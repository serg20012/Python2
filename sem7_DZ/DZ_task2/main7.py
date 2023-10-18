# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео,
# изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли
# для сортировки.
import os
import shutil


def sort_files(directory):
    image_extensions = ('.jpg', '.jpeg', '.png')
    text_extensions = ('.txt', '.doc', '.docx',)

    os.makedirs(os.path.join(directory, 'text'), exist_ok=True)
    os.makedirs(os.path.join(directory, 'img'), exist_ok=True)

    for filename in os.listdir(directory):

        if filename.endswith(text_extensions):
            scr = os.path.join(
                os.getcwd(), 'sem7_DZ', 'path_DZ_7', filename)
            dst = os.path.join(os.getcwd(), 'sem7_DZ',
                               'path_DZ_7', 'text', filename)
            os.replace(scr, dst)
        elif filename.endswith(image_extensions):
            scr = os.path.join(
                os.getcwd(), 'sem7_DZ', 'path_DZ_7', filename)
            dst = os.path.join(os.getcwd(), 'sem7_DZ',
                               'path_DZ_7', 'img', filename)
            os.replace(scr, dst)
        else:
            # Если файл не подходит ни под одно расширение, оставляем его в исходной директории
            continue

        print(f"Файл {filename} был перемещен в соответствующую директорию.")


# Пример использования
directory_path = "./sem7_DZ/path_DZ_7"
sort_files(directory_path)
