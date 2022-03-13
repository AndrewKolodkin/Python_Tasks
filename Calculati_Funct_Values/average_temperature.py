# В течение некоторого периода ежедневно измерялись температуры в
# 0 и 12 часов в одном и том же месте.
# Также известна средняя статистическая суточная температура за аналогичный период,
# полученная в результате наблюдений за погодой за длительный период времени
# в рассматриваемой местности. Необходимо вывести номера дней,
# в которые средняя температура за сутки
# (вычисляется как среднее значение температуры в 0 и 12 часов)
# была выше средней статистической.

# Входные данные:
#
# строка, состоящая из вещественных чисел, разделенных
# пробелами (значения температур в 0 часов);
# строка, состоящая из вещественных чисел, разделенных
# пробелами (значения температур в 12 часов);
# среднесуточная температура (вещественное число).
# Выходные данные:
#
# номера дней, в которых температура была выше средней
# (нумерация дней начинается с 0), каждый номер выводится на отдельной строке.
temp_0 = list(map(float, input().split()))
temp_1 = list(map(float, input().split()))
average_temp = float(input())
temp_avg = [sum(i) / len(i) for i in zip(temp_0, temp_1)]
for k in range(len(temp_avg)):
    list_high = temp_avg[k]
    if list_high > average_temp:
        print(k)
