from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
lines = [sorted(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x: x[1])
L = int(input())
ans, heap = 0, []

for s, e in lines:
    if L < e - s: continue
    while heap and heap[0] < e - L: heappop(heap)
    heappush(heap, s)
    if ans < len(heap): ans = len(heap)

print(ans)
