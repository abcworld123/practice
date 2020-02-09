import math

a , b = map(int, input().split())
sqrtb = math.ceil(math.sqrt(b))
prime = set(range(2, sqrtb + 1))
no_prime = set()

for x in range(2, sqrtb + 1):
    start = math.ceil(a / x)
    end = sqrtb // x
    for i in range(start + 1, end + 1):
        no_prime.add(x * i)

prime = prime - no_prime
no_ans = set()

for p in prime:
    p *= p
    start = math.ceil(a / p)
    end = b // p
    for i in range(start, end + 1):
        no_ans.add(p * i)

print(b - a + 1 - len(no_ans))
