"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
list_numbers = [random.randint(0, 20) for _ in range(10)]  # Генерируем список чисел
max_value = list_numbers[0]
min_value = list_numbers[0]
min_pair = None
max_pair = None
sum_numbers = 0
print('Initial list of numbers:', list_numbers)
for elem in enumerate(list_numbers):  # Создаем пару: (индекс, число из списка)
    if elem[1] <= min_value:  # Проверяем значение на минимум. Если Да, то сохраняем пару: (индекс, значение)
        min_pair = elem
        min_value = elem[1]
    elif elem[1] >= max_value:  # Проверяем значение на максимум. Если Да, то сохраняем пару: (индекс, значение)
        max_pair = elem
        max_value = elem[1]
print('Max number:', max_pair[1])  # Вывод макимального значения
print('Min number:', min_pair[1])  # Вывод минимального значения
if min_pair[0] <= max_pair[0]:  # Считаем сумму проежуточных значений
    for i in list_numbers[min_pair[0] + 1: max_pair[0]]:
        sum_numbers += i
    [print(i, end=' ') for i in list_numbers[min_pair[0] + 1: max_pair[0]]]  # Вывод слагаемых
else:
    for i in list_numbers[max_pair[0] + 1: min_pair[0]]:
        sum_numbers += i
    [print(i, end=' ') for i in list_numbers[max_pair[0] + 1: min_pair[0]]]  # Вывод слагаемых
print()
print('Sum of numbers:', sum_numbers)  # Вывод суммы элементов между минимальным и максимальным
# При наличии одинаковых значений выбирается любое, учитывайте это при проверке (по условию задания)!
