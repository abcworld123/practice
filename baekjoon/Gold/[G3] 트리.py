import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(1010)

def dnc(l, r, i):
    if l == r:
        ans.append(preorder[i])
        return i
    m = idx[preorder[i]]
    p = preorder[i]
    if l < m:
        i = dnc(l, m - 1, i + 1)
    if m < r:
        i = dnc(m + 1, r, i + 1)
    ans.append(p)
    return i

for T in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    idx = [0] * (n + 1)
    ans = []

    for i in range(n): idx[inorder[i]] = i
    dnc(0, n - 1, 0)
    print(' '.join(map(str, ans)))
