"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random
list_numbers = [random.randint(0, 10) for _ in range(20)]  # Генерируем список чисел
dict_values = {}  # Создаем словарь для подсчета количества значений
max_pair = None
max_value = 0
print('Initial list of numbers:', list_numbers)
for elem in list_numbers:  # Подсчитываем количество значений
    dict_values[elem] = dict_values.get(elem, 0) + 1
    if dict_values[elem] > max_value:  # Определяем наиболее частотное значение
        max_pair = (elem, dict_values[elem])
        max_value = dict_values[elem]
print(f'Число {max_pair[0]} встречается чаще всего ({max_pair[1]} раз(а))')
# При наличии одинаковых значений выбирается любое, учитывайте это при проверке (по условию задания)!
