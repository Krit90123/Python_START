"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""

number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Ввели неверное число')
elif number > 5:
    print('Выходной!')
else:
    print('Рабочий день!')