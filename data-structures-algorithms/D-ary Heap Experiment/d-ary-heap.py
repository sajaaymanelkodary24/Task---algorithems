
import heapq, random, time

def test(d, values):
    h = []
    start = time.perf_counter()

    for x in values:
        i = len(h)
        h.append(x)
        while i:
            p = (i - 1) // d
            if h[p] >= h[i]:
                break
            h[p], h[i] = h[i], h[p]
            i = p

    insert_time = time.perf_counter() - start
    start = time.perf_counter()

    while h:
        h[0] = h[-1]
        h.pop()
        i = 0
        while True:
            children = range(d*i+1, min(d*i+d+1, len(h)))
            j = max(children, key=lambda j: h[j], default=-1)
            if j < 0 or h[i] >= h[j]:
                break
            h[i], h[j] = h[j], h[i]
            i = j

    return insert_time, time.perf_counter() - start

data = [random.randint(1, 10000) for _ in range(20000)]

for d in (2, 3, 4):
    print(d, "ary:", test(d, data))
