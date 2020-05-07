from collections import defaultdict


number_companies = int(input('Введите количество предприятий:'))
dict_companies = defaultdict(int)
dict_companies['sum_profit'] = 0

for i in range(number_companies):
    name, profit = input('Введите название компании и прибыль через пробел (Мозгобой 1000000):').split()
    dict_companies[name] = int(profit)
    dict_companies['sum_profit'] += int(profit)

mean_value = dict_companies['sum_profit'] / number_companies
dict_companies['mean_value'] = mean_value

del dict_companies['sum_profit']

print('Среднее значение прибыли предприятий за год:', mean_value)
print('Предприятия с прибылью ниже среднего:')

for name, value in sorted(dict_companies.items(), key=lambda x: x[1]):
    if name == 'mean_value':
        print('Предприятия с прибылью выше среднего:')
        continue
    print(name, value)

# Внизу пример ввода и вывод данных
"""
Введите количество предприятий:>? 5
Введите название компании и прибыль через пробел (Мозгобой 1000000):>? Рука 100
Введите название компании и прибыль через пробел (Мозгобой 1000000):>? Нога 200
Введите название компании и прибыль через пробел (Мозгобой 1000000):>? Нос 150
Введите название компании и прибыль через пробел (Мозгобой 1000000):>? Живот 500
Введите название компании и прибыль через пробел (Мозгобой 1000000):>? Голова 1000
Среднее значение прибыли предприятий за год: 390.0
Предприятия с прибылью ниже среднего:
Рука 100
Нос 150
Нога 200
Предприятия с прибылью выше среднего:
Живот 500
Голова 1000
"""