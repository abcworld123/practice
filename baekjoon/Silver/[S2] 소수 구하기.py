import math

a, b = map(int, input().split())
prime = [2]
start = 0

for n in range(3, b + 1):
	ok = 1
	i = 0
	if n == a: start = len(prime)
	end = int(math.sqrt(n))
	while prime[i] <= end:
		if n % prime[i] == 0: ok = 0; break
		i += 1
	if ok: prime.append(n);

if b > 1:
	for n in prime[start:]: print(n)
