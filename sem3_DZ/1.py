# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list1 = [1, 35, 6, 7, 4, 3, 2, 2, 3, 5, 6, 7, 6]
list2 = []
for i in list1:
    spam = list1.count(i)
    if spam == 2:
        if i not in list2:
            list2.append(i)
print(list2)
