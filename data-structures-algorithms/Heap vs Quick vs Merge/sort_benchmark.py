
import random
import time
import heapq
import matplotlib.pyplot as plt

def heap_sort(a):
    h = a.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []

    while left and right:
        result.append(
            left.pop(0) if left[0] <= right[0]
            else right.pop(0)
        )

    return result + left + right

sizes = [100, 500, 1000, 2000]
algorithms = {
    "Heap Sort": heap_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}
times = {name: [] for name in algorithms}

for n in sizes:
    data = [random.randint(0, 10000) for _ in range(n)]

    for name, func in algorithms.items():
        start = time.perf_counter()
        result = func(data.copy())
        times[name].append(time.perf_counter() - start)
        assert result == sorted(data)

for name, values in times.items():
    plt.plot(sizes, values, marker='o', label=name)

plt.xlabel("Number of elements")
plt.ylabel("Time (seconds)")
plt.title("Heap Sort vs Quick Sort vs Merge Sort")
plt.legend()
plt.grid(True)
plt.show()
