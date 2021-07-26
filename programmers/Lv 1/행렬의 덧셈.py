def solution(a, b): return [[a[i][j] + b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
