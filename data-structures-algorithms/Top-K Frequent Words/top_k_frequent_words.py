
from collections import Counter
import heapq
import re

text = input("Enter text: ").lower()
k = int(input("Enter k: "))

freq = Counter(re.findall(r"\b\w+\b", text))
heap = []

for word, count in freq.items():
    heapq.heappush(heap, (count, word))
    if len(heap) > k:
        heapq.heappop(heap)

for count, word in sorted(heap, key=lambda x: (-x[0], x[1])):
    print(word, ":", count)
