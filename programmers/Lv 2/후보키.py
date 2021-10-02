from itertools import combinations

def solution(relation):
    cdn, ok = len(relation), []
    for i in range(1, len(relation[0]) + 1):
        for c in combinations(range(len(relation[0])), i):
            setc = set(c)
            if not any([o.issubset(setc) for o in ok]):
                s = set(' '.join([x[y] for y in c]) for x in relation)
                if len(s) == cdn: ok.append(setc)
    return len(ok)
