# Задача "Съедобное, несъедобное":
# Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
# Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?
# Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.
# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
# Пункты задачи:
# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.
# Создайте объекты этих классов.


# Краткое описание:
# Класс Animal: Базовый класс для всех животных. Содержит атрибуты:
# alive = True — животное живо.
# fed = False — животное голодно.
# name — имя конкретного животного.
# Класс Plant: Базовый класс для всех растений. Содержит атрибуты:
# edible = False — растение по умолчанию несъедобное.
# name — имя конкретного растения.
# Классы-наследники:
# Mammal (млекопитающее) и Predator (хищник) наследуются от класса Animal. Каждый из них имеет метод eat(self, food),
# который проверяет, съедобно ли переданное растение, и в зависимости от этого изменяет состояние животного.
# Flower (цветок) и Fruit (фрукт) наследуются от класса Plant. У фруктов переопределён атрибут edible на True.
print('Задача "Съедобное, несъедобное"')
# 2 класса родителя: Animal, Plant
class Animal:
    # Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
    # name - индивидуальное название каждого животного.
    def __init__(self, name):
            self.name = name  # Индивидуальное имя животного
            self.alive = True  # живой
            self.fed = False   # голодный

class Plant:
    # Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
    def __init__(self, name):
        self.name = name  # Индивидуальное имя растения
        self.edible = False  # не съедобно
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.

# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):

    def __init__(self, name):
        super().__init__(name) # Используем инициализацию базового класса Plant

class Fruit(Plant):
    # У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
    def __init__(self, name):
        super().__init__(name) # Используем инициализацию базового класса Plant
        self.edible = True # Фрукты съедобны


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

# Объяснение:
# Классы Animal и Plant: Базовые классы, содержащие общие атрибуты для всех животных и растений соответственно.
# Классы Mammal и Predator: Наследуются от Animal, содержат метод eat(self, food), который проверяет,
# съедобно ли растение. Если съедобно — животное насыщается, если нет — умирает.
# Классы Flower и Fruit: Наследуются от Plant. У фруктов переопределён атрибут edible на True, что делает их съедобными.
# Пример выполнения: Хищник (a1) пытается съесть несъедобный цветок (p1), в результате он умирает.
# Млекопитающее (a2) съедает съедобный фрукт (p2) и становится сытым.
