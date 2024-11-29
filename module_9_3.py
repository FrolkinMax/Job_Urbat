print()
print('\033[36;4mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36;4mЗадача "Генераторные сборки"\033[0m','\n')
#Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.

# Задача:
# Дано 2 списка:

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Решение:
first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример выполнения кода:
print(list(first_result))
print(list(second_result))
# Вывод в консоль:
# [1, 2]
# [False, False, True]
