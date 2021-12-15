import os, io
from bisect import bisect_left
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

input()
arr = [float('inf')]

for x in map(int, input().split()):
    if arr[-1] < x: arr.append(x)
    else: arr[bisect_left(arr, x)] = x

print(len(arr))
