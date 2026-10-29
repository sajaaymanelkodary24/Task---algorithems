
import heapq, os

def external_sort(source, output, chunk_size=1000):
    files = []

    with open(source) as f:
        while True:
            data = []
            for _ in range(chunk_size):
                line = f.readline()
                if not line:
                    break
                data.append(int(line))

            if not data:
                break

            data.sort()
            name = f"run{len(files)}.txt"
            with open(name, "w") as out:
                out.writelines(f"{x}\n" for x in data)
            files.append(name)

    streams = [open(name) for name in files]
    try:
        with open(output, "w") as out:
            merged = heapq.merge(
                *(map(int, f) for f in streams)
            )
            out.writelines(f"{x}\n" for x in merged)
    finally:
        for f in streams:
            f.close()
        for name in files:
            os.remove(name)

external_sort("input.txt", "sorted.txt")
print("Saved sorted.txt")
