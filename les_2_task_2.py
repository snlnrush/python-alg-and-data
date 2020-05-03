"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input('Enter number:'))
even_count = 0
odd_count = 0

while number > 0:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count +=1
    number //= 10

print(f'Even numbers: {even_count}')
print(f'Odd numbers: {odd_count}')
