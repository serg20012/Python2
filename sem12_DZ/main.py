# Задание
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv


class NameDescriptor:
    def __set__(self, instance, value):
        print(value)
        if value.istitle() and value.isalpha():
            instance._name = value
        else:
            raise ValueError("Неверный формат имени")

    def __get__(self, instance, owner):
        return instance._name


class Student:
    name = NameDescriptor()

    def __init__(self, name, subject, grade, test_result):
        self.name = name
        self.subject = subject
        self.grade = grade
        self.test_result = test_result

    def save_to_csv(self):
        with open(f'.\sem12_DZ\subjects.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                [self.name, self.subject, self.grade, self.test_result])

# Пример использования


student1 = Student("Петров", "Math", 4, 80)
# student2 = Student("Анна Иванова", "History", 5, 90)


student1.save_to_csv()
# student2.save_to_csv()

print("Результаты студентов сохранены в файл .csv")
