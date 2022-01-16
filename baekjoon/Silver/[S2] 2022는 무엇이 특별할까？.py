from bisect import bisect
from itertools import permutations as p

N, d = map(int, input().split())
arr = [int(''.join(map(str, x)), d) for x in p(range(d), d) if x[0] != 0]
i = bisect(arr, N)
print(arr[i] if i != len(arr) else -1)
