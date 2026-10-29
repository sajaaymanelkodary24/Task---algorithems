
import math

def insertion(a, lo, hi):
    for i in range(lo + 1, hi + 1):
        x, j = a[i], i - 1
        while j >= lo and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x

def heap_sort(a, lo, hi):
    h = a[lo:hi + 1]
    h.sort(reverse=False)
    a[lo:hi + 1] = h

def intro(a, lo, hi, depth):
    if hi - lo < 16:
        insertion(a, lo, hi)
        return

    if depth == 0:
        heap_sort(a, lo, hi)
        return

    pivot = a[(lo + hi) // 2]
    i, j = lo, hi

    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if lo < j:
        intro(a, lo, j, depth - 1)
    if i < hi:
        intro(a, i, hi, depth - 1)

def introsort(a):
    if len(a) > 1:
        depth = 2 * int(math.log2(len(a)))
        intro(a, 0, len(a) - 1, depth)
    return a

numbers = [9, 4, 7, 2, 8, 1, 5, 3, 6]
print("Sorted:", introsort(numbers))
