m, b, ans, hour = [], [], 0, 0
N, M = map(int, input().split())
for row in range(N): m += list(map(int, input().split()))
for i in range(N * M):
	if m[i] == 0: b.append(i)
m[0] = 2

while 1:
	queue, exposed = [], set()
	for v in range(N * M):
		if m[v] == 2: queue.append(v)
	for v in queue:
		if m[v] == 2:
			U, R, D, L = v - M, v + 1, v + M, v - 1
			if U >= 0:
				if m[U] == 0: m[U] = 2; queue.append(U)
				elif m[U] == 1: exposed.add(U)
			if R < N * M and R % M:
				if m[R] == 0: m[R] = 2; queue.append(R)
				elif m[R] == 1: exposed.add(R)
			if D < N * M:
				if m[D] == 0: m[D] = 2; queue.append(D)
				elif m[D] == 1: exposed.add(D)
			if L % M != M - 1:
				if m[L] == 0: m[L] = 2; queue.append(L)
				elif m[L] == 1: exposed.add(L)
	hour += 1
	for i in exposed: m[i] = 0
	if m.count(1) == 0: break

print(hour)
print(len(exposed))
