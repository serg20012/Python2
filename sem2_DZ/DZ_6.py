# Задание №6
# Напишите программу банкомат. 
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
sum = 0
make = 0
count = 0 # для доп комиссии 3%
PERCENT_bank_crime = 1.5
PERCENT_more_bank_crime =3
PREDEL_min_bank_crime = 30
PREDEL_max_bank_crime = 600
while make !=3:
    print ("сумма на счете: ", sum, " кол-во операций ", count)
    bank_crime = 0
    more_bank_crime = 0
    make = int(input("пополнить -1, снять - 2, выйти -3: " ))
    if sum > 5000000: 
        sum = sum - sum /100 *10
        print (sum)
    if make ==1 : 
        plus = int(input("введите сумму пополнения кратную 50: "))
        if plus %50 ==0 and plus >0:
            if count == 3:
                more_bank_crime = plus / 100 * PERCENT_more_bank_crime 
                count = -1
            sum = sum + plus - more_bank_crime
            # print (plus, more_bank_crime)
            count = count +1 
        else : print ("введена неверная сумма")
    elif make ==2:
        minus = int(input("введите сумму снятия: "))
        bank_crime = minus / 100 *PERCENT_bank_crime
        if bank_crime < PREDEL_min_bank_crime: bank_crime = PREDEL_min_bank_crime
        if bank_crime > PREDEL_max_bank_crime: bank_crime = PREDEL_max_bank_crime
        if count == 3: 
            more_bank_crime = minus / 100 * PERCENT_more_bank_crime
            if sum >= minus + bank_crime + more_bank_crime:
                count = -1
                sum = sum - minus - bank_crime - more_bank_crime
                print (minus, bank_crime, more_bank_crime)
                count = count +1
            else:
                print ("выводимая сумма с  учетом комиссии больше чем сумма на счете") 
        elif sum >= minus + bank_crime:
            sum = sum - minus - bank_crime
            print (minus, bank_crime)
            count = count +1
        else:
            print ("выводимая сумма с  учетом комиссии больше чем сумма на счете")





