import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 16384


class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._fd = file.fileno()
		self.buffer = BytesIO()
		self.writable = "x" in file.mode or "r" not in file.mode
		self.write = self.buffer.write if self.writable else None

	def read(self):
		while True:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			if not b:
				break
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines = 0
		return self.buffer.read()

	def readline(self):
		while self.newlines == 0:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			self.newlines = b.count(b"\n") + (not b)
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines -= 1
		return self.buffer.readline()

	def flush(self):
		if self.writable:
			os.write(self._fd, self.buffer.getvalue())
			self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
	def __init__(self, file):
		self.buffer = FastIO(file)
		self.flush = self.buffer.flush
		self.writable = self.buffer.writable
		self.write = lambda s: self.buffer.write(s.encode("ascii"))
		self.read = lambda: self.buffer.read().decode("ascii")
		self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

#############################################################################

def init(seg, s, e, i):
	if s == e: seg[i] = [arr[s], 0, 1, arr[s]]  # max, smax, max_cnt, sum
	else:
		m, c = (s + e) >> 1, i << 1
		seg[i] = find_fs(init(seg, s, m, c), init(seg, m + 1, e, c + 1))
	return seg[i]


def find_fs(lc, rc):
	if lc[0] == rc[0]:
		return [lc[0], max(lc[1], rc[1]), lc[2] + rc[2], lc[3] + rc[3]]
	else:
		if lc[0] < rc[0]: lc, rc = rc, lc
		return [lc[0], max(lc[1], rc[0]), lc[2], lc[3] + rc[3]]


def get_sum(seg, lz, s, e, l, r, i):
	propagation(seg, lz, s, e, i)
	if l <= s and e <= r: return seg[i][3]
	m, c = (s + e) >> 1, i << 1
	if m < l: return get_sum(seg, lz, m + 1, e, l, r, c + 1)
	elif m + 1 > r: return get_sum(seg, lz, s, m, l, r, c)
	else: return get_sum(seg, lz, s, m, l, r, c) + get_sum(seg, lz, m + 1, e, l, r, c + 1)


def get_max(seg, lz, s, e, l, r, i):
	propagation(seg, lz, s, e, i)
	if l <= s and e <= r: return seg[i][0]
	m, c = (s + e) >> 1, i << 1
	if m < l: return get_max(seg, lz, m + 1, e, l, r, c + 1)
	elif m + 1 > r: return get_max(seg, lz, s, m, l, r, c)
	else: return max(get_max(seg, lz, s, m, l, r, c), get_max(seg, lz, m + 1, e, l, r, c + 1))


def update(seg, lz, s, e, l, r, i, v):
	propagation(seg, lz, s, e, i)
	if s == e:
		if seg[i][0] > v:
			seg[i][3] -= (seg[i][0] - v) * seg[i][2]
			seg[i][0] = v
	else:
		m, c = (s + e) >> 1, i << 1
		if l <= s and e <= r and seg[i][1] < v:
				seg[i][3] -= (seg[i][0] - v) * seg[i][2]
				seg[i][0] = v
				if seg[c][0] > v and (lz[c] == 0 or lz[c] > v):
					seg[c][3] -= (seg[c][0] - v) * seg[c][2]
					seg[c][0] = v
					lz[c] = v
				if seg[c + 1][0] > v and (lz[c + 1] == 0 or lz[c + 1] > v):
					seg[c + 1][3] -= (seg[c + 1][0] - v) * seg[c + 1][2]
					seg[c + 1][0] = v
					lz[c + 1] = v
		else:
			nl, nr = None, None
			if l <= m and seg[c][0] > v:
				nl = update(seg, lz, s, m, l, r, c, v)
			if m + 1 <= r and seg[c + 1][0] > v:
				nr = update(seg, lz, m + 1, e, l, r, c + 1, v)
			if nl and nr: seg[i] = find_fs(nl, nr)
			elif nl: seg[i] = find_fs(nl, seg[c + 1])
			elif nr: seg[i] = find_fs(seg[c], nr)
	return seg[i]


def propagation(seg, lz, s, e, i):
	if lz[i]:
		if s != e:
			c = i << 1
			if seg[c][0] > lz[i]:
				seg[c][3] -= (seg[c][0] - lz[i]) * seg[c][2]
				seg[c][0] = lz[i]
				lz[c] = lz[i]
			if seg[c + 1][0] > lz[i]:
				seg[c + 1][3] -= (seg[c + 1][0] - lz[i]) * seg[c + 1][2]
				seg[c + 1][0] = lz[i]
				lz[c + 1] = lz[i]
		lz[i] = 0


N = int(input())
arr = [0] + list(map(int, input().split()))
seg = [0] * (1 << ((N - 1).bit_length() + 1))
lz = seg[:]
init(seg, 1, N, 1)

for i in range(int(input())):
	op, *x = map(int, input().split())
	if op == 1 and seg[1][0] > x[2]: update(seg, lz, 1, N, x[0], x[1], 1, x[2])
	elif op == 2: sys.stdout.write(str(get_max(seg, lz, 1, N, x[0], x[1], 1)) + '\n')
	elif op == 3: sys.stdout.write(str(get_sum(seg, lz, 1, N, x[0], x[1], 1)) + '\n')


# 충분히 빠른데 40퍼에서 시간초과 ㅠ
