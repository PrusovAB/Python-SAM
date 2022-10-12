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