
# 1 По двум заданным числам проверить является ли одно квадратом второго.
# 2 Найти максимальное из пяти чисел.
# 3 Вывести на экран числа от -N до N.
# 4 Показать первую цифру дробной части числа.

# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

# 6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# 8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.

# 9 Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти.

# 10 Найти расстояние между двумя точками пространства.

# 1 По двум заданным числам проверить является ли одно квадратом второго.
print('1. По двум заданным числам проверить является ли одно квадратом второго.')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a**2 ==b:
    print('Второе квадрат первого')
elif b**2 ==a:
    print('Первое квадрат второго')
else:
    print('Ни одно не является квадратом другого')

# 2 Найти максимальное из пяти чисел.
print('Найти максимальное из пяти чисел.')
A=int(input('Введите данные №1 ==> '))
B=int(input('Введите данные №2 ==> '))
C=int(input('Введите данные №3 ==> '))
D=int(input('Введите данные №4 ==> '))
F=int(input('Введите данные №5 ==> '))
imax=0 #Счетчик 
if B > imax:
    imax=B
if C > imax:
    imax =C
if D > imax:
    imax = D
if A>imax:
    imax = A
if F>imax:
    imax = F
print('Наибольшее число: ',imax)

# 3 Вывести на экран числа от -N до N.

print('# 3 Вывести на экран числа от -N до N.')
number = int(input(" Введите число : "))
number_two = number*-1
for i in range(number_two, number+1):
    print(i)

# 4. Показать первую цифру дробной части числа.
import math
print('4. Показать первую цифру дробной части числа.')
number_Three = float(input("Введите число: "))
rez = number_Three - math.floor(number_Three)
print(math.floor(rez*10))
 
# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

print('5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30')
number_four = int(input("Введите число :"))

if (number_four % 5 == 0 and number_four % 10 == 0 or number_four % 15 == 0) and number_four % 30 != 0:
    print("Кратно")
else:
    print("Не кратно")


# 6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

nymberDay = int(input("ВВедите число от 1 до 7: "))


def number(n):
    if nymberDay == 1:
        print("День недели понедельник день тяжелый идти на работу")
    elif nymberDay == 2:
        print("День недели вторник день тяжелый идти на работу")
    elif nymberDay == 3:
        print("День недели среда день тяжелый идти на работу")
    elif nymberDay == 4:
        print("День недели четверг день тяжелый идти на работу")
    elif nymberDay == 5:
        print("День недели пятница день тяжелый идти на работу")
    elif nymberDay == 6:
        print("День недели суббота Выходной")
    elif nymberDay == 7:
        print("День недели воск-е Выходной")
    else:
        print("Сказали же ввести число от 1 до 7")


number(nymberDay)

# 8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.

a = int(input("введите кординаты X: "))
b = int(input("введите кординаты Y: "))

if a > 0 and b > 0:
    print("1 четверть")
elif a < 0 and b < 0:
    print("3 четверть")
elif a > 0 and b < 0:
    print("4 четверть")
elif a < 0 and b > 0:
    print("2 четверть")
else:
    print("Вы на кординатных осях")

#9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти.



# 10 Найти расстояние между двумя точками пространства.
