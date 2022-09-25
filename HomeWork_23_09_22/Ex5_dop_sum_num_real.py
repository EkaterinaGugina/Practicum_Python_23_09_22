# Ex5_dop_sum_num_real (дополнительная). Напишите программу, 
# которая будет принимать на вход вещественное число и выводить сумму цифр этого числа (решить без использования списка).
number = float(input('Введите действительное число с двумя цифрами после запятой, например 2.59: '))
sum_number = 0
num_1 = round(abs(number), 2) * 100
while num_1 != 0:
    sum_number += int(num_1 % 10)
    num_1 //= 10
print('Сумма цифр, входящих в это число равна ', sum_number)





# from math import sqrt
# x_A, y_A = map(int, input('Введите координаты первой точки: ').split())
# x_B, y_B = map(int, input('Введите координаты второй точки: ').split())
# modul_vector = sqrt((x_A - x_B)**2 + (y_A - y_B)**2)
# print(f'A {x_A, y_A}; B {x_B, y_B} ---> АВ = {round(modul_vector, 2)}')