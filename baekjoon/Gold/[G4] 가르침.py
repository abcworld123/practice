from itertools import combinations

N, K = map(int, input().split()); K -= 5
arr, words = [input() for _ in range(N)], []
if K < 0: print(0); exit(0)

ans = 0
bit = {chr(x + 97): 1 << x for x in range(26)}
acint = {'a', 'c', 'i', 'n', 't'}
acint_n = sum(bit[c] for c in acint)
not_acint = set(chr(x + 97) for x in range(26)) - acint
not_acint_n = [bit[c] for c in not_acint]
for word in arr: words.append(sum(bit[c] for c in set(word)))

for comb in map(sum, combinations(not_acint_n, K)):
	n = 0
	case = acint_n | comb
	for word in words:
		if word & case == word: n += 1
	if ans < n: ans = n

print(ans)
