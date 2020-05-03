"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


def s_element(n, s=0, b=1):
    if n == 0:
        return s
    s += b
    n -= 1
    b /= 2
    return s_element(n, s, b)


amount = int(input('Enter number:'))

if amount == 0:
    print(f'Sum of numbers: 0')
else:
    print(f'Sum of numbers: {s_element(amount)}')
