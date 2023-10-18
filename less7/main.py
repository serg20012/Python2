# f = open('123.txt', "a", encoding="utf-8")
# f.write("всякая еренда\n")
# f.close()

# f.write("Окончание файла\n")
# f.close()
# # print(f)
# # print(list(f))

# f = open('bin_data', "wb", buffering=64)
# f.write(b'X' * 1200)
# f.close()

# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()

# # f = open('data.txt', 'r', encoding='utf-8')
# # print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode
# # byte 0xec in position 14: invalid continuation byte
# # f.close()

# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(f)
# print(list(f))

# f.close()


# with open('123.txt', 'r+', encoding='utf-8') as f:
#     print(list(f))
# print(f.write('Пока'))  # ValueError: I/O operation on closed file.

# with (open('123.txt', 'r+', encoding='utf-8') as f1,
#         open('bin_data', 'rb') as f2,
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# print(f.write('Пока'))  # ValueError: I/O operation on closed file.

# with (open('123.txt', 'r+', encoding='utf-8') as f1,
#         open('bin_data', 'rb') as f2,
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# text = "Same text test for all1\n"
# with open('123.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
#     print(f'{res = }\n{len(text) = }')

# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(line)
#         print(f'{res = }\n{len(line) = }')

# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f'{res = }\n{len(line) = }')

# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'a', encoding='utf-8') as f:
#     f.writelines("\n".join(text))

# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, file=f)

# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'a', encoding='utf-8') as f:
#     for line in text:
#         print(line, end="***\n##", file=f)

# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'w', encoding='utf-8') as f:
#     print(f.tell())
#     for line in text:
#         res = f.write(f'{line}\n')
#         print(f.tell())
#     print(f.tell())
# print(f.tell())

# last = before = 0
# text = ["Same text test for all1",
#         "two elements for test",
#         "third element forforfor test text",]

# with open('1234.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#         print(f'{last = }, {before}')
#     print(f'{last = }, {before}')
#     print(f'{f.seek(before,0) = }')
#     f.write('\n'.join(text))

# last = before = 0

# with open('1234.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f'{f.seek(before,0) = }')
#     print(f.truncate(35))

# import os
# from pathlib import Path
# print(os.getcwd())
# print(Path.cwd())

# os.mkdir("new1")
# Path("new2").mkdir()


# import os
# from pathlib import Path

# file_1 = os.path.join(os.getcwd(), 'dir1', 'new_file.txt')
# print(f'{file_1 = }\n{file_1}')
# # print(os.path)
# file_2 = Path().cwd() / 'dir' / 'new_file.txt'
# print(f'{file_2 = }\n{file_2}')


# import os
# from pathlib import Path

# print(os.listdir())

# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)

# import os
# from pathlib import Path

# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = }', end='\t')
#     print(f'{os.path.isfile(obj) = }', end='\t')
#     print(f'{os.path.islink(obj) = }', end='\t')
#     print(f'{obj = }')

# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')

# import os
# for dir_path, dir_name, ﬁle_name in os.walk(os.getcwd()):
#     print(f'{dir_path = }\n{dir_name = }\n{ﬁle_name = }\n')

# import os
# from pathlib import Path

# # # os.rename('old_name.py', 'new_name.py')

# # p = Path('new_name.py')
# # p.rename('new_file.py')

# Path('new_file.py').rename('newest_file.py')

# os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))

# old_file = Path('new_name.py')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)
