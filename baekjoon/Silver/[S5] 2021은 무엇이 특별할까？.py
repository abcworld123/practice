from bisect import bisect

p = [x for x in range(2, 104) if all((x % y for y in range(2, x)))]
arr = [p[i] * p[i + 1] for i in range(26)]

print(arr[bisect(arr, int(input()))])
