"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».

"""
import timeit
import cProfile


def prime_eratosphen(index_prime):
    n = index_prime ** 2  # Задаем глубину поиска
    numbers_list = [i for i in range(n)]
    numbers_list[1] = 0
    for i in range(2, n):
        if numbers_list[i] != 0:
            j = i * 2
        while j < n:
            numbers_list[j] = 0
            j += i
    prime_numbers = [i for i in numbers_list if i != 0]
    return prime_numbers[index_prime - 1]  # Возвращаем простое число под заданным номером

# print(f'Под номером 30 находится простое число {prime_eratosphen(30)}')

# Далее профилирование алгоритма


# cProfile.run('prime_eratosphen(100)')
"""
6 function calls in 0.009 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.007    0.007    0.009    0.009 les_4_task_2_2.py:13(prime_eratosphen)
        1    0.001    0.001    0.001    0.001 les_4_task_2_2.py:15(<listcomp>)
        1    0.001    0.001    0.001    0.001 les_4_task_2_2.py:24(<listcomp>)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('prime_eratosphen(200)')
"""
6 function calls in 0.035 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.035    0.035 <string>:1(<module>)
        1    0.029    0.029    0.035    0.035 les_4_task_2_2.py:13(prime_eratosphen)
        1    0.003    0.003    0.003    0.003 les_4_task_2_2.py:15(<listcomp>)
        1    0.003    0.003    0.003    0.003 les_4_task_2_2.py:24(<listcomp>)
        1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('prime_eratosphen(500)')
"""
6 function calls in 0.340 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.010    0.010    0.340    0.340 <string>:1(<module>)
        1    0.268    0.268    0.329    0.329 les_4_task_2_2.py:13(prime_eratosphen)
        1    0.035    0.035    0.035    0.035 les_4_task_2_2.py:15(<listcomp>)
        1    0.026    0.026    0.026    0.026 les_4_task_2_2.py:24(<listcomp>)
        1    0.000    0.000    0.340    0.340 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('prime_eratosphen(1000)')
"""
6 function calls in 1.645 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.028    0.028    1.645    1.645 <string>:1(<module>)
        1    1.177    1.177    1.617    1.617 les_4_task_2_2.py:13(prime_eratosphen)
        1    0.378    0.378    0.378    0.378 les_4_task_2_2.py:15(<listcomp>)
        1    0.063    0.063    0.063    0.063 les_4_task_2_2.py:24(<listcomp>)
        1    0.000    0.000    1.645    1.645 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# "les_4_task_2_2.prime_eratosphen(100)"
# 100 loops, best of 5: 6.99 msec per loop

# "les_4_task_2_2.prime_eratosphen(500)"
# 100 loops, best of 5: 232 msec per loop

# "les_4_task_2_2.prime_eratosphen(1000)"
# 100 loops, best of 5: 1.05 sec per loop