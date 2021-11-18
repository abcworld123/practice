for x in range(26000000, 2 ** 25):
    if x % 1000000 == 0: print(x)
    A1 = 1 if x & (1 << 0) else 0
    B1 = 1 if x & (1 << 1) else 0
    C1 = 1 if x & (1 << 2) else 0
    D1 = 1 if x & (1 << 3) else 0
    E1 = 1 if x & (1 << 4) else 0
    A2 = 1 if x & (1 << 5) else 0
    B2 = 1 if x & (1 << 6) else 0
    C2 = 1 if x & (1 << 7) else 0
    D2 = 1 if x & (1 << 8) else 0
    E2 = 1 if x & (1 << 9) else 0
    A3 = 1 if x & (1 << 10) else 0
    B3 = 1 if x & (1 << 11) else 0
    C3 = 1 if x & (1 << 12) else 0
    D3 = 1 if x & (1 << 13) else 0
    E3 = 1 if x & (1 << 14) else 0
    A4 = 1 if x & (1 << 15) else 0
    B4 = 1 if x & (1 << 16) else 0
    C4 = 1 if x & (1 << 17) else 0
    D4 = 1 if x & (1 << 18) else 0
    E4 = 1 if x & (1 << 19) else 0
    A5 = 1 if x & (1 << 20) else 0
    B5 = 1 if x & (1 << 21) else 0
    C5 = 1 if x & (1 << 22) else 0
    D5 = 1 if x & (1 << 23) else 0
    E5 = 1 if x & (1 << 24) else 0

    line_hor = [[A1, B1, C1, D1, E1], [A2, B2, C2, D2, E2], [A3, B3, C3, D3, E3], [A4, B4, C4, D4, E4], [A5, B5, C5, D5, E5]]
    line_ver = [[A1, A2, A3, A4, A5], [B1, B2, B3, B4, B5], [C1, C2, C3, C4, C5], [D1, D2, D3, D4, D5], [E1, E2, E3, E4, E5]]
    line_dia = [[A1, B2, C3, D4, E5], [A5, B4, C3, D2, E1]]

    bingo_hor = [all(line) for line in line_hor]
    bingo_ver = [all(line) for line in line_ver]
    bingo_dia = [all(line) for line in line_dia]

    bingo_cans = set()

    if bingo_hor[0]: bingo_cans.update([0,1,2,3,4])
    if bingo_hor[1]: bingo_cans.update([5,6,7,8,9])
    if bingo_hor[2]: bingo_cans.update([10,11,12,13,14])
    if bingo_hor[3]: bingo_cans.update([15,16,17,18,19])
    if bingo_hor[4]: bingo_cans.update([20,21,22,23,24])

    if bingo_ver[0]: bingo_cans.update([0,5,10,15,20])
    if bingo_ver[1]: bingo_cans.update([1,6,11,16,21])
    if bingo_ver[2]: bingo_cans.update([2,7,12,17,22])
    if bingo_ver[3]: bingo_cans.update([3,8,13,18,23])
    if bingo_ver[4]: bingo_cans.update([4,9,14,19,24])

    if bingo_dia[0]: bingo_cans.update([0,6,12,18,24])
    if bingo_dia[1]: bingo_cans.update([4,8,12,16,20])

    canof1 = bin(x).count('1')

    a1 = not bingo_dia[1]
    b1 = (not bingo_hor[0] and not bingo_ver[1])
    c1 = bingo_dia[0]
    d1 = D4
    e1 = bingo_hor[0] or bingo_ver[4] or bingo_dia[1]
    a2 = not A4
    b2 = (True in bingo_hor) and (True in bingo_ver) and (True in bingo_dia)
    c2 = C2
    d2 = canof1 <= 17
    e2 = len(bingo_cans) % 2 == 0
    a3 = bingo_hor[2] or bingo_ver[0]
    b3 = (canof1 - len(bingo_cans)) >= 5
    c3 = (not C3) or (bingo_hor[2] or bingo_ver[2] or bingo_dia[0] or bingo_dia[1])
    d3 = bingo_ver.count(True) >= 2
    e3 = 25 - len(bingo_cans) >= 10
    a4 = not A2
    b4 = bingo_hor[1] or bingo_ver[3]
    c4 = line_ver[2].count(1) <= 3
    d4 = D1
    e4 = bingo_dia.count(True) > 0
    a5 = E5
    b5 = True  # 보류
    c5 = C5
    d5 = bingo_hor.count(True) + bingo_ver.count(True) + bingo_dia.count(True) >= 3
    e5 = A5

    correct = [a1^A1, b1^B1, c1^C1, d1^D1, e1^E1, a2^A2, b2^B2, c2^C2, d2^D2, e2^E2, a3^A3, b3^B3, c3^C3, d3^D3, e3^E3, a4^A4, b4^B4, c4^C4, d4^D4, e4^E4, a5^A5, b5^B5, c5^C5, d5^D5, e5^E5].count(0)

    # if correct == 24: print(x, correct, temp.index(1), bingo_cans)
    if correct == 25:
        for i in range(25):
            print('#' if x & (1 << i) else '.', end='')
            if (i + 1) % 5 == 0: print()
