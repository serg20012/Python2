# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

from datetime import time, date, datetime
import logging
import argparse


FORMAT = 'дата и время - {asctime}. Ошибка: {msg}'

logging.basicConfig(filename='.\\sem15_DZ\\task4.log', format=FORMAT, style='{', filemode='w',
                    encoding='utf-8', level=logging.INFO)


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
        logging.exception("день недели!")
        return
    try:
        month = int(months.get(month))
    except Exception as e:
        logging.exception("месяц!")
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
        logging.exception("неделя не существует")
        return
    return test_day


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Преобразование текста в дату.')
    parser.add_argument(
        'text', type=str, help='Текст для преобразования в дату.')
    args = parser.parse_args()

    result = convert_date(args.text)
    if result:
        print(result)
    else:
        print("Неверный формат. См. task4.log")


# text = "1-я четвыерг ноября"
# result = convert_date(text)
# if result:
#     print(result)
# else:
#     print("Неверный формат см. task4.log")
