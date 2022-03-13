# Задание
# Постройте график функции, описывающей численность населения на интервале [a, b]:
from math import pi, atan
import matplotlib.pyplot as plt


def ar_ctg(x):
    return (pi / 2) - atan(x)


def population_calc(y):
    return 172 / 45 * ar_ctg((2000 - y) / 45)


# Зададим начало a и конец  b интервала построения функции,
# задав количество точек построения. Вычислим шаг:
a = int(input('Начальный год: '))
b = int(input('Конечный год: '))
n = [int(i) for i in range(a, b)]
year_list = [population_calc(x) for x in n]

line = plt.plot(n, year_list)
plt.gca().spines['left'].set_position('center')
plt.gca().spines['bottom'].set_position('center')
plt.gca().spines["top"].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# plt.grid()
plt.show()