# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint as rnd

a = []
n = int(input("Введите длину списка: "))

for i in range(n):
    a.append(rnd(1, 100))
print(a)

pr = []
if n % 2 == 0:
    for i in range(n//2):
        pr.append(a[i] * a[n-i - 1])
else:
    for i in range(n//2 + 1):
        pr.append(a[i] * a[n-i -1])
print(pr)
