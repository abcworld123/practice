import sys

K = input()
input()

dic = {}
for i in range(1, 9):
    dic[i] = {int(K * i)}
    for j in range(1, i):
        for a in dic[i - j]:
            for b in dic[j]:
                dic[i].update([a + b, a - b, a * b])
                if b: dic[i].add(a // b)

for a in map(int, sys.stdin.readlines()):
    for i in range(1, 9):
        if a in dic[i]: print(i); break
    else: print('NO')
