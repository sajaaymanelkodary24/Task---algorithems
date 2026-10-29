
import random, time

def hybrid(a, k):
    if len(a) <= k:
        for i in range(1, len(a)):
            x, j = a[i], i-1
            while j >= 0 and a[j] > x:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = x
        return a

    m = len(a)//2
    l = hybrid(a[:m], k)
    r = hybrid(a[m:], k)
    out = []

    while l and r:
        out.append(l.pop(0) if l[0] <= r[0] else r.pop(0))
    return out + l + r

data = [random.randint(0, 100000) for _ in range(5000)]

for k in [4, 8, 16, 24, 32, 48, 64]:
    t = time.perf_counter()
    hybrid(data[:], k)
    print(k, round(time.perf_counter()-t, 5), "seconds")
