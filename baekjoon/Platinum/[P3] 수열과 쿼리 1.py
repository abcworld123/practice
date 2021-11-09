import sys
from bisect import bisect_right
input = sys.stdin.readline


def init(mstree, start, end, i):
    if start == end: mstree[i] = [arr[start]]
    else:
        mstree[i] = []
        mid, child = (start + end) >> 1, i << 1
        left, right = init(mstree, start, mid, child), init(mstree, mid + 1, end, child + 1)
        l, r, L, R = 0, 0, len(left), len(right)
        while l < L or r < R:
            if l < L and r < R:
                if left[l] <= right[r]: mstree[i].append(left[l]); l += 1
                else: mstree[i].append(right[r]); r += 1
            elif l >= L: mstree[i].append(right[r]); r += 1
            else: mstree[i].append(left[l]); l += 1
    return mstree[i]


def find(mstree, start, end, left, right, val, i):
    if right < start or left > end: return 0
    if start == end: return 1 if mstree[i][0] > val else 0
    if left <= start and end <= right: return len(mstree[i]) - bisect_right(mstree[i], val)
    mid, child = (start + end) >> 1, i << 1
    return find(mstree, start, mid, left, right, val, child) + find(mstree, mid + 1, end, left, right, val, child + 1)


N = int(input())
arr = [0] + list(map(int, input().split()))
mstree = [0] * (1 << (N.bit_length() + 1))
init(mstree, 1, N, 1)

for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(find(mstree, 1, N, a, b, c, 1))
