
from math import radians, sin, cos, asin, sqrt
from itertools import combinations
import time

places = [
    ("Cafe A", 30.0444, 31.2357),
    ("Cafe B", 30.0500, 31.2400),
    ("Cafe C", 30.0600, 31.2200),
    ("Cafe D", 30.0300, 31.2500),
    ("Cafe E", 30.0470, 31.2320)
]

def dist(a, b):
    lat1, lon1 = map(radians, a[1:])
    lat2, lon2 = map(radians, b[1:])
    dlat, dlon = lat2-lat1, lon2-lon1
    h = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 6371 * 2 * asin(sqrt(h))

def brute(points):
    return min(
        (dist(a, b), a[0], b[0])
        for a, b in combinations(points, 2)
    )

def closest(points):
    if len(points) <= 3:
        return brute(points)

    points = sorted(points, key=lambda p: p[1])
    m = len(points)//2
    left, right = points[:m], points[m:]
    best = min(closest(left), closest(right))

    # Check pairs crossing the split line.
    mid = points[m][1]
    strip = [p for p in points if abs(p[1]-mid) < best[0]/111]
    for a, b in combinations(strip, 2):
        d = dist(a, b)
        if d < best[0]:
            best = (d, a[0], b[0])
    return best

for name, func in [("Brute force", brute), ("Divide and conquer", closest)]:
    t = time.perf_counter()
    print(name, func(places), round(time.perf_counter()-t, 6), "sec")
