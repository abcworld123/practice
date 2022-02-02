from itertools import permutations

def solution(n, weak, dist):
    dl = len(dist)
    per = list(permutations(dist))
    ans = 99
    for _ in range(len(weak)):
        for d in per:
            di = 0
            cur = weak[0]
            for w in weak:
                if w - cur > d[di]:
                    di += 1
                    cur = w
                    if di == dl: break
            else:
                ans = min(ans, di + 1)
        weak.append(weak.pop(0) + n)

    return ans if ans != 99 else -1

print(solution(12,	[1, 3, 4, 9, 10],	[12]))
