# Задача "История строительства":

# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам
# класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута
# houses_history.
#
# Пример результата выполнения программы:
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
#
# # Удаление объектов
# del h2
# del h3
#
# print(House.houses_history)
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории


class House:  # класс

    houses_history = [] # создаем атрибут согласно задачи

    def __new__(cls, *args, **kwargs):
        if cls.houses_history is []:  # если __instanse ранее не был создан
            cls.houses_history = super().__new__() # тогда мы в этот атребут запишим ссылку на наш класс
        cls.houses_history.append(args[0]) # возврат данной ссылки огласно индексу[0]

        return object.__new__(cls)

    # иначи вывод следующийы  ('ЖК Эльбрус', 10)]
    #                        [('ЖК Эльбрус', 10), ('ЖК Акация', 20)]
    #                        [('ЖК Эльбрус', 10), ('ЖК Акация', 20), ('ЖК Матрёшки', 20)]

    def __init__(self, name, number_of_floors, *args, **kwargs):
        self.name = name
        self.number_of_floors = number_of_floors
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

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

    def __eq__(self, other): # оператор для сравнения равенства этажей с учетом пренадлежности значения к
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    # def __eq__(self, other): # оператор для сравнения равенства этажей без учета принадлежности к классу
    #     return int(self.number_of_floors) == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value): # запись согласно задачи
        return self.__add__(value)

    def __iadd__(self, value): # запись согласно задачи
        return self.__add__(value)

# Пример выполнения программы согласно задачи

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов согласно задачи
del h2
del h3

print(House.houses_history)