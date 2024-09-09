class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        if cls.houses_history is []:
            cls.houses_history = super().__new__()
        cls.houses_history.append(args[0])

        return object.__new__(cls)


    def __init__(self, name, number_of_floors, *args, **kwargs):
        self.name = name
        self.number_of_floors = number_of_floors
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


# Давайте разберём этот код по частям, чтобы понять, как он работает.
#
# 1. Определение класса House
# python
# Копировать код
# class House:
#     houses_history = []
# houses_history — это атрибут класса House, представляющий собой список. Этот список предназначен для хранения истории
# всех созданных объектов House.
#
# 2. Метод __new__
# python
# Копировать код
# def __new__(cls, *args, **kwargs):
#     if cls.houses_history is []:
#         cls.houses_history = super().__new__()
#     cls.houses_history.append(args[0])
#
#     return object.__new__(cls)
# __new__ — это специальный метод, который вызывается перед созданием нового экземпляра класса.
# Именно здесь выделяется память для объекта.
# if cls.houses_history is []: — проверка на то, пуст ли список houses_history. Этот код имеет логическую ошибку,
# поскольку проверка is [] сравнивает, ссылается ли объект на тот же самый список в памяти, а не проверяет на пустоту.
# Для правильной проверки нужно использовать if not cls.houses_history:.
# cls.houses_history = super().__new__() — попытка заменить список houses_history новым объектом.
# Это некорректное использование super().__new__(), так как метод должен вызывать создание объекта, а не замену списка.
# Этот код, вероятно, не выполняет задуманную функцию.
# cls.houses_history.append(args[0]) — добавление имени дома в список houses_history. args[0] — это первый аргумент,
# переданный в конструктор, т.е. name дома.
# return object.__new__(cls) — вызов базового метода __new__, который создаёт новый экземпляр класса House.
# Возвращается экземпляр класса House.
#
# 3. Метод __init__
# python
# Копировать код
# def __init__(self, name, number_of_floors, *args, **kwargs):
#     self.name = name
#     self.number_of_floors = number_of_floors
#     self.args = args
#     self.kwargs = kwargs
# __init__ — это инициализатор, который вызывается после создания объекта.
# Здесь происходит инициализация атрибутов объекта.
# self.name = name — присваивание имени дома атрибуту объекта name.
# self.number_of_floors = number_of_floors — присваивание числа этажей атрибуту объекта number_of_floors.
# self.args = args и self.kwargs = kwargs — сохраняются дополнительные позиционные и именованные аргументы.
#
# 4. Метод __del__
# python
# Копировать код
# def __del__(self):
#     print(f'{self.name} снесён, но он останется в истории')
# __del__ — это деструктор, который вызывается при удалении объекта. Здесь выводится сообщение о том, что дом был
# снесён, но его имя остаётся в истории.
#
# 5. Пример использования класса House
# python
# Копировать код
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
# Создаются три объекта класса House, каждый из которых добавляет своё имя в список houses_history.
# После создания каждого объекта выводится текущий список houses_history.
# 6. Удаление объектов
# python
# Копировать код
# del h2
# del h3
#
# print(House.houses_history)
# Удаляются два объекта h2 и h3. Деструктор __del__ выводит сообщение об удалении домов. Однако, несмотря на это,
# список houses_history остаётся неизменным, так как удаление объектов не очищает историю.
# Итоговый вывод
# Этот код демонстрирует механизм создания объектов с историей. Основная идея заключается в том,
# чтобы отслеживать все созданные дома и сохранять их имена в списке houses_history. Однако,
# есть несколько логических ошибок, в том числе неправильная проверка пустоты списка
# и некорректное использование super().__new__().