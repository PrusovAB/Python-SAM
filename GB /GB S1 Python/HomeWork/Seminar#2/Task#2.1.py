print('''
1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
'''
)

def summ_iyogo(n): #Функция с аргументом 
    sum = 0 # Счетчик
    for i in number: # Цикл с пробужкой 
        sum += int(i) 
    return sum

number = input("Введите вещественное число: ").replace(".", "").replace(",", "")

print(summ_iyogo(number))

# Метод replace() возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.

# Метод в Python может принимать максимум 3 параметра: 
# old ‒ старая подстрока, которую нужно заменить; 
# new ‒ новая подстрока, которая заменит старую подстроку; 
# count (необязательно) ‒ сколько раз вы хотите заменить старую подстроку новой. Примечание: Если число не указано, метод заменяет все вхождения старой подстроки новой.
# Примечание: Если число не указано, метод заменяет все вхождения старой подстроки новой.
