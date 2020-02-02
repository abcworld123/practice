n = int(input())
li = []
for x in range(0, n):
    li += [tuple(map(int, input().split()))]
li.sort(key=lambda x: x[1])
li.sort(key=lambda x: x[0])
for x in li: print(x[0], x[1])
