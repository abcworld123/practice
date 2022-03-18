_len = 40

# dec to tri
def dtot(x):
    ret = ''
    if x < 0: x += 3 ** 40
    # print(x)
    while x:
        ret += str(x % 3)
        x //= 3
    return ret[::-1] or '0'

# const to list
def ctol(x):
    if x[:2] == '0t': return atol(dtot(int(x[2:], 3)))
    else: return atol(dtot(int(x)))

# str num to list
def atol(x):
    return list(map(int, x[-_len:].zfill(_len)))

# for [add, sub, mul, div, mod]
def oper(a, b, op):
    a10 = int(''.join(map(str, a)), 3)
    b10 = int(''.join(map(str, b)), 3)
    print(a10, b10)
    c = atol(dtot(op(a10, b10)))
    return c

def _add(a, b):
    return oper(a, b, int.__add__)

def _sub(a, b):
    return oper(a, b, int.__sub__)

def _mul(a, b):
    return oper(a, b, int.__mul__)

def _div(a, b):
    return oper(a, b, int.__floordiv__)

def _mod(a, b):
    return oper(a, b, int.__mod__)

def _and(a, b):
    return [min(a[i], b[i]) for i in range(_len)]

def _or(a, b):
    return [max(a[i], b[i]) for i in range(_len)]

def _xor(a, b):
    return [(a[i] + b[i]) % 3 for i in range(_len)]

def _not(a):
    return [2 - a[i] for i in range(_len)]

def _lshift(a, x):
    x = int(''.join(map(str, x)), 3)
    return a[x:] + [0] * x if x else a[:]

def _rshift(a, x):
    x = int(''.join(map(str, x)), 3)
    return [0] * x + a[:-x] if x else a[:]

########################################################

# X = 0t0011222112010021000000000000000000000000

arr = '''
X = 0t0000000000000000000000000000000000000000

A = X
B = A >> 1
A = A | B
B = A >> 2
A = A | B
B = A >> 4
A = A | B
B = A >> 8
A = A | B
B = A >> 16
A = A | B
B = A >> 32
A = A | B

A = ~ A
A = A ^ X
A = ~ A
B = A >> 1
A = A | B
B = A >> 2
A = A | B
B = A >> 4
A = A | B
B = A >> 8
A = A | B
B = A >> 16
A = A | B
B = A >> 32
A = A | B

A = ~ A
A = A ^ 6078832729528464400
B = A >> 1
A = A | B
B = A >> 2
A = A | B
B = A >> 4
A = A | B
B = A >> 8
A = A | B
B = A >> 16
A = A | B
B = A >> 32
A = A | B

B = A & 2
B = B % 2
B = B + 1
X = A * B

A = 31

B = X >> A
B = B & 2
D = D | B
C = B * 16
Y = Y + C
B = B - 1
B = B * 16
A = A + B

B = X >> A
B = B & 2
D = D | B
C = B * 8
Y = Y + C
B = B - 1
B = B * 8
A = A + B

B = X >> A
B = B & 2
D = D | B
C = B * 4
Y = Y + C
B = B - 1
B = B * 4
A = A + B

B = X >> A
B = B & 2
D = D | B
C = B * 2
Y = Y + C
B = B - 1
B = B * 2
A = A + B

B = X >> A
B = B & 2
D = D | B
C = B * 1
Y = Y + C
B = B - 1
B = B * 1
A = A + B

B = X >> A
B = B & 2
D = D | B
C = B / 2
Y = Y + C
B = B - 1
B = B * 1
A = A + B

Y = 40 - Y


'''
# A = A ^ 0t1111111111111111111111111111111111111111
# A = A ^ 0t2222222222222222222222222222222222222222

arr = arr.splitlines()
while '' in arr: arr.remove('')
reg = {chr(c): [0] * 40 for c in range(65, 91)}
# print(arr)

for cmd in arr:
    cmd = cmd.split()
    print(cmd)
    if len(cmd) == 3:
        x, a = cmd[0], cmd[2]
        a = reg[a] if a.isupper() else ctol(a)
        reg[x] = a[:]
    elif len(cmd) == 4:
        x, a = cmd[0], cmd[3]
        a = reg[a] if a.isupper() else ctol(a)
        reg[x] = _not(a)
    else:
        x, a, b = cmd[0], cmd[2], cmd[4]
        a = reg[a] if a.isupper() else ctol(a)
        b = reg[b] if b.isupper() else ctol(b)
        if cmd[3] == '+':
            reg[x] = _add(a, b)
        elif cmd[3] == '-':
            reg[x] = _sub(a, b)
        elif cmd[3] == '*':
            reg[x] = _mul(a, b)
        elif cmd[3] == '/':
            reg[x] = _div(a, b)
        elif cmd[3] == '%':
            reg[x] = _mod(a, b)
        elif cmd[3] == '&':
            reg[x] = _and(a, b)
        elif cmd[3] == '|':
            reg[x] = _or(a, b)
        elif cmd[3] == '^':
            reg[x] = _xor(a, b)
        elif cmd[3] == '<<':
            reg[x] = _lshift(a, b)
        elif cmd[3] == '>>':
            reg[x] = _rshift(a, b)

    # print()
    print('X', ''.join(map(str, reg['X'])), f" ({int(''.join(map(str, reg['X'])), 3)})")
    print('A', ''.join(map(str, reg['A'])), f" ({int(''.join(map(str, reg['A'])), 3)})")
    print('B', ''.join(map(str, reg['B'])), f" ({int(''.join(map(str, reg['B'])), 3)})")
    print('D', ''.join(map(str, reg['D'])), f" ({int(''.join(map(str, reg['D'])), 3)})")
    print('Y', ''.join(map(str, reg['Y'])), f" ({int(''.join(map(str, reg['Y'])), 3)})")
    print()
