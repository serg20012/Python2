# Задание
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.
#


class Negative(Exception):
    def __str__(self):
        return 'Отрицательное значение не может быть! '


class Pryme:
    def __init__(self, x, y=None):
        self.x = x
        if y:
            self.y = y
        else:
            self.y = x
        if x < 0 or y < 0:
            raise Negative

    def per(self):
        p = self.x + self.x + self.y + self.y
        return p

    def s(self):
        s = self.x*self.y
        return s


c1 = Pryme(-10, 2)
print(c1.per())
print(c1.s())
