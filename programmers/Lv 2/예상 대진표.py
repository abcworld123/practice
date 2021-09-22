import math

def solution(n, a, b):
    return int(math.log2((a - 1) ^ (b - 1)) + 1)
