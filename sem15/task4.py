# Задание №4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

from datetime import time, date, datetime
import logging

FORMAT = 'дата и время - {asctime}. Ошибка: {msg}'

logging.basicConfig(filename='.\\sem15\\task4.log', format=FORMAT, style='{', filemode='w',
                    encoding='utf-8', level=logging.INFO)
# logging.basicConfig(filename='.\\sem15\\task4.log', filemode='w',
#                     encoding='utf-8', level=logging.INFO)


def convert_date(text):
    months = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12',
    }
    days = {
        'понедельник': '0',
        'вторник': '1',
        'среда': '2',
        'четверг': '3',
        'пятница': '4',
        'суббота': '5',
        'воскресенье': '6',
    }

    week, day_week, month = text.split()
    try:
        day_week = int(days.get(day_week))
    except Exception as e:
        logging.info("день недели!")
        return
    try:
        month = int(months.get(month))
    except Exception as e:
        logging.info("месяц!")
        return
    try:
        week = int(week[0:1])
        if week == 1:
            koef = 0
        elif week == 2:
            koef = 7
        elif week == 3:
            koef = 14
        elif week == 4:
            koef = 21
        elif week == 5:
            koef = 28

        for i in range(1, 8):
            test_day = date(2023, month, i+koef)
            # print(test_day)
            if test_day.weekday() == day_week:
                break
    except Exception as e:
        logging.info("неделя не существует")
        return
    return test_day


text = "1-я четвыерг ноября"
result = convert_date(text)
if result:
    print(result)
else:
    print("Неверный формат см. task4.log")
