from collections import defaultdict
import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = None
        self.b = None
        self.c = None
        self.d = None
    def __repr__(self): return f'{self.x} {self.y}'


N, K = map(int, input().split())
jump = input().decode().rstrip()
dic1, dic2 = defaultdict(list), defaultdict(list)

x, y = map(int, input().split())
frog = Node(x, y)
dic1[y - x].append(frog)
dic2[x + y].append(frog)

for _ in range(N - 1):
    x, y = map(int, input().split())
    node = Node(x, y)
    dic1[y - x].append(node)
    dic2[x + y].append(node)

for arr in dic1.values():
    if len(arr) <= 1: continue
    arr.sort(key=lambda e: e.n)
    arr[0].arr = arr[1]
    arr[-1].d = arr[-2]
    for i in range(1, len(arr) - 1):
        arr[i].arr = arr[i + 1]
        arr[i].d = arr[i - 1]

for arr in dic2.values():
    if len(arr) <= 1: continue
    arr.sort(key=lambda e: e.n)
    arr[0].b = arr[1]
    arr[-1].c = arr[-2]
    for i in range(1, len(arr) - 1):
        arr[i].b = arr[i + 1]
        arr[i].c = arr[i - 1]


for d in jump:
    if d == 'A':
        if not frog.a: continue
        to = frog.a; to.d = frog.d
        if frog.b: frog.b.c = frog.c
        if frog.c: frog.c.b = frog.b
        if frog.d: frog.d.arr = frog.a
        frog = to
    elif d == 'B':
        if not frog.b: continue
        if frog.a: frog.a.d = frog.d
        to = frog.b; to.c = frog.c
        if frog.c: frog.c.b = frog.b
        if frog.d: frog.d.arr = frog.a
        frog = to
    elif d == 'C':
        if not frog.c: continue
        if frog.a: frog.a.d = frog.d
        if frog.b: frog.b.c = frog.c
        to = frog.c; to.b = frog.b
        if frog.d: frog.d.arr = frog.a
        frog = to
    else:
        if not frog.d: continue
        if frog.a: frog.a.d = frog.d
        if frog.b: frog.b.c = frog.c
        if frog.c: frog.c.b = frog.b
        to = frog.d; to.arr = frog.a
        frog = to

print(frog.x, frog.y)
