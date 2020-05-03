"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter1 = input('Введите первую букву:')
letter2 = input('Введите вторую букву:')
index1 = alphabet.index(letter1)
index2 = alphabet.index(letter2)
print(f'Буква {letter1} находится на {index1 + 1} позиции')
print(f'Буква {letter2} находится на {index2 + 1} позиции')
print(f'Между буквой {letter1} и буквой {letter2} находится {abs(index1 - index2) - 1} букв(а/ы)')
