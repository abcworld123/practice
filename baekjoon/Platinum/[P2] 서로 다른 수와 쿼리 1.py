import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    comp = {x: i for i, x in enumerate(sorted(set(arr)), start=1)}
    for i in range(len(arr)): arr[i] = comp[arr[i]]
    arr = [0] + arr

    idx = [0] * (N + 1)
    prev = [0] * (len(comp) + 1)
    for i in range(1, N + 1):
        idx[i] = prev[arr[i]]
        prev[arr[i]] = i
    del prev

    M = int(input())
    queries = [[*map(int, input().split()), i] for i in range(M)]
    queries.sort(key=lambda x: x[1])
    ans = [0] * len(queries)
    fw = [0] * (N + 1)
    e = 0

    for l, r, i in queries:
        while e < r:
            e += 1
            if idx[e]:
                j = idx[e]
                while j <= N: fw[j] += 1; j += j & -j
        a, b = 0, 0
        area = r - l + 1
        l -= 1
        while r: a += fw[r]; r -= r & -r
        while l: b += fw[l]; l -= l & -l
        ans[i] = area - (a - b)

    os.write(1, '\n'.join(map(str, ans)).encode())

main()
