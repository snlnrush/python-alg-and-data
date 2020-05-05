"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random
list_numbers = [random.randint(0, 20) for _ in range(10)]  # Генерируем список чисел
min1 = list_numbers[0]
min2 = list_numbers[1]
print('Initial list of numbers:', list_numbers)  # Выводим исследуемый список
for i in list_numbers[2:]:  # Поиск двух наименьших элементов
    if i <= min1:
        if min2 > min1:
            min2 = min1
        min1 = i
    elif i <= min2:
        min2 = i
print(f'The two smallest elements: {min1} and {min2}')
