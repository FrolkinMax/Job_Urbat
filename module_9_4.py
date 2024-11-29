print()
print('\033[36;4mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36;4mЗадача "Создание функций на лету"\033[0m','\n')

# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
# Задача "Функциональное разнообразие":

# 1) Lambda-функция:
# Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Решение:
print(list(map(lambda x, y: x == y, first, second)))
# func_v1 = lambda list_1, list_2: list_1 == list_2
# result = list(map(func_v1, first, second))

# Пример выполнения кода:
print(result)
# Результат:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# 2) Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            # Записываем каждый элемент из data_set в файл
            for item in data_set:
                file.write(str(item) + '\n')
        # Возвращаем внутреннюю функцию write_everything
    return write_everything

# Пример выполнения кода:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Результат:
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']

# 3) Метод __call__:
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример выполнения кода:
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
