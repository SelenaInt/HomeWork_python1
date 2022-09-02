# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

from calendar import day_name


day_name = int(input('Enter day number (1-7): '))
week = ['Monday', 'Tuesday', 'Wendsday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
if day_name in range(1, 8):
    if day_name in range(1, 6):
        print(week[day_name-1], ' - Its a workday today(')
    else:
        print(week[day_name-1], ' - Your lucky, its a holiday!')
else:
    print('You made a mistake, the number outside 7 days')