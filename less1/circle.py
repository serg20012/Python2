num = float(input("введите число "))
# count = 0
# while count < num:
#     print(count)
#     count += 2
STEP = 2
limit = num - STEP
count = -STEP
# print(count)
while count < limit:
    count += STEP
    print(count)
    if count % 12 == 0:
        continue
    print(count, " !")

# count += STEP
# print(count)
