x = int(input("Введите число: "))
i = 2
k = 0
if i < x:
    while i < x:
        if x % i == 0:
           k = 1
        i += 1
else:
    i = -2
    while i > x:
        if x % i == 0:
           k = 1
        i -= 1
print(("Простое" if k == 0 else "Не простое"))