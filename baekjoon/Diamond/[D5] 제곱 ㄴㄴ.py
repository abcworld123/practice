def make_m(n):
	m = [0] + [1] * n
	for i in range(2, n + 1):
		if m[i] == 0: continue
		for j in range(2 * i, n + 1, i):
			m[j] -= m[i]
	return m


def count(m, k):
	x = 0
	for i in range(2, int(k ** .5) + 1):
		if m[i] == 0: continue
		else: x += m[i] * (k // (i * i))
	return k - x


k = int(input())
left = int(k * 1.64493) if k > 30000000 else int(k * 1.6449) if k > 3000000 else int(k * 1.64) if k > 10000 else int(k * 1.6) if k > 123 else k
right = int(k * 1.64494) if k > 30000000 else int(k * 1.645) if k > 3000000 else int(k * 1.65) if k > 10000 else int(k * 1.67)
m = make_m(int((k * 1.67) ** .5))

while left <= right:
	mid = (left + right) // 2
	nono = count(m, mid)
	if nono < k: left = mid + 1
	else: right = mid - 1

print(left)



# pypy 말고 python에서 최적
def make_m(n):
	m = [0] + [1] * n
	for i in range(2, n + 1):
		if m[i] == 0: continue
		for j in range(2 * i, n + 1, i): m[j] -= m[i]
	return m


def count(m, k, carr, m_ok):
	x = 0
	for i in m_ok: x += m[i] * (k // carr[i])
	return k - x


k = int(input())
left = int(k * 1.64493) if k > 30000000 else int(k * 1.6449) if k > 3000000 else int(k * 1.64) if k > 10000 else int(k * 1.6) if k > 123 else k
right = int(k * 1.64494) if k > 30000000 else int(k * 1.645) if k > 3000000 else int(k * 1.65) if k > 10000 else int(k * 1.67)
n = int(right ** .5)
m = make_m(n)
carr = (0, 1) + tuple(i * i for i in range(2, n + 1))
m_ok = tuple(i for i in range(2, len(m)) if m[i])

while left <= right:
	mid = (left + right) // 2
	if count(m, mid, carr, m_ok) < k: left = mid + 1
	else: right = mid - 1

print(left)
