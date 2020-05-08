"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_tree(phrase: str):
    """
    Функция строит дерево. Для полсчета используется Counter и его метод most_common() для сортировки
    """
    assert len(phrase) > 0, 'Пустая строка, нечего кодировать!'

    phrase_count = Counter(phrase)

    while len(phrase_count) > 1:
        node = Node(None)
        temp_var = phrase_count.most_common()[: -3: -1]
        if isinstance(temp_var[0][0], str):
            node.left = Node(temp_var[0][0])
        else:
            node.left = temp_var[0][0]
        if isinstance(temp_var[1][0], str):
            node.right = Node(temp_var[1][0])
        else:
            node.right = temp_var[1][0]

        del phrase_count[temp_var[0][0]]
        del phrase_count[temp_var[1][0]]

        phrase_count[node] = temp_var[0][1] + temp_var[1][1]

    return [key for key in phrase_count][0]


def encode_sym(root, codes=dict(), code=''):
    """
    Проходим по дереву и создаем коды для символов.
    """
    if root is None:
        return

    if isinstance(root.data, str):
        codes[root.data] = code
        return codes

    encode_sym(root.left, codes, code + '0')
    encode_sym(root.right, codes, code + '1')

    return codes


phrase = input('Введите кодируемую фразу:')
print('Кодируемая фраза:\n', phrase)

tree = encode_sym(build_tree(phrase))

print('\nКодировка по Хаффману')
print('Символ : Код')
for key, value in sorted(tree.items(), key=lambda x: len(x[1])):
    print(key, ':', value)

print('\nЗашифрованная строка:')
for letter in phrase:
    print(tree[letter], end=' ')

"""
Результат работы программ для фразы "beep boop beer!"

Кодируемая фраза:
 beep boop beer!
 
Кодировка по Хаффману
Символ : Код
b : 00
e : 11
  : 010
p : 011
o : 101
! : 1000
r : 1001

Зашифрованная строка:
00 11 11 011 010 00 101 101 011 010 00 11 11 1001 1000 
"""
