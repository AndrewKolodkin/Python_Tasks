# Рассчитать ежемесячную сумму платежа по кредиту при использовании
# дифференцированных выплат (в этом случае ежемесячный платеж по погашению кредита
# постепенно уменьшается к концу периода кредитования).
# Сумма кредита составляет s рублей, срок кредита n месяцев, процент - k%.
def compute_payment(t, s, n, k):
    a = s / n
    payment = (a + (s - (t - 1) * a) * (k / 1200))
    return payment


s = int(input('Сумма кредита: '))
n = int(input('Срок кредита в месяцах: '))
k = int(input('Процент: '))
t_list = [t for t in range(1, n + 1)]
t_payment = [compute_payment(t, s, n, k) for t in t_list]
proceeds = (sum(t_payment))
proceeds_bank = proceeds - s
for i in range(len(t_list)):
    print("%2d месяц - %8.2f руб" % (t_list[i], t_payment[i]))
print("Доход банка - %6.2f руб" % proceeds_bank)
