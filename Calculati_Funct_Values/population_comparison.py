# Задача
# Сравнить значения реальной численности населения
# в определенные годы со значениями, вычисленными по формуле в те же годы:
from math import pi, atan
import matplotlib.pyplot as plt


def ar_ctg(x):
    return (pi / 2) - atan(x)


def population_calc(y):
    return 172 / 45 * ar_ctg((2000 - y) / 45)


years = [1000, 1750, 1800, 1850, 1900, 1950, 1955,
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]

population = [0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
              2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
              5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
              7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]
start = int(input())
stop = int(input())
stop = stop + 1
population = population[start:stop]
years = years[start:stop]
population_list = [population_calc(years[t]) for t in range(len(years))]
# population_list = population[start:stop]
truncation_error = [abs(population[i] - population_list[i]) / population[i] for i in range(len(years))]
max_y = years[truncation_error.index(max(truncation_error))]
min_y = years[truncation_error.index(min(truncation_error))]
avr_error = sum(truncation_error) / len(truncation_error)
print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f"%(min_y, max_y, avr_error*100))
