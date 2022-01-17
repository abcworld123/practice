cmds = '''get X
get A
get B
get C
get D
get E
get F
get G
shl X 7
shl A 6
shl B 5
shl C 4
shl D 3
shl E 2
shl F 1
or X A
or X B
or X C
or X D
or X E
or X F
or X G
get Y
get A
get B
get C
get D
get E
get F
get G
shl Y 7
shl A 6
shl B 5
shl C 4
shl D 3
shl E 2
shl F 1
or Y A
or Y B
or Y C
or Y D
or Y E
or Y F
or Y G
get Z
get A
get B
shl Z 2
shl A 1
or Z A
or Z B
mov A X
mov B Y
mov C Z
and A Y
and B Z
and C X
mov D X
mov E Y
mov F Z
or D Y
or E Z
or F X
mov G A
and G Z
mov H A
or H B
or H C
mov I H
not I
mov J D
or J Z
and J I
or G J
not G
and H G
and I G
and B H
and E J
or B E
or B I
and C H
and F J
or C F
or C I
and A H
and D J
or A D
or A I
mov X B
mov Y C
mov Z A
or K B
or L B
or M B
or N B
or O B
or P B
or Q C
or R C
or S C
or T C
or U C
or V C
or W A
shr X 7
shr Y 7
shr Z 2
shr K 6
shr L 5
shr M 4
shr N 3
shr O 2
shr P 1
shr Q 6
shr R 5
shr S 4
shr T 3
shr U 2
shr V 1
shr W 1
and A 1
and B 1
and C 1
and K 1
and L 1
and M 1
and N 1
and O 1
and P 1
and Q 1
and R 1
and S 1
and T 1
and U 1
and V 1
and W 1
and Z 1
put X
put K
put L
put M
put N
put O
put P
put B
put Y
put Q
put R
put S
put T
put U
put V
put C
put Z
put W
put A'''

# 테스트용 코드
reg = {x: 0 for x in [chr(c) for c in range(65, 91)]}

while 1:
    inp = input()
    i = iter(inp)
    ans = ''

    for l in cmds.split('\n'):
        if not l: continue
        l = l.split()
        cmd, R = l[0], l[1]

        if cmd == 'not':
            reg[R] = reg[R] ^ ((1 << 8) - 1)
            continue

        if cmd == 'get':
            reg[R] = int(next(i))
            continue

        if cmd == 'put':
            ans += str(reg[R])
            continue

        X = l[2]

        if cmd == 'mov':
            reg[R] = int(X) if X.isdigit() else reg[X]

        elif cmd == 'and':
            reg[R] &= int(X) if X.isdigit() else reg[X]

        elif cmd == 'or':
            reg[R] |= int(X) if X.isdigit() else reg[X]

        elif cmd == 'xor':
            reg[R] ^= int(X) if X.isdigit() else reg[X]

        elif cmd == 'shl':
            reg[R] <<= int(X) if X.isdigit() else reg[X]
            reg[R] &= ((1 << 8) - 1)

        elif cmd == 'shr':
            reg[R] >>= int(X) if X.isdigit() else reg[X]

    print(ans)
    if '0' in bin(int(inp, 2) ^ int(ans, 2))[2:]: print('no')


# A: x & y -> ~z
# B: y & z -> ~x
# C: z & x -> ~y
# D: x | y
# E: y | z
# F: z | x
# G: ex3 -> ex13 -> ex02
# H: lst2 -> ex2
# I: mst1 -> ex0
# J: ex1
#
# B (8) -> C (8) -> A (3)
# put() -> X KLMNOP B -> Y QRSTUV C -> Z W A
