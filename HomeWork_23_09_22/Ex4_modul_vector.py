# Ex4_modul_vector. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
from math import sqrt
x_A, y_A = map(int, input('Введите координаты первой точки: ').split())
x_B, y_B = map(int, input('Введите координаты второй точки: ').split())
modul_vector = sqrt((x_A - x_B)**2 + (y_A - y_B)**2)
print(f'A {x_A, y_A}; B {x_B, y_B} ---> АВ = {round(modul_vector, 2)}')