def solution(n, m, x, y, queries):
    area = [[x, y], [x, y]]
    for q in queries[::-1]:
        if q[0] == 0:
            if area[0][1] + q[1] > m - 1: return 0
            area[1][1] = min(area[1][1] + q[1], m - 1)
            if area[0][1] != 0: area[0][1] = min(area[0][1] + q[1], m - 1)
        elif q[0] == 1:
            if area[1][1] - q[1] < 0: return 0
            area[0][1] = max(area[0][1] - q[1], 0)
            if area[1][1] != m - 1: area[1][1] = max(area[1][1] - q[1], 0)
        elif q[0] == 2:
            if area[0][0] + q[1] > n - 1: return 0
            area[1][0] = min(area[1][0] + q[1], n - 1)
            if area[0][0] != 0: area[0][0] = min(area[0][0] + q[1], n - 1)
        elif q[0] == 3:
            if area[1][0] - q[1] < 0: return 0
            area[0][0] = max(area[0][0] - q[1], 0)
            if area[1][0] != n - 1: area[1][0] = max(area[1][0] - q[1], 0)

    return (area[1][0] - area[0][0] + 1) * (area[1][1] - area[0][1] + 1)


print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))

# 0: 왼쪽
# 1: 오른쪽
# 2: 위
# 3: 아래

# 예제 2번 안됨, 근데 채점은 다맞음
