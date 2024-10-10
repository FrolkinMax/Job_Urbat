print('Автор: Фролкин Максим')
print()
print('Задача "Записать и запомнить"')
print()

def custom_write(file_name, strings):  #---file_name - название файла для записи; strings - список строк для записи
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:  # Файл открывается в режиме записи ('w') с кодировкой utf-8.
        for index, string in enumerate(strings, start=1):
            byte_start = file.tell()  # метод file.tell() для получения текущей позиции в байтах перед записью строки.
            file.write(string + '\n')
            strings_positions[(index, byte_start)] = string
    # Добавление в словарь: В словарь strings_positions добавляется запись с ключом в виде кортежа (index, byte_start),
    # где index — номер строки, а byte_start — позиция начала строки в байтах. Значением является сама строка string.
    return strings_positions

    # for index, string in enumerate(strings, start=1):
    # Итерация: Используется функция enumerate
    # для итерации по списку strings.Функция enumerate возвращает
    # кортежи, где первый элемент — это индекс(начиная
    # с 1, благодаря аргументу start = 1), а второй — сама строка.






info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)