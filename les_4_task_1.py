"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import timeit
import cProfile
import random


def do_it(list_numbers):
    max_value = list_numbers[0]
    min_value = list_numbers[0]
    min_pair = None
    max_pair = None
    # print('Initial list of numbers:', list_numbers)
    for elem in enumerate(list_numbers):  # Создаем пару: (индекс, число из списка)
        if elem[1] <= min_value:  # Проверяем значение на минимум. Если Да, то сохраняем пару: (индекс, значение)
            min_pair = elem
            min_value = elem[1]
        elif elem[1] >= max_value:  # Проверяем значение на максимум. Если Да, то сохраняем пару: (индекс, значение)
            max_pair = elem
            max_value = elem[1]
    list_numbers[max_pair[0]] = min_pair[1]  # Меняем максимальное значение на минимальное
    list_numbers[min_pair[0]] = max_pair[1]  # Меняем минимальное значение на максимальное
    # print('Max number:', max_pair[1])
    # print('Min number:', min_pair[1])
    # print('Modified list of numbers', list_numbers)  # Вывод уже измененного списка


def start():
    list_numbers = [random.randint(0, 20) for _ in range(10000)]  # Генерируем список чисел
    do_it(list_numbers)

# Ниже результаты профилирования алгоритма при помощи timeit и cProfile

# cProfile.run('start()') при длинне списка 1000
"""
5490 function calls in 0.015 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:12(do_it)
        1    0.000    0.000    0.015    0.015 les_4_task_1.py:32(start)
        1    0.001    0.001    0.015    0.015 les_4_task_1.py:33(<listcomp>)
     1000    0.004    0.000    0.011    0.000 random.py:174(randrange)
     1000    0.002    0.000    0.013    0.000 random.py:218(randint)
     1000    0.005    0.000    0.008    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
     1000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1484    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# "les_4_task_1.start()"
# 100 loops, best of 5: 2.47 msec per loop

# cProfile.run('start()') при длинне списка 10000
"""
55193 function calls in 0.142 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.142    0.142 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 les_4_task_1.py:12(do_it)
        1    0.000    0.000    0.142    0.142 les_4_task_1.py:32(start)
        1    0.015    0.015    0.139    0.139 les_4_task_1.py:33(<listcomp>)
    10000    0.029    0.000    0.101    0.000 random.py:174(randrange)
    10000    0.023    0.000    0.124    0.000 random.py:218(randint)
    10000    0.045    0.000    0.073    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.142    0.142 {built-in method builtins.exec}
    10000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    15187    0.017    0.000    0.017    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# "les_4_task_1.start()"
# 100 loops, best of 5: 25.3 msec per loop

# Вывод: сложность алгоритма линейная О(n)