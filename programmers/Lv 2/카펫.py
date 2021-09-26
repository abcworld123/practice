def solution(brown, yellow):
    for i in range(3, 1000000):
        for j in range(3, i + 1):
            if 2 * (i + j - 2) == brown and (i - 2) * (j - 2) == yellow: return [i, j]
