
print(
    '''
     1. Вычислить число c заданной точностью d
пример 
d = 0.001, π = 3.141 10-1 <= d <= 10-10
    '''
)

from cmath import pi

d = int(input('Введите точность числа Пи '))
print(f'Число Пи с заданной точностью {d} равно {round(pi,d)}')