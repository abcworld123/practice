def convert(num, base):
    q, r = divmod(num, base)
    if q == 0: return str(r)
    else: return convert(q, base) + str(r)

def solution(n): return int(convert(n, 3)[::-1], 3)
