def check():
    cur = sum(cnt[x] for x in n)
    return cur + (l - 1 - i) * 2 <= ans <= cur + (l - 1 - i) * 7

n = input()
N, l = int(n), len(n)
cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5, 0]
ans = sum(cnt[int(x)] for x in n)
n = list(map(int, str(int(n) + 1).zfill(l)))[-l:]
i, j, flag = 0, 0, 0

for i in range(l - 1, -1, -1):
    for j in range(n[i], 10):
        n[i] = j
        if check(): flag = 1; break
    if flag: break
    n[i] = 10
    if i: n[i - 1] += 1

for i in range(i + flag, l):
    for j in range(10):
        n[i] = j
        if check(): break

n = int(''.join(map(str, n)))
if n <= N: n += 10 ** l
print(n - N)


# 1020번 문제 *^_^*
