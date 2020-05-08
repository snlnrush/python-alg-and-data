"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
from sys import setrecursionlimit
setrecursionlimit(100000)


def graph_build(n):
    """Функция генерирует описание заданного в условии графа размера "n" в виде списка смежности"""
    g = [[i for i in range(n) if i != j] for j in range(n)]
    return g


def deep_search(graph, visited, way, visited_name, start=0):
    """Рекурсивный обход в глубину с заданной вершины (по умолчанию 0)"""
    visited[start] = True
    visited_name.append(start)
    for v in graph[start]:
        way.append(v)
        if not visited[v]:
            deep_search(graph, visited, way, visited_name, v)


nv = int(input('Введите количество вершин:'))
start = int(input('Введите начальную вершину:'))

print(f'Граф с {nv} взаимосвязанными вершинами в виде списка смежности: \n', graph_build(nv))

is_visited = [False] * nv
way = []
visited_name = []

graph = graph_build(nv)

deep_search(graph, is_visited, way, visited_name, start)

print('Пройденные вершины:', visited_name)
print('Путь обхода графа:', way)
