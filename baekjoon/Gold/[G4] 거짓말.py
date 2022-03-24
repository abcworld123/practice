import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_, *truth = map(int, input().split())
party = [list(map(int, input().split()))[1:] for _ in range(M)]
group = list(range(N + 1))

for p in party:
    x = group[p[0]]
    for i in range(1, len(p)):
        y = group[p[i]]
        for j in range(1, N + 1):
            if group[j] == y:
                group[j] = x

truth = {group[x] for x in truth}
party = [{group[x] for x in p} for p in party]
print(sum(all(t not in p for t in truth) for p in party))
