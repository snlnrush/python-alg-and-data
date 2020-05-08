"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random
import operator


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        # print('Left:', left)
        right = merge_sort(L[middle:], compare)
        # print('Right:', right)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    # print('Result:', result)
    return result


size_array = 10  # Размер массива

array = [random.randint(0, 51) for _ in range(size_array)]  # Формируем массив из случайных чисел [0; 50)

print('Массив до сортировки: \n', array, '\n')

print('\nМассив после сортировки: \n', merge_sort(array))
