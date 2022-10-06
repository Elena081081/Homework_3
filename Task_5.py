# <Задание 5>
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

def fib1(n):
    if n in [1, 2]:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
k = int(input('Введите число k: '))
for el in range(1, k + 1):
    list.append(fib1(el))
    list.insert(0, fib2(el))
print(f'Список чисел Фибоначчи: {list}')
