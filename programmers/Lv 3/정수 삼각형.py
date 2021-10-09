def solution(t):
    for i in range(1, len(t)):
        t[i - 1] = [0] + t[i - 1] + [0]
        for j in range(len(t[i])):
            t[i][j] += max(t[i - 1][j], t[i - 1][j + 1])
    return max(t[-1])
