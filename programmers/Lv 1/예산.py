def solution(d, budget):
    for i, x in enumerate(sorted(d)):
        budget -= x
        if budget < 0: return i
    return len(d)
