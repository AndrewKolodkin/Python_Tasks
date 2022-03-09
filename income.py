# Задание
# Используя функцию compute_income(), созданную на шаге 6 этого модуля,
# решить  задачу о подборе вклада.
# Пояснение.
# К реализации:
# Выполнить перебор значений вклада x, например от 1000 до 30000 рублей
# (эти числа  нужно подобрать в программе, верхняя граница может быть больше или меньше!!!!),
# с помощью цикла. В цикле вычислять значение прибыли  функцией compute_income(),
# в качестве параметров передать x , процентную ставку и количество месяцев из задачи.
# Сравнить полученное значение (ОКРУГЛИВ его функцией round()) с заданной в задаче прибылью.
# Если они совпадают - вывести вклад x в консоль.
from math import pow


# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    # вычислить прибыль
    S = deposit * ((1 + (interest_rate / (12 * 100))) ** amount_months)
    S = S - deposit
    return S
k = 8.0
n = 8
s = 602
# вычислить прибыль с помощью функции
for x in range(10000, 30000):
    income = compute_income(x, k, n)
    # print(round(income))
    if round(income) == s:
        # вывести результат
        print(x)
