# texts = ["Привет", "ЗДОРОВА", "привеТствую"]
# res = map(lambda x: x.lower(), texts)
# print(*res)

# numbers = [42, -73, 1024]
# res = tuple(filter(lambda x: x > 0, numbers))
# print(res)


# # Определяем функцию, которую будем применять к каждому элементу
# def square(x):
#     return x ** 2

# # Создаем список чисел
# numbers = [1, 2, 3, 4, 5]

# # Применяем функцию square к каждому элементу списка numbers
# result = map(square, numbers)
# print(*result)
# # Итерация по результату
# for item in result:
#     print(item)


# names = ["Иван", "Николай", "Пётр"]
# salaries = [125_000, 96_000, 109_000]
# awards = [0.1, 0.25, 0.13, 0.99]
# for name, salary, award in zip(names, salaries, awards):
#     print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

# my_list = [42, 256, 73]
# print(sum(my_list))
# print(sum(my_list, start=1024))

# data = [25, -42, -146, 73, -100, 12]
# # print(list(map(str, data)))
# # print(max(data, key=lambda x: -x))
# print(*filter(lambda x: not x[0].startswith('__'), globals().items()))
