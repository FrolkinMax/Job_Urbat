print()
print('\033[36mАвтор: Фролкин Максим\033[0m','\n')
print('\033[36mЗадача "Вызов разом"\033[0m','\n')


def apply_all_func(int_list, *functions):
    results = {}
    for functions_ in functions:
        results[functions_.__name__] = functions_(int_list)
    return results


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))






