def Z(rs, re, cs, ce, q, i):
    if re - rs == 1 and ce - cs == 1: return i
    rm, cm = (rs + re) >> 1, (cs + ce) >> 1
    if r < rm: re = rm
    else: rs = rm; i += q * 2
    if c < cm: ce = cm
    else: cs = cm; i += q
    return Z(rs, re, cs, ce, q >> 2, i)

N, r, c = map(int, input().split())
print(Z(0, 1 << N, 0, 1 << N, 1 << (2 * (N - 1)), 0))
