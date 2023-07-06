# data = [2, 4, 6, 8, 10, ]
# print(*data, sep='\t')

# data = [2, 4, 6, 8, 10, ]
# for item in data:
#     print(item, sep='\t')

# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e)

# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)

# data = {2, 4, 4, 6, 8, 10, 12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1, res2, res3, sep='\n')


# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result


# for i, num in enumerate(factorial(1000), start=1):
#     print(f'{i}! = {num}')

# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         # input()
#         yield number


# for i, num in enumerate(factorial(1000), start=1):
#     print(f'{i}! = {num}')

def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }')
