import math

for i in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    a = int(math.sqrt(d))
    if d > a**2 + a: a += 1
    print(2*a - 1) if d <= a**2 else print(2*a)
