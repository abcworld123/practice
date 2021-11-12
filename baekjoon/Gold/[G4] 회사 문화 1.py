import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
booha = [[] for _ in range(n + 1)]
sangsa = tuple(map(int, input().split()))
chingchan = {i: 0 for i in range(1, n + 1)}

for i in range(1, n): booha[sangsa[i]].append(i + 1)
for i in range(m):
	a, b = map(int, input().split())
	chingchan[a] += b

queue = deque([1])
while queue:
	cur = queue.popleft()
	for i in booha[cur]:
		chingchan[i] += chingchan[cur]
		queue.append(i)

print(*chingchan.values())
