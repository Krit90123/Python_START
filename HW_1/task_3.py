"""
Напишите программу, которая принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Ввод: два значения типа <int>
Вывод: значение типа <int> либо значение типа <str>

Пример:

34
-30
4

2
4
1

-34
0
Точка на отрицательной части оси абсцисс
"""

x = int(input('Введите число x:'))
y = int(input('Введите число y:'))


if x == 0 and y == 0:
    print('Неверные координаты точек ;)')
elif x > 0 and y > 0:
    print(
        f'Четверть 1 ')
elif x < 0 and y > 0:
    print(
        f'Четверть  2 ')
elif x < 0 and y < 0:
    print(
        f'Четверть 3 ')
elif x > 0 and y < 0:
    print(
        f'Четверть 4 ')