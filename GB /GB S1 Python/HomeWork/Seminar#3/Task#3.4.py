
print(
    '''
    4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
    '''
)
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input())
# f = bin(a)
# print(f)


a = int(input('Введите число '))
b = ''
while a > 0:
    b = str(a%2) + b
    a = a // 2
print(b)

input("\n\nНажмите Enter чтобы выйти.")