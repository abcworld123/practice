prime = list(range(2, 1001))
for x in range(2, 32):
    for p in prime:
        if p != x and p % x == 0:prime.remove(p)
input()
nums = map(int, input().split())
count = 0
for x in nums:
    if x in prime: count += 1
print(count)
