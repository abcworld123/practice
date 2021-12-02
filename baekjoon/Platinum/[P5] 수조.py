import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    b, h, w, d = map(int, input().split())
    arr.append((b, w * d))
    arr.append((b + h, -w * d))
arr.sort()

water = int(input())
cw, cy, ca = 0, 0, 0

for l in arr:
    new = (l[0] - cy) * ca
    if cw + new >= water:
        print(f'{cy + round((water - cw) / ca, 2):.2f}')
        exit()
    cw += new
    cy = l[0]
    ca += l[1]

print('OVERFLOW')
