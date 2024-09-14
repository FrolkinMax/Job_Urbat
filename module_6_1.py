# Базовый класс для всех животных
class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Не накормленное
        self.name = name   # Имя животного

# Базовый класс для всех растений
class Plant:
    def __init__(self, name):
        self.edible = False  # Несъедобное по умолчанию
        self.name = name      # Имя растения

# Класс Млекопитающее
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Хищник
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Цветок
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)  # Используем инициализацию базового класса Plant

# Класс Фрукт
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)   # Используем инициализацию базового класса Plant
        self.edible = True       # Фрукты съедобны

# Проверка программы
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод имен животных и растений
print(a1.name)
print(p1.name)

# Проверка атрибутов
print(a1.alive)  # Жив ли Волк с Уолл-Стрит
print(a2.fed)    # Сытость Хатико

# Хищник пытается съесть цветок
a1.eat(p1)
# Млекопитающее ест фрукт
a2.eat(p2)

# Проверка результатов
print(a1.alive)  # Жив ли Волк с Уолл-Стрит после еды
print(a2.fed)    # Сытость Хатико после еды
