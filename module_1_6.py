
print()
print('\033[36;4mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36;4mПрактическая работа по уроку "Организация программ и методы строк"\033[0m','\n')

my_string = input('Введите произвольный текст: ')  # вод для примера: Организация программ и методы строк

print(f'{my_string}, {len(my_string)} - это длина строки')
print()
print(my_string.upper())  # в верхнем регистре
print(my_string.lower())  # в нижнем регистре
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])

