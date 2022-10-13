
#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# В тексте используется разделитель пробел.
# - **random.sample**
    
#     Возвращает новый список состоящий из неповторяющихся элементов, выбрано случайным образом.

import random


user_number = int(input('Введите количество слов: '))

def get_offer(user_number):
    word = 'абв'
    result = []
    for i in range(user_number):
        temp = random.sample(word, k = 3)
        result.append(''.join(temp))
    my_list = ' '.join(result)
    return my_list
# .join объединяем список в строку 

def clean_list(arr):
    word = 'абв'
    arr = arr.split(' ')
    for i in arr:
        if word in arr:
            arr.remove(word)
    my_list = ' '.join(arr)
    return my_list

my_list = get_offer(user_number)
print(my_list)
print(clean_list(my_list))
#split разделитель (необязательный параметр) – строка разбивается на части с помощью указанного символа. Если разделитель не задан, то любая пробельная строка (пробел, новая строка и т.д.) считается разделителем;