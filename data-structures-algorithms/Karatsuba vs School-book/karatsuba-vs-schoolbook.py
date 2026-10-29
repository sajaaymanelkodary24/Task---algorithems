
import random, timeit

def school(a, b):
    return a * b

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    a, b = divmod(x, p)
    c, d = divmod(y, p)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    mid = karatsuba(a+b, c+d) - ac - bd

    return ac*p*p + mid*p + bd

for digits in (10, 50, 100, 500, 1000):
    x = random.randint(10**(digits-1), 10**digits-1)
    y = random.randint(10**(digits-1), 10**digits-1)

    for name, func in [("School-book", school), ("Karatsuba", karatsuba)]:
        t = timeit.timeit(lambda: func(x, y), number=10)
        print(digits, name, round(t, 6), "seconds")
