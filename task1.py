# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint as rnd
n = int(input("Введите размер списка: "))
a = []
s = 0
for i in range(n):
    a.append(rnd(1, 100))
print(a)
for i in range(n):
    if i % 2 == 1:
        s = s + a[i]
print(s)



