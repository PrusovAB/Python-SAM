print(
    '''
    3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
*Пример:*

- Для n = 6:
    [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
    Сумма чисел = 14.0717
    '''
)

def sequenceСalculation(n):
    res = {i:round((1 + 1 / i)**i, 2) for i in range(1, n+1)}
    return res

n = int(input("Введите число N: "))

print(sequenceСalculation(n))