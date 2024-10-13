print()
print('\033[36mАвтор: Фролкин Максим\033[0m')
print()
print('\033[36mЗадача "Форматирование строк\033[0m"')
print()


comand1 = '\033[33mМастера кода\033[0m'
comand2 = '\033[32mВолшебники данных\033[0m'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round(((team1_time + team2_time) / tasks_total), 1)
# Использование %:
print('"В команде %s участников: \033[31m%s\033[0m!"' % (comand1, team1_num))
print('"В команде %s участников: \033[31m%s\033[0m!"' % (comand2, team2_num))
print('\033[35m"Итого сегодня в командах участников: %s и %s!"\033[0m' % (team1_num, team2_num))
# Использование format():
print('"Команда {} решила задач: \033[31m{}\033[0m!"'.format(comand1, score_1))
print('"Команда {} решила задач: \033[31m{}\033[0m!"'.format(comand2, score_2))
print('"{} решили задачи за \033[31m{}\033[0m с!"'.format(comand1, team1_time))
print('"{} решили задачи за \033[31m{}\033[0m с!"'.format(comand2, team2_time))
# Использование f-строк:
print(f'\033[36m"Команды решили {score_1} и {score_2} задач."\033[0m')
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'\033[35mПобеда команды {comand1}!\033[0m'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'\033[35mПобеда команды {comand2}!\033[0m'
else:
    result = '\033[35mНичья!\033[0m'
print(result)
