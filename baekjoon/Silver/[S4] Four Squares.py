def p(n): print(n); exit()

n = int(input())

sq = {x * x for x in range(1, 224)}
if n in sq: p(1)

sq2 = {x + y for x in sq for y in sq if x + y <= 50000}
if n in sq2: p(2)

for x in sq:
    if n > x and n - x in sq2: p(3)

p(4)
