"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
number_letter = int(input('Введите номер буквы:'))
print(f'Под номером {number_letter} находится буква: {alphabet[number_letter - 1]}')
