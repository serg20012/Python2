# Задание №7_2
# Напишите программу, которая принимает две строки 
# вида “a/b” — дробь с числителем и знаменателем. 
# Программа должна возвращать сумму 
# и *произведение дробей. Для проверки своего 
# кода используйте модуль fractions.
import fractions


def simply(a, b):
    # проверка кратности числителя и знаменателя
    if a != b and a > 1 and b > 1:
        if a > b and a % b == 0:
            a //= b
            b = 1
        elif b > a and b % a == 0:
            b //= a
            a = 1
    elif a == b:
        a = 1
        b = 1
    # упрощение числителя и знаменателя 
    c1 = min(a,b)
    for i in range(2, c1//2+1):
        if a%i ==0 and b%i ==0:
            a=a//i
            b=b//i
    return a, b
drobi1 = input("Введите дробь a/b: ")
drobi2 = input("Введите дробь a2/b2: ")

a, b = map(int, drobi1.split("/"))
a2, b2 = map(int, drobi2.split("/"))

sum_test = fractions.Fraction(a, b) + fractions.Fraction(a2, b2)
prosv_test = fractions.Fraction(a, b) * fractions.Fraction(a2, b2)
print(sum_test)
print(prosv_test)

a, b = simply(a, b)
a2, b2 = simply(a2, b2)
# print(a,b)
# print(a2,b2)

sum_chisl = a * b2 + a2 * b
sum_znam = b * b2
sum_chisl, sum_znam = simply(sum_chisl, sum_znam)
print("сумма дробей ", sum_chisl, "/", sum_znam)

prosv_chisl = a * a2
prosv_znam = b * b2
prosv_chisl, prosv_znam = simply(prosv_chisl, prosv_znam)
print("произведение дробей", prosv_chisl, "/", prosv_znam)