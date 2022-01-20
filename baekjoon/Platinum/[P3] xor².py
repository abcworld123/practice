import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg, arr):
	for i in range(N): seg[262144 + i] = arr[i]
	for i in range(262143, 0, -1): seg[i] = seg[i << 1] ^ seg[i << 1 | 1]

def get(seg, i, x):
	ret, cur, b = 0, 1, 131072
	while b:
		ib = 1 if i & b else 0
		xb = 1 if x & b else 0
		ch = cur << 1 | xb
		ret ^= seg[ch] * ib
		cur = ch ^ ib
		b >>= 1
	return ret

def update(seg, i, x):
	seg[i] ^= x
	while i > 1:
		seg[i >> 1] = seg[i] ^ seg[i ^ 1]
		i >>= 1


N = int(input())
seg = [0] * 524288
ans = __pypy__.builders.StringBuilder()
init(seg, list(map(int, input().split())))

for _ in range(int(input())):
	cmd, *q = map(int, input().split())
	if cmd == 1: ans.append(str(get(seg, q[1] + 1, q[2]) ^ get(seg, q[0], q[2])) + '\n')
	else: update(seg, 262144 + q[0], q[1])

os.write(1, ans.build().encode())


######################################

# 이전 버전
import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg, arr, leaf, s, e, i):
	if s == e:
		if e <= N:
			seg[i] = arr[s - 1]
			leaf[s - 1] = i
	else:
		m, ch = (s + e) >> 1, i << 1
		seg[i] = init(seg, arr, leaf, s, m, ch) ^ init(seg, arr, leaf, m + 1, e, ch + 1)
	return seg[i]

def get(seg, e, l, r, x, bi, i):
	if r - l + 1 == bi << 1 or not bi: return seg[i]
	a, b, c, m = not not l & bi, not not r & bi, not not x & bi, e - bi
	l &= ~bi; r &= ~bi; x &= ~bi; e &= ~bi
	if a ^ b:
		if c: return get(seg, m, 0, r, x, bi >> 1, i << 1) ^ get(seg, e, l, e, x, bi >> 1, i << 1 | 1)
		else: return get(seg, m, l, e, x, bi >> 1, i << 1) ^ get(seg, e, 0, r, x, bi >> 1, i << 1 | 1)
	elif a == c: return get(seg, m, l, r, x, bi >> 1, i << 1)
	else: return get(seg, e, l, r, x, bi >> 1, i << 1 | 1)

def update(seg, i, v):
	seg[i] ^= v
	i >>= 1
	while i:
		seg[i] = seg[i << 1] ^ seg[i << 1 | 1]
		i >>= 1


N = int(input())
arr = list(map(int, input().split()))
sqn = 1 << (N - 1).bit_length()
bi = 1 << (N - 1).bit_length() - 1
seg = [0] * sqn * 2
leaf = [0] * N
init(seg, arr, leaf, 1, sqn, 1)
ans = __pypy__.builders.StringBuilder()
sqn -= 1

for _ in range(int(input())):
	cmd, *q = map(int, input().split())
	if cmd == 1: ans.append(str(get(seg, sqn, q[0], q[1], q[2], bi, 1)) + '\n')
	else: update(seg, leaf[q[0]], q[1])

os.write(1, ans.build().encode())


######################################

# 테스트용 코드
import os, io
from tqdm import tqdm
f = open('input.txt').fileno()
input = io.BytesIO(os.read(f, os.fstat(f).st_size)).readline

N = int(input())
arr = list(map(int, input().split()))
ans = []

for _ in tqdm(range(int(input()))):
	cmd, *q = map(int, input().split())
	if cmd == 1:
		ret = 0
		l, r, x = q
		for i in range(N):
			if l <= i ^ x <= r: ret ^= arr[i]
		ans.append(ret)
	else:
		i, x = q
		arr[i] ^= x

print('\n'.join(map(str, ans)))

#####################################

from random import randint
f = open('input.txt', 'w')
def print(*args):
	f.write(f"{' '.join(map(str, args))}\n")

N, Q = 200000, 200000
# lim = 127
lim = 2147483647
arr = [randint(0, lim) for _ in range(N)]

print(N)
print(*arr)
print(Q)

for _ in range(Q):
	cmd = randint(1, 2)
	if cmd == 1:
		l = randint(0, N - 1)
		r = randint(l, N - 1)
		x = randint(0, N - 1)
		print(cmd, l, r, x)
	else:
		i = randint(0, N - 1)
		x = randint(0, lim)
		print(cmd, i, x)
