# Задача. "Геометрические вычисления на плоскости"
# 1. На вход подаются координаты точек на плоскости
# 2. Написать функцию вычисления длины отрезков между точками
# 3. Написать функцию вычисления периметра и площади треугольника
# 4. Рассчитать радиус вписанной в треугольник окружности
# 5. Расчитать радиус описанной окружности
# 6. Рассчитать сумму длин трех медиан треугольника.
from math import sqrt, pow


# функция вычисления длины отрезков между точками
def len_compute(x0, y0, x1, y1):
    len = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
    return len


# функция вычисления площади треугольника
def area(a1, b1, c1):
    p = (a1 + b1 + c1) / 2
    S = sqrt(p * (p - a1) * (p - b1) * (p - c1))
    return S


def compute_radius_inscribed(p, a1, b1, c1):
    inscribed_radius = sqrt((p / 2 - a1) * (p / 2 - b1) * (p / 2 - c1) / (p / 2))
    return inscribed_radius


def compute_circumscribed_radius(s, a2, b2, c2):
    circumscribed_radius = (a2 * b2 * c2) / (4 * s)
    return circumscribed_radius


print('Введите координаты вершин треугольника: ')
x_a = float(input('Координата X вершины A: '))
y_a = float(input('Координата Y вершины A: '))
x_b = float(input('Координата X вершины B: '))
y_b = float(input('Координата Y вершины B: '))
x_c = float(input('Координата X вершины C: '))
y_c = float(input('Координата X вершины C: '))
c = len_compute(x_a, y_a, x_b, y_b)
a = len_compute(x_b, y_b, x_c, y_c)
b = len_compute(x_a, y_a, x_c, y_c)
# Проверка существует ли треугольник
if a + b <= c or b + c <= a or a + c <= b:
    print("error")
else:
    s = area(a, b, c)
    p = a + b + c
    r1 = compute_radius_inscribed(p, a, b, c)
    r2 = compute_circumscribed_radius(s, a, b, c)
    # Длины медиан
    M1 = 0.5 * sqrt(2 * (c ** 2 + b ** 2) - a ** 2)
    M2 = 0.5 * sqrt(2 * (a ** 2 + c ** 2) - b ** 2)
    M3 = 0.5 * sqrt(2 * (a ** 2 + b ** 2) - c ** 2)
    summ_m = M1 + M2 + M3
print(round(r1, 4), round(r2, 4), round(summ_m, 4))
