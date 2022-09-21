import sys
print("Добро пожаловать в программу для расчета дохода по вкладу.")
name= input("Как тебя зовут? ")
print("Привет " , name)
print("Вычесление дохода по вкладу")
print("ведите исходные данные")
while True:
    s = float(input("\nСумма вклада (РУБ) -> "))
    if s>0 : break
    print("Ошибка ввода данных!\nСумма вкада должна быть больше нуля!")
#while True:
    #ar = input("Повторить ввод данных? (Да/Нет):")
    #if ar =="Нет" or ar == "Нет":
        #print("\nПрограмма работу завершила.")
        #sys.exit()
    #if ar == "Да" or ar == "Да":
        #break
while True:
    vklad = int(input ("\nСрок вклада (МЕСЯЦЕВ) ->"))
    if vklad>0 : break
    print("Ошибка ввода данных!\nСумма вкада должна быть больше нуля!")
while True:
    stavka =float(input ("\nПроцентная ставка (ГОДОВЫХ) ->"))
    if stavka>0 : break
    print("Ошибка ввода данных!\nСумма вкада должна быть больше нуля!")
#Расчет
#обработка данных
summ = s*stavka/12/100*vklad
summ1 = s+summ
#Вывод
print("\nДоход по вкладу:  %9.2f руб." % summ)
summ1=s+summ
print ("\nСумма по окончании срока вклада: %9.2f руб." % summ1)
input ("\nНажмите Enter для завершения програмы")
