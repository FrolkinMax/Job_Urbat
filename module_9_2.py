print()
print('\033[36mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36mЗадача "Списковые, словарные сборки"\033[0m','\n')
# Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач

# Дано:
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Выполнение:
first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}

# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)