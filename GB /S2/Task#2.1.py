#Найти среднее арифметическое среди всех элементов массива.
print('Задание №2.1\nНайти среднее арифметическое среди всех элементов массива.')

a1=int(input('Введите элемент массива: '))
b2=int(input('Введите элемент массива: '))
c3=int(input('Введите элемент массива: '))
d4=int(input('Введите элемент массива: '))

element=(a1,b2,c3,d4)

print('Среднее арифметическое среди всех элементов массива = ',sum(element)/len(element))
input('\nНажмите Enter для завершения программы')
# sum - Вычисляет сумму всех элементов в последовательности
# len - считает кол-во элементов
