# ✔ Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.
bag = {'нож': 5, 'рюмка': 3,
       'бутылка': 2, 'закуска': 4,
       'тарелка': 2, 'вода': 6,
       'подушка': 8, 'стул': 8,
       'вилка': 5, 'палатка': 7}
in_bag = int(input("введите вместимость bag"))
# in_bag = 10
want_in = 0
bagspam = bag
# подсчет всех вещей
for key, val in bag.items():
    want_in = want_in + val
print(
    f'вместимость рюкзака {in_bag}, а вес вещей {want_in}')
temp = want_in
# print(val)

while want_in > in_bag:
    print('вес вещей больше чем рюкзак, будем выкидывать лишнее по макс весу')
    max_val = max(bag.values())
    # print(max_val)
    for key, val in bag.items():
        # print("хочу -", want_in)
        # print("факт -", temp)

        if max_val == val:
            # print(f'выкинули {key}, весом {val}')
            bag.pop(key)
            want_in -= max_val
            # print(f'стало: вес вещей {want_in}')
            break
else:
    print(
        f'вместимость рюкзака {in_bag}, а вес вещей {want_in}')
print(bag)
