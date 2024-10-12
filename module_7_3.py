print('Автор: Фролкин Максим')
print()
print('Задача "Найдёт везде"')
print()

import re

class WordsFinder:  # Создание класса
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}  # Создается пустой словарь, который будет хранить слова из файлов.
        punctuation = r"[',.=!?;:\s\-]"  # Определяет шаблон для замены всех символов пунктуации и пробелов.

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Преобразует строку в нижний регистр, для нечувствительности к регистру
                text = re.sub(punctuation, ' ', text)  # Заменяет все символы пунктуации и пробелы на один пробел.
                words = text.split()  # Разбивает текст на слова, используя пробел как разделитель
                all_words[file_name] = words  # Добавляет список слов в словарь all_words с ключом, равным имени файла.

        return all_words  # Возвращает словарь all_words, содержащий слова из всех файлов.

    def find(self, word):
        word = word.lower()  # Преобразует искомое слово в нижний регистр для нечувствительности к регистру.
        result = {}  # Создается пустой словарь, который будет хранить результат подсчета.

        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word)  # Добавляет в словарь result ключ, равный имени файла, и значение,
                # равное индексу первого вхождения слова в списке слов.

        return result

    def count(self, word):
        word = word.lower()  # Преобразует искомое слово в нижний регистр для нечувствительности к регистру.
        result = {}  # Создается пустой словарь, который будет хранить результат подсчета.

        for name, words in self.get_all_words().items():  # Итерируется по парам ключ-значение в словаре, возвращаемом методом
            result[name] = words.count(word)  # Добавляет в словарь result ключ, равный имени файла, и значение,
            # равное количеству вхождений слова в списке слов.

        return result

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # 3 слово по счёту
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего


# def get_all_words(self):
#     all_words = {}  # Создается пустой словарь, который будет хранить слова из файлов
#     split = ''  # Создается пустая строка, для сбора всех строк из файла после обработки.
#     execute = [',', '.', '=', '!', '?', ';', ':', ' - ']  # Список символов, которые заменим на пробелы.
#     with open(self.file_names, encoding='utf-8') as file:
#         for line in file:  # Итерируется по каждой строке в файле
#             line = line.lower()  # Преобразует строку в нижний регистр, елаем поиск нечувствительным к регистру.
#             for i in line:  # Итерируется по каждому символу в строке.
#                 if i in execute:  # Проверяет, является ли символ одним из символов пунктуации.
#                     line = line.replace(i, ' ')  # Заменяет символ пунктуации на пробел.
#             split = split + line  # Добавляет обработанную строку к переменной split.
#         all_words.update({self.file_names: split.split()})  # Добавляет обработанную строку к переменной split.
#     return all_words  # Разбивает собранную строку split на слова с помощью метода split() и обновляет словарь
# #  all_words, добавляя ключ self.file_names и значение — список слов.
#
# # with open(self.file_names, encoding='utf-8') as file: Открывает файл с именем, хранящимся в self.file_names,
# # в режиме чтения с кодировкой UTF-8. Оператор with обеспечивает автоматическое закрытие
# # файла после выполнения блока кода.