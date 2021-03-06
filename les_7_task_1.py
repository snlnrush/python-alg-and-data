"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

Алгоритм улучшен дбавлением проверки предсортировки. Если при проходе не происходит обмена значений,
значит массив уже отсортирован и нет необходимости делать оставшиеся циклы. Экономия около 10% на больших массивах.
Проверено при длинне массива 100 и 1000.
"""
import random


def bubble_sort_modified(array):
    n = 1
    while n < len(array):
        flag_changes = True
        for i in range(size_array - 1, -1 + n, -1):
            if array[i] > array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                flag_changes = False  # Флаг избыточности прохода сортировки
        print(n, array)  # Вывод для наглядности номера прохода и результата
        if flag_changes:  # Проверяем флаг. Если True, значит больше проходов делать не надо
            break
        n += 1


size_array = 100  # Размер массива

array = [random.randint(-100, 99) for _ in range(size_array)]  # Формируем массив из случайных чисел [-100; 100)

print('Массив до сортировки: \n', array, '\n')

bubble_sort_modified(array)

print('\nМассив после сортировки: \n', array)
