# Программа для поиска наибольшего числа!
a = int(input('Введите первое число : '))  # Ввод данных
b = int(input('Введите второе число  : '))
while True:  # Цикл
    if a > b:  # Условие
        print('Большее число:', a)
        break  # Конец цикла
    else:
        print('Большее число:', b)
        break
input("\nНажмите Enter для завершения програмы")  # конец программы
