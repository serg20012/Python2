# list1 = [1, 3, 5, 3, 5, 6, 8, 9, 00, 8, 7, 5]
# # list1.sort()
# print(list1.extend([333, 444]))
# print(list1.sort(reverse=True))
# # res = sorted(list1)
# print(list1)
# # print(res)
# print(f'{{Фигурные скобки}} и {{name}}')

# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}')

# data = [3254, 436431453211, 43465474, 2342, 462256, 1747]

# for item in data:
#     print(f'{item:>10}')

# num = 2 * pi * data[1]
# print(f'{num = :_}')
# print(f'{num = }')

# text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text)
# help(str.endswith)
# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>13}')

# d = tuple(range(3))
# print(d, sep='\n')

# my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
# # print(my_tuple[2:6:2])
# # print(my_tuple[-3])
# # print(my_tuple.count(2))
# # print(f'{my_tuple = }')
# print(my_tuple.index(2, 2))
# print(type(my_tuple))

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.setdefault('five')
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# new_spam = my_dict.setdefault('two')
# print(f'{new_spam=}\t{my_dict=}')
# new_eggs = my_dict.setdefault('one', 1_000)
# print(f'{new_eggs=}\t{my_dict=}')
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# # print(my_dict.items())

# for key, value in my_dict.items():
#     print(f'{key = } значение до 100 - {100 - value}')
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)
help(list)