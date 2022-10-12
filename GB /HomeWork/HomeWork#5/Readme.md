
![image](https://user-images.githubusercontent.com/106627508/194627608-8c05f444-1c76-4cd3-a7a3-571ae623bf86.png)


# HOMEWORK # 5
### Входные и выходные данные хранятся в отдельных текстовых файлах.
## 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
```python
#Входные и выходные данные хранятся в отдельных текстовых файлах.
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
```

## 2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""

```python

```
## 3. Создайте программу для игры в ""Крестики-нолики"".

```python

```

## 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

```python
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
import codecs
path_file = input('Введите имя исходного файла: ')

path_encode = input('Введите имя файла для RLE кодирования: ')

def RLE_coding(path_file, path_encode):
    with open(path_file, 'r', encoding='utf-8') as my_f1:
        lines = my_f1.readlines()
        for line in lines:
            for_coding = line.strip()
            with open(path_encode, 'a', encoding='utf-8') as my_f2:
                i = 0
                encode = ''
                while i < len(for_coding):
                    count = 1
                    while i + 1 < len(for_coding) and for_coding[i] == for_coding[i + 1]:
                        count += 1
                        i += 1
                    encode += str(count) + for_coding[i]
                    i += 1
                for i in range(len(encode)):
                    my_f2.write(f'{encode[i]}')
                my_f2.write('\n')

def RLE_decoding(path_encode):
    decode = ''
    count = ''
    with open(path_encode, 'r', encoding='utf-8') as my_f1:
        lines = my_f1.readlines()
        for line in lines:
            for_decoding = line.strip()
            for char in for_decoding:
                if char.isdigit():
                    count += char
                else:
                    decode += char * int(count)
                    count = ''
            print(decode)
            decode = ''


RLE_coding(path_file, path_encode)
RLE_decoding(path_encode)

- open
    
    # ```python
    # #что бы открыть и прочитать файл спользуем фунцию open 
    # file = open('my_file.txt') #открывет файл на чтение
    # #открывает файл my_file.txt
    # print(file.read()) # прочитает файл и выведет на экран 
    # #Но будет выводится что то нечитаемое из за неправильной кодировки, 
    # #Решает проблему присвоение кодировки - **encoding='utf-8'**
    # # Пример 
    # file = open('my_file.txt', encoding='utf-8')
    # print(file.read())
    # >>> Читаемый текст
    # ```
    
    # | file.speek(0) | Прочитывает файл с начала |
    # | --- | --- |
    # | file.readline() | по умолчанию выводит первую сточку файла |
    # | file.readlines() |  выводит весь текст из файла в одну строку |
    # | file.close() | ОБЯЗАТЕЛЬНО! - закрывает файл после использования! |
    
    # ```python
    # #перебрать файл построчно 
    # file = open('my_file.txt', encoding='utf-8')
    # for line in file:
    #     print(line,end='')
    # ```
```

Входные и выходные данные хранятся в отдельных текстовых файлах.

## 5. Создайте программу для игры в "Крестики-нолики".

```python

```
## 6. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

```python

```
