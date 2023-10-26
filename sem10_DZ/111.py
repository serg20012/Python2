class Animal:
    def __init__(self, name, specific_property):
        self.name = name
        self.specific_property = specific_property


class AnimalFactory:
    def create_animal(self, animal_type, name, specific_property):
        if animal_type == 'Fish':
            return Fish(name, specific_property)
        elif animal_type == 'Bird':
            return Bird(name, specific_property)
        elif animal_type == 'Grass':
            return Grass(name, specific_property)
        else:
            raise ValueError('Invalid animal type')


# Пример использования
animal_factory = AnimalFactory()

fish = animal_factory.create_animal('Fish', 'Акула', 'треугольный плавник')
bird = animal_factory.create_animal('Bird', 'vorobey', 'прямые крылья')
grass = animal_factory.create_animal('Grass', 'sosna', 'зеленая хвоя')

print(fish.name, fish.specific_property)
print(bird.name, bird.specific_property)
print(grass.name, grass.specific_property)
