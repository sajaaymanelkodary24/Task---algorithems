
import random, time
import matplotlib.pyplot as plt

def insertion(a):
    a = a[:]
    for i in range(1, len(a)):
        x, j = a[i], i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
    return a

def merge(a):
    if len(a) < 2:
        return a
    m = len(a)//2
    l, r = merge(a[:m]), merge(a[m:])
    out = []
    while l and r:
        out.append(l.pop(0) if l[0] <= r[0] else r.pop(0))
    return out + l + r

def quick(a):
    if len(a) < 2:
        return a
    p = a[len(a)//2]
    return quick([x for x in a if x < p]) + \
           [x for x in a if x == p] + \
           quick([x for x in a if x > p])

sizes = [1000, 5000, 10000, 50000, 100000]
funcs = {"Insertion": insertion, "Merge": merge,
         "Quick": quick, "Python sorted": sorted}
results = {name: [] for name in funcs}

for n in sizes:
    base = list(range(n))
    cases = {
        "sorted": base,
        "reversed": base[::-1],
        "random": random.sample(base, n)
    }

    for case, data in cases.items():
        for name, func in funcs.items():
            if name == "Insertion" and n > 10000:
                results[name].append(float("nan"))
                continue
            t = time.perf_counter()
            func(data)
            elapsed = time.perf_counter() - t
            results[name].append(elapsed)

for name, times in results.items():
    plt.plot(range(len(times)), times, marker=".", label=name)

plt.ylabel("Time (seconds)")
plt.xlabel("Test case and input size")
plt.legend()
plt.grid()
plt.show()
