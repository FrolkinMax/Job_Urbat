print()
print('\033[36mАвтор: Фролкин Максим\033[0m')
print()
print('\033[36mЗадача "План перехват"\033[0m')
print()

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        set_sum = personal_sum(numbers)
        return set_sum[0] / (len(numbers) - set_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return print(f'В numbers записан некорректный тип данных')
    except:
        if isinstance(numbers, int):
            return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать