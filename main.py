x = int(input("Введите число: ")) #вводится число
i = 2 #число на которое будет делиться введённое
k = 0 #флаг
if i < x: # для положительных значений
    while i < x: #цикл выполняется, пока i не станет равна x
        if x % i == 0: # если остаток от деления 0 - число не может быть простым, меняется знач флага
           k = 1 
        i += 1 #
else: # для отрицательных значений
    i = -2
    while i > x: # цикл выполняется, пока i не станет равна x
        if x % i == 0: # если остаток от деления 0 - число не может быть простым, меняется знач флага
           k = 1
        i -= 1
print(("Простое" if k == 0 else "Не простое")) # в зависимости от значения флага выводится результат
