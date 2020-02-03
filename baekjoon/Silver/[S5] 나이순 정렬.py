n = int(input())
people = []
for _ in range(0, n): people += [input().split()]
people.sort(key=lambda x: int(x[0]))
for p in people: print(p[0], p[1])
