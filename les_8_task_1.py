"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.

Принцип. Строим граф друзей. Создаем словарь, в котором ключ - номер друга, а значание - номера друзей,
с которыми здоровался и дополнительной свой номер (сам с собой). Обходим граф, проверяем в словаре здоровался или нет.
Если нет, добавляем номер друга в словарь по ключу. Если какой-то друг уже с другим здоровался, до обратно здороваться
не нужно.
"""


def graph_build(n):
    """Функция генерирует описание графа приветствий друзей размера "n" в виде списка смежности"""
    g = [[i for i in range(n) if i != j] for j in range(n)]
    return g


def friends_graph(g, start=0):
    dict_graph = {i: [i, ] for i in range(len(g))}  # Словарь "друг: сам, с кем здоровался"
    count = 0
    for i in range(len(g)):
        for j in g[i]:
            if i not in dict_graph[j]:
                dict_graph[i].append(j)
                count += 1
    print("Для наглядности, с кем какой друг здоровался:", dict_graph)
    return count


nf = int(input('Введите количество друзей:'))

graph = graph_build(nf)
print(f'При вестрече {nf} друзей было {friends_graph(graph)} рукопожатий.')
