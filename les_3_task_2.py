"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
"""
import random
even_index_list = []
list_numbers = [random.randint(0, 20) for _ in range(10)]  # Генерируем список чисел
print('Initial list of numbers:', list_numbers)
for elem in enumerate(list_numbers):  # Создаем пару (индекс, число из списка)
    if elem[1] % 2 == 0:  # Проверяем четность. Если Да, то сохраняем индекс
        even_index_list.append(elem[0])
print('List of even number indices', even_index_list)
