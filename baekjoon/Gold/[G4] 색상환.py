from math import comb

N, K = map(int, open(0))
print((2 * comb(N - K, K) - comb(N - K - 1, K)) % 1000000003)
