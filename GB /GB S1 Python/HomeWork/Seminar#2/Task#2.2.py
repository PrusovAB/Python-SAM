print(
    '''
    2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*

  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
    '''
    )

import math
#С помощью встроенной функции 
print('Нахождение факториала ! ')
N=math.factorial(int(input('Введите факториал N: ')))
print('Факториал: ',N)


num = int(input('Введите факториал N: '))
factorial1 = 1
 
if(num%1==0 and num>=0):
    # Вычисляем факториал числа num
    for i in range(1, num+1):
        factorial1 = i*factorial1
        print(factorial1,sep='*') #sep не работает? почему ? 
    # Выводим результат на экран
    print(f'\n{num}! = {factorial1}')
# Если num - отрицательное или нецелое число, выводим сообщение об ошибке
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')