# 📌 Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class FabricAnimal:
    def make(self, type_a, name, unuc_property):
        if type_a == 'Fish':
            return Fish(name, unuc_property)
        elif type_a == 'Bird':
            return Bird(name, unuc_property)
        elif type_a == 'Grass':
            return Grass(name, unuc_property)


class Animal:
    def __init__(self, name, unuc_property):
        self.name = name
        self.unuc_property = unuc_property

    def unic(self):
        print(f'{self.name} имеет {self.unuc_property}')


class Fish(Animal):
    def __init__(self, name, unuc_property):
        super().__init__(name, unuc_property)


class Bird(Animal):
    def __init__(self, name, unuc_property):
        super().__init__(name, unuc_property)


class Grass(Animal):
    def __init__(self, name, unuc_property):
        super().__init__(name, unuc_property)


fa = FabricAnimal()
anim1 = fa.make("Fish", "Акула", "треугольный плавник")
print(anim1.name)
anim2 = fa.make("Bird", "воробей", "треугольный плавник")
anim2.unic()


# fish = Fish("Акула", "треугольный плавник")
# bird = Bird("vorobey", "прямые крылья")
# grass = Grass("sosna", "зеленая хвоя")
# print(fish.name)
# fish.unic()

# print(bird.name)
# bird.unic()

# print(grass.name)
# grass.unic()
