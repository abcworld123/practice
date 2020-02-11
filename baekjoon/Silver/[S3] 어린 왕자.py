T = int(input())

for t in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    count = 0
    for i in range(n): planets.append(list(map(int, input().split())))
    for p in planets:
        r = p[2] ** 2
        d1 = (x1 - p[0]) ** 2 + (y1 - p[1]) ** 2
        d2 = (x2 - p[0]) ** 2 + (y2 - p[1]) ** 2
        if (d1 - r) * (d2 - r) < 0: count += 1
    print(count)
