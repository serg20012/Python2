# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def func_my(**kwargs):
    result = {}
    for key, value in kwargs.items():
        print(value)
        try:
            hash(value)
        except TypeError:
            value = str(value)
        result[value] = key
    return result


print(func_my(name="Ivan", aqe=42, zp=50_000, child=['pety', 'lisa', 'sveta']))
