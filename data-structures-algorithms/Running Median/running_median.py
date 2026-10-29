
import heapq

low, high = [], []

for x in map(float, input("Enter numbers: ").split()):
    if not low or x <= -low[0]:
        heapq.heappush(low, -x)
    else:
        heapq.heappush(high, x)

    if len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))

    if len(low) > len(high):
        median = -low[0]
    else:
        median = (-low[0] + high[0]) / 2

    print("Median:", median)
