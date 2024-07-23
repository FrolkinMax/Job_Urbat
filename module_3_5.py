def get_multiplied_digits(number):
    # Преобразуем число в строку для легкого доступа к цифрам
    str_number = str(number)
    
    # Получаем первую цифру числа и преобразуем её в целое число
    first = int(str_number[0])
    
    # Если длина строки больше 1, выполняем рекурсивный вызов для оставшихся цифр
    if len(str_number) > 1:
        # Рекурсивно вызываем функцию для оставшихся цифр и умножаем на первую цифру
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем единственную цифру
        return first

# Пример выполнения функции
result = get_multiplied_digits(40203)
print(result)  
