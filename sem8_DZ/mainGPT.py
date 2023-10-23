import os
import json
import csv
import pickle


def info_dir(directory_path):
    result = []
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(directory_path):
        dir_info = {
            "path": dirpath,
            "type": "directory",
            "size": 0  # Размер директории будет заполнен позже
        }

        # Рассчитываем размер директории с учетом всех файлов и поддиректорий
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            dir_info["size"] += os.path.getsize(file_path)
            total_size += os.path.getsize(file_path)

        # Сохраняем информацию о файлах в текущей директории
        file_info = []
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_info.append({
                "path": file_path,
                "type": "file",
                "size": os.path.getsize(file_path)
            })

        dir_info["files"] = file_info
        result.append(dir_info)
        print(dir_info)

    # Сохраняем результаты в json
    with open("result.json", "w") as json_file:
        json.dump(result, json_file, indent=4)

    # # Сохраняем результаты в csv
    # with open("result.csv", "w", newline="") as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow(["Path", "Type", "Size"])
    #     for item in result:
    #         csv_writer.writerow([item["path"], item["type"], item["size"]])

    # # Сохраняем результаты в pickle
    # with open("result.pkl", "wb") as pickle_file:
    #     pickle.dump(result, pickle_file)

    return total_size


# Пример использования

info_dir('.\sem8_DZ')
