"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import timeit
import cProfile

def inverse(n, s=''):
    if n == 0:
        return s
    s += str(n % 10)
    return inverse(n // 10, s)


def start(number):
    if number == 0:
        return 0
    else:
        return inverse(number)


# print(start(1234567890))

# Ниже результаты профилирования алгоритма при помощи timeit и cProfile

# cProfile.run('start(1234567890)')
"""
15 function calls (5 primitive calls) in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     11/1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:11(inverse)
        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:18(start)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('start(9876543211234567890)')
"""
24 function calls (5 primitive calls) in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     20/1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:11(inverse)
        1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:18(start)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# "les_4_task_1_2.start(1234567890)"
# 100 loops, best of 5: 8.4 usec per loop

# "les_4_task_1_2.start(9876543211234567890)"
# 100 loops, best of 5: 16.5 usec per loop

# Вывод: вероятно, сложность алгоритма линейная О(n)