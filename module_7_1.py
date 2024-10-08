
print('Автор: Фролкин Максим')
print()
print('Задача "Учёт товаров"')
print()

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')  # Открывает файл products.txt для чтения
        file_ = file.read()  # Читает все содержимое файла и сохраняет его в переменную file_
        file.close()  # закрытие файла
        return file_  # Возвращает содержимое файла в виде строки

    def add(self, *product):  # Этот метод добавляет новые продукты в файл
        for i in product:
            prod_ = str(i)  # prod_ это переменная принимающая строковое значение
            file = open(self.__file_name, 'r')  # Открывает файл products.txt для чтения
            file_ = file.read()  # Читает все содержимое файла и сохраняет его в переменную file_
            file.close()  # закрытие файла
            if prod_ in file_:  # если продукт prod_ нахотится в file_ то возврат строки
                print(f'Продукт {prod_} уже есть в магазине!')
            else:  # иначе
                file = open(self.__file_name, 'a')  # Открывает файл products.txt для добавления
                file.write(f'{prod_}\n')  # зпись продукта и переход на новую строку
                file.close()  # закрытие файла


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())