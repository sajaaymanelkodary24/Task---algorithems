
import heapq

meetings = [(0, 30), (5, 10), (15, 20), (35, 40)]
meetings.sort()
rooms = []

for start, end in meetings:
    if rooms and rooms[0] <= start:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)

print("Minimum rooms:", len(rooms))
