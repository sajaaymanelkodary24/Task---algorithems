
import heapq
import json
from collections import Counter

def build_codes(text):
    freq = Counter(text)
    heap = [[count, i, char] for i, (char, count)
            in enumerate(freq.items())]
    heapq.heapify(heap)

    if not heap:
        return {}

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, [
            a[0] + b[0], min(a[1], b[1]), [a, b]
        ])

    codes = {}

    def walk(node, code):
        if isinstance(node[2], str):
            codes[node[2]] = code or '0'
        else:
            walk(node[2][0], code + '0')
            walk(node[2][1], code + '1')

    walk(heap[0], '')
    return codes

with open("input.txt", encoding="utf-8") as f:
    text = f.read()

codes = build_codes(text)
bits = ''.join(codes[c] for c in text)

data = {
    "codes": codes,
    "bits": bits,
    "length": len(text)
}

with open("compressed.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

decoded = {}
if codes:
    root = {}
    for char, code in codes.items():
        node = root
        for bit in code:
            node = node.setdefault(bit, {})
        node['char'] = char

    result, node = [], root
    for bit in bits:
        node = node[bit]
        if 'char' in node:
            result.append(node['char'])
            node = root
    decoded = ''.join(result)

print("Original characters:", len(text))
print("Encoded bits:", len(bits))
print("Decoded correctly:", decoded == text)
print("Saved: compressed.json")
