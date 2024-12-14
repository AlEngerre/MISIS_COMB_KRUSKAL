def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] != rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(n, edges):
    parent = list(range(n))  # Родитель для каждой вершины
    rank = [0] * n  # Ранг для оптимизации объединений
    mst = []

    # Сортируем рёбра по весу
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):  # Если вершины не связаны
            union(parent, rank, u, v)
            mst.append((u, v, weight))

    return mst

# Пример использования
edges = [
    (0, 1, 1),  # ребро между вершинами 0 и 1 с весом 1
    (0, 2, 4),  # ребро между вершинами 0 и 2 с весом 4
    (1, 2, 2),  # ребро между вершинами 1 и 2 с весом 2
    (1, 3, 5),  # ребро между вершинами 1 и 3 с весом 5
    (2, 3, 3),  # ребро между вершинами 2 и 3 с весом 3
]

# Вершины графа: 0, 1, 2, 3
mst = kruskal(4, edges)
print("Минимальное остовное дерево:", mst)