k = int(input("Введите число: "))
a = [1, 0, 1]

for i in range(3, k + 2):
    a.append(a[i - 1] + a[i - 2])

for i in range(2, k + 1):
    a.insert(0, a[1] - a[0])
print(a)