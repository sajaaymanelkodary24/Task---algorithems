
import heapq

events = [(1, "Customer A"), (2, "Customer B"),
          (3, "Customer C"), (5, "Customer D")]
heapq.heapify(events)
tellers = [0, 0]

while events:
    time, name = heapq.heappop(events)
    i = min(range(2), key=lambda x: tellers[x])
    start = max(time, tellers[i])
    tellers[i] = start + 3
    print(name, "arrives:", time,
          "starts:", start, "finishes:", tellers[i])
