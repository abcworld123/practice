def solution(n): return sum((n % x == 0) * x for x in range(1, n + 1))
