import math


class Figure:
    sides_count = 0 # количество сторон

    def __init__(self, color: tuple, *sides: int, filled: bool = True) -> None:
        # Проверка на количество переданных сторон
        if len(sides) != self.sides_count:
            self.__sides = [1 * self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [i for i in self.__color]
    # это генератор списка, который создает новый список, содержащий все элементы из self.__color

    def __is_valid_color(self, r, g, b):
        color_list = [r, g, b]
        color_list.sort()
        if color_list[0] < 0 or color_list[-1] > 255:
            return False
        else:
            return True
    # проверяем, являются ли значения r, g, b (компоненты цвета) допустимыми

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
    # Метод set_color(self, r, g, b) используется для установки нового цвета объекта.

    def __is_valid_sides(self, sides): # Метод используется для проверки, являются ли значения сторон допустимыми
        sides_list = []  # Создается пустой список который удет хранить допуступные значения сторон
        for i in sides:
            if i > 0:
                sides_list.append(i)
        if len(sides_list) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *sides): # Метод используется для установки новых значений сторон объекта
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):  # Метод используется для получения значения приватного атрибута
        return [*self.__sides] # __sides и возврата его в виде списка. Оператор распаковки (*)

    def __len__(self):  # Метод __len__ возвращает сумму всех элементов в __sides.
        return sum(self.__sides)

class Circle(Figure):  #  круг
    sides_count = 1
    __radius = None

    def set_radius(self):  # Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны)
        self.__radius = self.__len__() / (2 * math.pi)
        return self.__radius

    def get_square(self):  # Метод get_square возвращает площадь круга
        self.set_radius()  # (можно рассчитать как через длину, так и через радиус).
        return (self.__radius ** 2) * math.pi


class Triangle(Figure):  # триугольник
    sides_count = 3
    __height = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1 * self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1] ** 3



# Примеры использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
