n = int(input())
people = []
for x in range(0, n): people += [tuple(map(int, input().split()))]

for p1 in people:
    rank = 1
    for p2 in people:
        if p1[0] < p2[0] and p1[1] < p2[1]: rank += 1
    print("%d " % rank, end='')
