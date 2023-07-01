# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

sum = 0
make = 0
count = 0  # для доп комиссии 3%
PERCENT_bank_crime = 1.5
PERCENT_more_bank_crime = 3
PREDEL_min_bank_crime = 30
PREDEL_max_bank_crime = 600
history = []


def input_mon():
    global sum, count, history, more_bank_crime
    plus = int(
        input("введите сумму пополнения кратную 50: "))
    if plus % 50 == 0 and plus > 0:
        if count == 3:
            more_bank_crime = plus / 100 * PERCENT_more_bank_crime
            count = -1
        sum = sum + plus - more_bank_crime
        # print (plus, more_bank_crime)
        count = count + 1
        history.append("пп")
    else:
        print("введена неверная сумма")


def take_mon():
    global sum, count,history, more_bank_crime
    minus = int(input("введите сумму снятия: "))
    bank_crime = minus / 100 * PERCENT_bank_crime
    if bank_crime < PREDEL_min_bank_crime:
        bank_crime = PREDEL_min_bank_crime
    if bank_crime > PREDEL_max_bank_crime:
        bank_crime = PREDEL_max_bank_crime
    if count == 3:
        more_bank_crime = minus / 100 * PERCENT_more_bank_crime
        if sum >= minus + bank_crime + more_bank_crime:
            count = -1
            sum = sum - minus - bank_crime - more_bank_crime
            print(minus, bank_crime, more_bank_crime)
            count = count + 1
            history.append("сн")
        else:
            print("выводимая сумма с  учетом комиссии больше чем сумма на счете")
    elif sum >= minus + bank_crime:
        sum = sum - minus - bank_crime
        print(minus, bank_crime)
        count = count + 1
        history.append("сн")
    else:
        print("выводимая сумма с  учетом комиссии больше чем сумма на счете")


while make != 3:
    print("сумма на счете: ", sum,
          " кол-во операций: ", count,
          " история операций:", history)
    bank_crime = 0
    more_bank_crime = 0
    if sum > 5_000_000:
        sum = sum - sum / 100 * 10
        print("сумма на счете более 5 млн. отняли 10% Итого: ", sum)
    make = int(input("пополнить -1, снять - 2, выйти -3: "))
    if make == 1:
        input_mon()
    elif make == 2:
        take_mon()