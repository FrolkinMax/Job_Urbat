from threading import Thread
from time import sleep, time

print()
print('\033[36;4mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36;4mДомашнее задание по теме "Введение в потоки".\033[0m','\n')


def wite_words(word_count, file_name):
    with open(file_name, mode='w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        set_time = round(end_time - start_time, 2)
        print(f'Работа потоков: {set_time} секунд(ы)')
    return wrapper

@timing
def first_words():
    wite_words(10, 'example1.txt')
    wite_words(30, 'example2.txt')
    wite_words(200, 'example3.txt')
    wite_words(100, 'example4.txt')

@timing
def second_words():
    thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
    thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
    thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
    thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

    thr_1.start()
    thr_2.start()
    thr_3.start()
    thr_4.start()

    thr_1.join()
    thr_2.join()
    thr_3.join()
    thr_4.join()

print('Один поток:')
first_words()
print()
print('Четыре потока:')
second_words()
print()
