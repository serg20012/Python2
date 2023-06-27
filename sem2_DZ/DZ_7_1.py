# Задание №7_1
# Напишите программу, которая получает целое 
# число и возвращает его шестнадцатеричное 
# строковое представление. Функцию hex 
# используйте для проверки своего результата.

data = "0123456789ABCDEF"
x = int(input("Введите число: "))
y = x
res_h = []
while x: 
    ostatok = x % 16
    # print (ostatok)
    if x % 16 > 9:
        ostatok = data [ostatok] 
    # print (ostatok, " > 9")
    res_h.insert(0, ostatok)
    y = y // 16
    if y == 0:
        break

print (*res_h)
print (hex(x))
res_hex = ''.join(str(bit) for bit in res_h)
print (res_hex)