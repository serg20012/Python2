# Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# [1,2,3,4,5,6,7, 8, 9,10] номер count
# [0,1,1,2,3,5,8,13,21,34] ряд res
n = int(input('порядковое число из ряда Фибоначчи : '))
# def fib(n: int):
#     num1 = 0
#     num2 = 1
#     res = [0, 1]
#     result = 0
#     count = 2
#     while count < n:
#         result = num1 + num2
#         num1 = num2
#         num2 = result
#         res.append(result)
#         # print(res)
#         count += 1
#     return res
# print(fib(n))


def fib(n: int):
    num1 = 0
    num2 = 1
    res = [0, 1]
    result = 0
    count = 2
    while count < n:
        result = num1 + num2
        num1 = num2
        num2 = result
        count += 1
        yield result
        # print(res)


print(*fib(n))
