"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша (hash(),
sha1() или любая другая из модуля hashlib)
"""
import hashlib
from itertools import combinations


def options(phrase: str) -> set:
    """
    Функция вычисляет все возможные уникальные варианты и сочетания подстрок.

    """
    assert len(phrase) > 0, 'Пустая строка!'

    if len(phrase) == 1:
        return set(phrase)

    options_set = set()
    for i in range(1, len(phrase)):
        options_set.update(combinations(phrase, i))  # комбинируем все варианты подстрок, уникализируем их во множестве.
    return options_set


def hash_check(phrase: str, subs: set) -> tuple:
    """
    Функция проверяет наличие подстроки в строке с помощью хеш-функции и при наличии суммирует.
    """
    count = 0
    list_subs = []
    for sub_item in subs:
        sub_item_hash = hashlib.sha1(''.join(sub_item).encode('utf-8')).hexdigest()
        for i in range(len(phrase) - len(sub_item) + 1):
            if sub_item_hash == hashlib.sha1(phrase[i: i + len(sub_item)].encode('utf-8')).hexdigest():
                count += 1
                list_subs.append(''.join(sub_item))
                break
    return count, list_subs


phrase = input('Введите исследуему строку:')

print('\nИсследуемая строка:\n', phrase)

result = hash_check(phrase, options(phrase))

print('\nКоличество различных подстрок в строке:', result[0])
print('\nВсе различные уникальные подстроки в строке:\n', result[1])


"""
Пример работы программы

Исследуемая строка:
 papa
 
Количество различных подстрок в строке: 6

Все различные уникальные подстроки в строке:
 ['pap', 'p', 'pa', 'apa', 'a', 'ap']
"""
