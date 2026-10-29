import pandas as pd
import time

prices = pd.read_csv("prices.csv")["price"].tolist()

def linear_profit(a):
    low = a[0]
    best = 0

    for p in a[1:]:
        best = max(best, p - low)
        low = min(low, p)

    return best

def max_sub(a):
    mid = len(a) // 2

    left = a[:mid]
    right = a[mid:]

    if len(a) == 1:
        return a[0], a[0], a[0]

    _, _, lbest = max_sub(left)
    _, _, rbest = max_sub(right)

    lmin = min(left)
    rmax = max(right)

    best = max(lbest, rbest, rmax - lmin)
    return min(min(left), min(right)), max(max(left), max(right)), best

def divide_profit(prices):
    changes = [prices[i] - prices[i - 1]
               for i in range(1, len(prices))]

    if not changes:
        return 0

    return max(0, max_sub(changes)[2])

start = time.time()
print("Linear Profit:", linear_profit(prices))
print("Linear Time:", time.time() - start)

start = time.time()
print("Divide & Conquer Profit:", divide_profit(prices))
print("Divide & Conquer Time:", time.time() - start)