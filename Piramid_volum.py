# Задача
# Дана длина ребра основания правильной треугольной пирамиды а и ее высота h.
# Найти объем пирамиды и площадь ее полной поверхности.
# При вводе неверных данных (длина и высота не должны иметь нулевые или отрицательные значения)
# - вывести "error".
from math import sqrt


def piramid_volum(a1, h1):
    V = ((a1**2) * h1) / (4 * sqrt(3))
    return V


def piramid_area(a2, h2):
    S = (a2 ** 2 * sqrt(3) / 4) + ((3 * a2) / 2) * sqrt(h2 ** 2 + ((a2 ** 2) / 12))
    return S


fin_len = float(input())
height = float(input())
if fin_len <= 0 or height <= 0:
    print('error')
else:
    volum = piramid_volum(fin_len, height)
    area = piramid_area(fin_len, height)
    print(round(volum, 3), round(area, 3))
