# Задание
# Постройте графики следующих функций на интервале от -240(градусов) до 360(градусов):
from math import cos, sin, radians, exp, log1p, pow
import matplotlib.pyplot as plt


def f_x(x):
    f = exp(cos(radians(x))) + log1p(sin(0.8 * radians(x)) ** 2 + 1) * cos(radians(x))
    return f


def y_x(y):
    return -log1p((cos(radians(y)) + sin(radians(y)) ** 2) + 1.7) + 2


interval_a = int(input())
interval_b = int(input())

z = [int(i) for i in range(interval_a, interval_b)]
graphical_1 = [y_x(n) for n in z]
graphical_2 = [f_x(m) for m in z]
line1 = plt.plot(graphical_1)
line2 =plt.plot(graphical_2)
plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines["top"].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# plt.grid()
plt.show()
