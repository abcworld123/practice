import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


sqn = 500
N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))

M = int(input())
q = [(*map(int, input().split()), i) for i in range(M)]
q.sort(key=lambda x: (x[0] // sqn, x[1]))
q.append((N + 1, N + 1, -1))

ans = [0] * M
S, E = [0] * (K + 1), [0] * (K + 1)
s, e, i = q[0]
j = 0

for sq in range(sqn + 2):
    m = min((sq + 1) * sqn, N + 1)
    for k in range(sq * sqn, N + 1):
        S[arr[k]] = E[arr[k]] = 0
    while e < m:
        cur = 0
        for k in range(s, e + 1):
            if S[arr[k]]: cur = max(cur, k - S[arr[k]])
            else: S[arr[k]] = k
        ans[i] = cur
        for k in range(s, e + 1): S[arr[k]] = 0
        j += 1
        s, e, i = q[j]

    cur, l, r = 0, m, m - 1
    while s < m:
        while r < e:
            r += 1
            if S[arr[r]]:
                cur = max(cur, r - S[arr[r]])
                E[arr[r]] = r
            else: E[arr[r]] = S[arr[r]] = r
        t = cur
        while s < l:
            l -= 1
            if E[arr[l]]: cur = max(cur, E[arr[l]] - l)
            else: E[arr[l]] = l
        ans[i] = cur
        cur = t
        while l < m:
            if E[arr[l]] < m: E[arr[l]] = 0
            l += 1
        j += 1
        s, e, i = q[j]

os.write(1, '\n'.join(map(str, ans)).encode())


# 포문을 버킷 단위로 돈다.
# m은 바로 다음 벼킷의 시작점
# 현재 버킷 내 인덱스들의 S, E를 전부 0으로 초기화.
#
# 1. l, r 모두 하나의 버킷 내에 있을 때:
# 무식하게 일일이 구한다. 무식해보여도 반드시 O(루트n)임.
#
# 2. l이 현재 버킷 내에, r은 현재 버킷 오른쪽에 있을 때:
# 현재 버킷의 오른쪽 경계선부터는 계속 써먹을 수 있다. 왜냐하면 r이 단조증가 하기 때문.
# 대신 l은 초기화하고 무식하게 구하는 것을 반복.
#
# 이 방법의 핵심은 범위가 넓어지는 방향으로만 올바른 답이 도출된다는 것
