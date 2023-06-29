text = input("Введите текст: ")

try:
    number = int(text)
    print("Двоичное представление:", bin(number))
    print("Восьмиричное представление:", oct(number))
    print("Шестнадцатиричное представление:", hex(number))
except ValueError:
    if all(ord(char) < 128 for char in text):
        print("Текст написан в ASCII.")
    else:
        print("Текст не написан в ASCII.")
