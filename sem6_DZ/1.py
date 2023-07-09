# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from date_check import my_data
from sys import argv

user_data = argv[1]
# print(type(user_data))
# print(user_data)
# day, mounth, year = map(int, user_data.split("."))

# user_data = input("BB date d формате DD.MM.YYYY: ")
print(my_data(user_data))
