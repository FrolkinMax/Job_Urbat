# Задача "Нужно больше этажей":

# 1__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2 Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения
# по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3 __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4 __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

class House:  # класс
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # метод подъема на этаж
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):  # new_floor + 1 т.к. иначе будет подъем не включая указанный этаж
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):  # возвращаем количество этажей
        return (self.number_of_floors)

    def __str__(self):  # возвращаем строку "Название: <название>, кол-во этажей: <этажи>".
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}.")

    def __eq__(self, other): # оператор для сравнения равенства этажей
        return int(self.number_of_floors) == other

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        return House(self.name, self.number_of_floors + value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__