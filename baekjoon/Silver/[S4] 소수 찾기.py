input()
c, p = 0, []
for n in range(2, 1001):
    if not [x for x in p if n % x == 0]: p += [n]
for n in map(int, input().split()):
    if n in p: c += 1
print(c)
