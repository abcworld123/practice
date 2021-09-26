def solution(n):
    a, b = 0, 0
    for i in range(1, n): a, b = b, a + b
    return b % 1234567
