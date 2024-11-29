def bellman_ford(graph, vertices, start):
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distances

# Example graph and test case
graph_bellman_ford = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('C', 'D', 3),
    ('D', 'B', -6)
]
vertices_bellman_ford = ['A', 'B', 'C', 'D']

print("Bellman-Ford Algorithm:", bellman_ford(graph_bellman_ford, vertices_bellman_ford, 'A'))
