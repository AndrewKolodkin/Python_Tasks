# Задача
# Вычисление и прогноз численности населения Земли по формуле С. П. Капицы.
import math

def arc_ctg(x):
    return (math.pi / 2) - math.atan(x)

def compute_population(t):
    # вычислить численность населения для года t по формуле
    a = (172 / 45) * arc_ctg((2000 - t) / 45)
    return a

# ввести строку с перечисленными через пробел годами
line = input()
# преобразовать строку в список из строковых значений годов
years_str_list = line.split()
# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list,
# преобразовав строковые значения в целые
years_list = [int(i) for i in years_str_list]

# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list
population_list = [compute_population(i) for i in years_list]
for i in range(n):
    print(f"{years_list[i]:5d} - {population_list[i]:6.3f} миллиард(ов)")
# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"
