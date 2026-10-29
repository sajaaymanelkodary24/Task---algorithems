
import heapq

lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(list(heapq.merge(*lists)))
