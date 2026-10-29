
import random, time
from multiprocessing import Pool

def merge_sort(a):
    if len(a) < 2:
        return a
    m = len(a)//2
    l, r = merge_sort(a[:m]), merge_sort(a[m:])
    out = []
    while l and r:
        out.append(l.pop(0) if l[0] <= r[0] else r.pop(0))
    return out+l+r

def parallel_sort(a, workers):
    m = len(a)//2
    with Pool(workers) as pool:
        l, r = pool.map(merge_sort, [a[:m], a[m:]])
    return list(__import__('heapq').merge(l, r))

if __name__ == "__main__":
    data = [random.randint(0, 100000) for _ in range(100000)]

    for workers in (1, 2, 4):
        t = time.perf_counter()
        result = parallel_sort(data, workers)
        print(workers, "workers:", round(time.perf_counter()-t, 3), "sec")
