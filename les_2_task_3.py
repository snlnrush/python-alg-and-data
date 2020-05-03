"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def inverse(n, s=''):
    if n == 0:
        return s
    s += str(n % 10)
    return inverse(n // 10, s)


number = int(input('Enter number:'))

if number == 0:
    print(f'Inverse number: 0')
else:
    print(f'Inverse number: {inverse(number)}')
