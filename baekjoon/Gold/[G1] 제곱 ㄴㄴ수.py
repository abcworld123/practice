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



# 개선 버전
def make_m(b):
    sqrtb = int(b ** .5)
    m = [0] + [1] * sqrtb
    for i in range(2, sqrtb + 1):
        if m[i] == 0: continue
        for j in range(2 * i, sqrtb + 1, i):
            m[j] -= m[i]
    return m


def count(m, k):
    x = 0
    for i in range(2, int(k ** .5) + 1):
        if m[i] == 0: continue
        else: x += m[i] * (k // (i * i))
    return k - x


a, b = map(int, input().split())
m = make_m(b)
print(count(m, b) - count(m, a - 1))
