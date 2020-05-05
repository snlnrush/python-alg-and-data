"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random
list_numbers = [random.randint(0, 20) for _ in range(10)]  # Генерируем список чисел
max_value = list_numbers[0]
min_value = list_numbers[0]
min_pair = None
max_pair = None
print('Initial list of numbers:', list_numbers)
for elem in enumerate(list_numbers):  # Создаем пару: (индекс, число из списка)
    if elem[1] <= min_value:  # Проверяем значение на минимум. Если Да, то сохраняем пару: (индекс, значение)
        min_pair = elem
        min_value = elem[1]
    elif elem[1] >= max_value:  # Проверяем значение на максимум. Если Да, то сохраняем пару: (индекс, значение)
        max_pair = elem
        max_value = elem[1]
list_numbers[max_pair[0]] = min_pair[1]  # Меняем максимальное значение на минимальное
list_numbers[min_pair[0]] = max_pair[1]  # Меняем минимальное значение на максимальное
print('Max number:', max_pair[1])
print('Min number:', min_pair[1])
print('Modified list of numbers', list_numbers)  # Вывод уже измененного списка
# При наличии одинаковых значений выбирается любое, учитывайте это при проверке (по условию задания)!
