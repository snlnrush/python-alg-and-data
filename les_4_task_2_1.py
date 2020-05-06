"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Второй — без использования «Решета Эратосфена».

Использован метод:

Перебор делителей. Достаточно поделить n на все простые числа от 2 до округленного значения корня квадратного из n.
"""
import timeit
import cProfile


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            return False
        i += 1
    return True


def search_prime_number(n):
    prime_number_list = []
    num = 2
    while len(prime_number_list) < n:
        if is_prime(num):
            prime_number_list.append(num)
        num += 1
    return prime_number_list[-1]


# print(f'Под номером 30 находится простое число {search_prime_number(30)}')

# Далее профилирование алгоритма

# cProfile.run('search_prime_number(5)')
"""
30 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       10    0.000    0.000    0.000    0.000 les_4_task_2_1.py:16(is_prime)
        1    0.000    0.000    0.000    0.000 les_4_task_2_1.py:27(search_prime_number)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('search_prime_number(50)')
"""
511 function calls in 0.004 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
      228    0.001    0.000    0.001    0.000 les_4_task_2_1.py:16(is_prime)
        1    0.002    0.002    0.004    0.004 les_4_task_2_1.py:27(search_prime_number)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('search_prime_number(100)')
"""
1185 function calls in 0.004 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
      540    0.002    0.000    0.002    0.000 les_4_task_2_1.py:16(is_prime)
        1    0.001    0.001    0.004    0.004 les_4_task_2_1.py:27(search_prime_number)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# cProfile.run('search_prime_number(1000)')
"""
16841 function calls in 0.137 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.137    0.137 <string>:1(<module>)
     7918    0.095    0.000    0.095    0.000 les_4_task_2_1.py:16(is_prime)
        1    0.031    0.031    0.137    0.137 les_4_task_2_1.py:27(search_prime_number)
        1    0.000    0.000    0.137    0.137 {built-in method builtins.exec}
     7919    0.009    0.000    0.009    0.000 {built-in method builtins.len}
     1000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# "les_4_task_2_1.search_prime_number(30)"
# 30 loops, best of 5: 258 usec per loop

# "les_4_task_2_1.search_prime_number(50)"
# 30 loops, best of 5: 653 usec per loop

# "les_4_task_2_1.search_prime_number(100)"
# 30 loops, best of 5: 1.98 msec per loop

# "les_4_task_2_1.search_prime_number(1000)"
# 30 loops, best of 5: 64.4 msec per loop