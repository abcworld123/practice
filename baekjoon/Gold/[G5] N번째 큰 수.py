import io, os
from heapq import heappop, heappush

def readint():
    n, sign = 0, 1
    while 1:
        for x in io.BytesIO(os.read(0, 35000)).read():
            if x >= 48: n = 10 * n + x - 48
            elif x == 45: sign = -1
            else: yield n * sign; n, sign = 0, 1

input = readint()
N = next(input)
heap = []

for _ in range(N):
    heappush(heap, next(input))

for _ in range(N * N - N):
    heappush(heap, next(input))
    heappop(heap)

print(heappop(heap))
