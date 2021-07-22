def solution(n, lost, reserve):
    me = []
    for r in reserve:
        if r in lost: me.append(r)
    for m in me:
        lost.remove(m)
        reserve.remove(m)
    for r in sorted(reserve):
        if r - 1 in lost: lost.remove(r - 1)
        elif r + 1 in lost: lost.remove(r + 1)
    return n - len(lost)
