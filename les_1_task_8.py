"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
number1 = int(input('Введите первое число'))
number2 = int(input('Введите второе число'))
number3 = int(input('Введите третье число'))
print(f'Число {(number1 + number2 + number3) - (max(number1, number2, number3) + min(number1, number2, number3))} является средним')
