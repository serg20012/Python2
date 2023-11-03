# Cоздать CSV файл с тремя студентами (ФИО), названиями предметов,
# название предмета хранит оценку от 2 до 5
# и результат теста от 0 до 100

import csv
import random

# Список предметов
subjects = ["Math", "History", "Physics", "Chemistry"]

# Создаем CSV файл и записываем заголовок
with open(f'.\sem12_DZ\subjects.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Grade", "Test Result"])

    # Заполняем файл случайными данными
    for subject in subjects:
        grade = random.randint(2, 5)
        test_result = random.randint(0, 100)
        writer.writerow([subject, grade, test_result])

print("CSV файл успешно создан.")
