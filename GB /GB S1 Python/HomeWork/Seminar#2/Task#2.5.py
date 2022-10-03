print(
    '''
    5.Реализуйте алгоритм перемешивания списка.
    '''
)

import random

array = [0, 1, 2 ,3 , 4, 5, 6, 7, 8, 9]
print(array)
for i in range(10):
    temp = array[i]
    index = random.randint(0,9)
    array[i] = array[index]
    array[index] = temp
print(array)