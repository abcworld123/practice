def solution(arr, divisor): return max(sorted(filter(lambda x: x % divisor == 0, arr)), [-1], key=lambda x: len(x))
