# Ракета запускается с точки на экваторе и развивает скорость v км/с.
# Каков результат запуска?
# Указание: если v ≤ 7.8 км/с, то ракета упадет на Землю (вывести 0),
# если 7.8 <v <11.2, то ракета станет спутником Земли (вывести 1),
# если  11.2 ≤ v ≤ 16.4 , то ракета станет спутником Солнца (вывести 2),
# если v > 16.4, то ракета покинет Солнечную Систему (вывести 3).
# Если будет введено значение, меньшее или равное 0, то вывести "error".
# Входные данные:
# скорость ракеты.
# Выходные данные:
# число 0, 1, 2, 3 или error.
print('Расчитать результат запуска ракеты!')
speed = float(input('Скорость запуска ракеты? '))
if speed <= 0:
    print('error')
elif speed <= 7.8:
    print('0')
elif 7.8 < speed < 11.2:
    print('1')
elif 11.2 <= speed <= 16.4:
    print('2')
elif speed > 16.4:
    print('3')
