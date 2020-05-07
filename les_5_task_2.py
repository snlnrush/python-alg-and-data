"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import OrderedDict


def convert_16_10(lst: list) -> int:
    base = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
    ordered_base = OrderedDict(base)
    convert_16_10_lst = []
    for power, value in enumerate(lst[:: -1]):
        convert_16_10_lst.append(ordered_base[value] * (16 ** power))
    return sum(convert_16_10_lst)


def convert_10_16(num: int) -> list:
    base = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C',
            13: 'D', 14: 'E', 15: 'F'}
    ordered_base = OrderedDict(base)
    convert_10_16_lst = []
    while num != 0:
        main, balance = divmod(num, 16)
        convert_10_16_lst.append(ordered_base[balance])
        num = main
    return convert_10_16_lst[:: -1]


number_a_lst = list(input('Введите первое число (hex):').swapcase())
number_b_lst = list(input('Введите второе число (hex):').swapcase())
a_10 = convert_16_10(number_a_lst)
b_10 = convert_16_10(number_b_lst)
print(f'Результат умножения {number_a_lst} на {number_b_lst}:', convert_10_16(a_10 * b_10))
print(f'Результата сложения {number_a_lst} на {number_b_lst}:', convert_10_16(a_10 + b_10))

# Внизу пример ввода и вывод данных
"""
Введите первое число (hex):>? a2
Введите второе число (hex):>? c4f
Результат умножения ['A', '2'] на ['C', '4', 'F']: [7, 'C', 9, 'F', 'E']
Результата сложения ['A', '2'] на ['C', '4', 'F']: ['C', 'F', 1]
"""