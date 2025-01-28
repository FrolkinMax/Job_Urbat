
print()
print('\033[36;4mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36;4mПрактическая работа по по теме: "Неизменяемые и изменяемые объекты. Кортежи"\033[0m','\n')

immutable_var = 1, 2, 3, [1,2], "raps"
print(immutable_var)
print()
# immutable_var[0] = 200
#print(immutable_var) при попытке внести изменения в кортеж выдается ошибка
# TypeError: 'tuple' object does not support item assignment
# (кортеж является неизменяемой структурой)

mutable_list=[1, 2, "f", "topi"]
print(mutable_list)
mutable_list[3]="poti"
print(mutable_list)



