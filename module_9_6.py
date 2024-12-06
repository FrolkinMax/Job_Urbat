print()
print('\033[36;4mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36;4mДомашнее задание по теме "Генераторы"\033[0m','\n')


def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]

# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)

