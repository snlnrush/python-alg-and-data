"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
import timeit
import cProfile


def sum_mimax():
    list_numbers = [random.randint(0, 20) for _ in range(1000)]  # Генерируем список чисел
    max_value = list_numbers[0]
    min_value = list_numbers[0]
    min_pair = None
    max_pair = None
    sum_numbers = 0
    # print('Initial list of numbers:', list_numbers)
    for elem in enumerate(list_numbers):  # Создаем пару: (индекс, число из списка)
        if elem[1] <= min_value:  # Проверяем значение на минимум. Если Да, то сохраняем пару: (индекс, значение)
            min_pair = elem
            min_value = elem[1]
        elif elem[1] >= max_value:  # Проверяем значение на максимум. Если Да, то сохраняем пару: (индекс, значение)
            max_pair = elem
            max_value = elem[1]
    # print('Max number:', max_pair[1])  # Вывод макимального значения
    # print('Min number:', min_pair[1])  # Вывод минимального значения
    if min_pair[0] <= max_pair[0]:  # Считаем сумму проежуточных значений
        for i in list_numbers[min_pair[0] + 1: max_pair[0]]:
            sum_numbers += i
        # [print(i, end=' ') for i in list_numbers[min_pair[0] + 1: max_pair[0]]]  # Вывод слагаемых
    else:
        for i in list_numbers[max_pair[0] + 1: min_pair[0]]:
            sum_numbers += i
        # [print(i, end=' ') for i in list_numbers[max_pair[0] + 1: min_pair[0]]]  # Вывод слагаемых
    return sum_numbers

# print(sum_mimax())

# Ниже результаты профилирования алгоритма при помощи timeit и cProfile

# cProfile.run('sum_mimax()') при длинне списка 100
"""
565 function calls in 0.002 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 les_4_task_1_3.py:13(sum_mimax)
        1    0.000    0.000    0.001    0.001 les_4_task_1_3.py:14(<listcomp>)
      100    0.000    0.000    0.001    0.000 random.py:174(randrange)
      100    0.000    0.000    0.001    0.000 random.py:218(randint)
      100    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      160    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# python -m timeit -n 100 -s "import les_4_task_1_3" "les_4_task_1_3.sum_mimax()"
# 100 loops, best of 5: 251 usec per loop

# cProfile.run('sum_mimax()') при длинне списка 200
"""
Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 les_4_task_1_3.py:13(sum_mimax)
        1    0.000    0.000    0.003    0.003 les_4_task_1_3.py:14(<listcomp>)
      200    0.001    0.000    0.002    0.000 random.py:174(randrange)
      200    0.001    0.000    0.003    0.000 random.py:218(randint)
      200    0.001    0.000    0.002    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
      200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      299    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# "les_4_task_1_3.sum_mimax()"
# 100 loops, best of 5: 486 usec per loop

# cProfile.run('sum_mimax()') при длинне списка 1000
"""
5519 function calls in 0.013 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
        1    0.000    0.000    0.013    0.013 les_4_task_1_3.py:13(sum_mimax)
        1    0.001    0.001    0.012    0.012 les_4_task_1_3.py:14(<listcomp>)
     1000    0.003    0.000    0.009    0.000 random.py:174(randrange)
     1000    0.002    0.000    0.011    0.000 random.py:218(randint)
     1000    0.004    0.000    0.006    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
     1000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1514    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# "les_4_task_1_3.sum_mimax()"
# 100 loops, best of 5: 2.51 msec per loop

# Вывод: сложность алгоритма линейная О(n)