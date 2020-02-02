n = int(input())
count = 0

for _ in range(0, n):
    d = set()
    pre = ' '
    s = input()
    for c in s:
        if c not in d: d.add(c); pre = c
        elif c != pre: count -= 1; break
    count += 1

print(count)
