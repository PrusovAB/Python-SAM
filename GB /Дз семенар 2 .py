# тут находятся решение домашних заданий первого блока на языке python 

#print('Задание 2.2 \n Нахождение индексов максимального и минимального элемента массива.)
#По блок-схеме 
#Вариант №1
#Тут оба варианта рабочие
numbers=[1,2,3,4,5,6]
size=6
index=1
imax=0
imin=0
while index<size:
    if numbers[index]>numbers[imax]:
        imax=index
    if numbers[index]<numbers[imin]:
        imin=index
    index=index+1
print('Максимальное значение: ',imax,'-----','Минимальное значение: ',imin)

#Вариант №2
#Как бы я решил данную задачу на python
import math
from random import random
print('Задание №2.2\nНахождение индексов максимального и минимального элемента массива')
numbers = []
for j in range(6):
    numbers.append(int(random()*6))
print(numbers)
numbers =sorted(numbers)
print('Минимальный элемент: ' , numbers[0],'Максимальный элемент: ', numbers[-1])
#или Этот вариант 
print(min(numbers),'———',max(numbers))
#Задание 2.3. Развернуть массив, то есть записать все его элементы в обратном порядке. Вывести получившийся массив на экран.
#Вариант №1
#По блок-схеме
print('Задание на «разворот» массива. Нужно перевернуть массив и записать его в обратном порядке.')
size = 10 
a = [0:size-1]
i=0
if i<size/2:
  t=a[i
  a[i]=a[size-1-i]
  a[size-1-i]
  i=i+1
else:
  a[0:size-1]
#Вариант №2
#Как бы я решил данную задачу на python
#В питоне нет массивов там есть списки
print('Задание на «разворот» массива. Нужно перевернуть массив и записать его в обратном порядке.')
list1=[1,54,22,1111,2233,44556,]
print(list1)
list1.reverse()
print(list1)
#Задание 2.4 Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами.
#Как бы я решил данную задачу на python
from random import randint 
print('Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами.')
a = []         
for i in range (20):    
    a.append (randint (1, 100)) 
print ('Массив элементов',a)        
internalsum = 0 
maxim = max(a)
minim = min(a)
print('Максимальная сумма: ',maxim)
print('Минимальная сумма: ',minim)
for i in a:   
    if i<maxim and i>minim:
        internalsum+=i   
print ('Cумма: ', internalsum)
#Вариант №2
a = [randint(1, 100) for i in range(20)]
print(*a)
mn = min(a)
mx = max(a)
print('Минимальная сумма: ', mn)
print('Максимальная сумма: ', mx)
summ = sum(a[min(a.index(mn), a.index(mx)) + 1:max(a.index(mn), a.index(mx))])
print('Сумма'summ)
