
import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

def dijkstra_heap(start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue

        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))

    return dist

def dijkstra_array(start):
    dist = {v: float('inf') for v in graph}
    visited = set()
    dist[start] = 0

    while len(visited) < len(graph):
        u = min(
            (v for v in graph if v not in visited),
            key=lambda v: dist[v],
            default=None
        )
        if u is None or dist[u] == float('inf'):
            break

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

print("Heap:", dijkstra_heap('A'))
print("Array:", dijkstra_array('A'))
