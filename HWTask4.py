# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

nnumber = int(input('Введите номер четверти (1-4): '))
if nnumber < 1 or nnumber > 4: print('Вы вышли из диапазона')
elif nnumber == 1: print('x > 0 and y > 0')
elif nnumber == 2: print('x < 0 and y > 0')
elif nnumber == 3: print('x < 0 and y < 0')
elif nnumber == 4: print('x > 0 and y < 0')
