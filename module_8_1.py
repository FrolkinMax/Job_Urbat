print()
print('\033[36mАвтор: Фролкин Максим\033[0m')
print()
print('\033[36mЗадача "Программистам всё можно\033[0m"')
print()

def add_everything_up(a, b):
    # Начинаем блок try, чтобы попытаться выполнить сложение a и b
    try:
        a + b
    # Если возникает исключение TypeError (например, если a и b имеют разные типы),
    # переходим в блок except
    except TypeError:
        # Преобразуем a и b в строки
        a = str(a)
        b = str(b)
        # Возвращаем конкатенацию строк a и b
        return a + b
    # Если исключение не возникло, переходим в блок else
    else:
        # Преобразуем a и b в числа с плавающей точкой (float)
        a = float(a)
        b = float(b)
        # Складываем числа и округляем результат до трех знаков после запятой при помощи функции round
        return round(a + b, 3)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))