import sys
input = sys.stdin.readline

i = 1
while 1:
    rip = 0
    o, w = map(int, input().split())
    if o == w == 0: break
    while 1:
        a, b = input().split()
        if a == '#' and b == '0': break
        else: w += int(b) * (1 if a == 'F' else -1)
        if w / o <= 0: print(f'{i} RIP'); rip = 1
    if not rip:
        if 0.5 < w / o < 2: print(f'{i} :-)')
        else: print(f'{i} :-(')
    i += 1
