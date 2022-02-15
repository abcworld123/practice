import sys
sys.setrecursionlimit(101000)
input = sys.stdin.readline

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


n = int(input())
inorder = list(map(int, input().split()))[::-1]
preorder = list(map(int, input().split()))[::-1]
idx = [0] * (n + 1)
ans = []

for i in range(n): idx[inorder[i]] = i
dnc(0, n - 1, 0)
print(' '.join(map(str, ans[::-1])))
