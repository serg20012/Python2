# from typing import Callable


# def main(x: int) -> Callable[[int], dict[int, int]]:
#     d = {}

#     def loc(y: int) -> dict[int, int]:
#         for i in range(y):
#             d[i] = x ** i
#         return d

#     return loc


# small = main(42)
# big = main(73)
# print(small(7))
# print(big(7))
# print(small(3))


import random
from typing import Callable


def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 10) = }')
