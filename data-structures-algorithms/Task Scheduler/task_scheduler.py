
import heapq

tasks = []
counter = 0

while True:
    cmd = input("INSERT / EXTRACT-MAX / EXIT: ").upper()

    if cmd == "INSERT":
        name = input("Task name: ")
        priority = int(input("Priority: "))
        counter += 1
        heapq.heappush(tasks, (-priority, counter, name))

    elif cmd == "EXTRACT-MAX":
        if tasks:
            p, _, name = heapq.heappop(tasks)
            print("Executing:", name, "Priority:", -p)
        else:
            print("No tasks available")

    elif cmd == "EXIT":
        break
