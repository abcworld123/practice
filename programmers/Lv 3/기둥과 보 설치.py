def gidung_add(arr, x, y):
    if y == 0 or arr[y - 1][x] & 1 or arr[y][x - 1] & 2 or arr[y][x] & 2:
        arr[y][x] |= 1

def gidung_del(arr, x, y):
    cant1 = arr[y + 1][x] & 1 and arr[y + 1][x - 1] & 2 == 0 and arr[y + 1][x] & 2 == 0
    cant2 = arr[y + 1][x] & 2 and (arr[y + 1][x - 1] & 2 == 0 or arr[y + 1][x + 1] & 2 == 0) and arr[y][x + 1] & 1 == 0
    cant3 = arr[y + 1][x - 1] & 2 and (arr[y + 1][x - 2] & 2 == 0 or arr[y + 1][x] & 2 == 0) and arr[y][x - 1] & 1 == 0
    if not (cant1 or cant2 or cant3):
        arr[y][x] &= ~1

def bo_add(arr, x, y):
    if arr[y - 1][x] & 1 or arr[y - 1][x + 1] & 1 or (arr[y][x - 1] & 2 and arr[y][x + 1] & 2):
        arr[y][x] |= 2

def bo_del(arr, x, y):
    cant1 = arr[y][x] & 1 and arr[y][x - 1] & 2 == 0 and arr[y - 1][x] & 1 == 0
    cant2 = arr[y][x + 1] & 1 and arr[y][x + 1] & 2 == 0 and arr[y - 1][x + 1] & 1 == 0
    cant3 = arr[y][x - 1] & 2 and arr[y][x - 2] & 2 and arr[y - 1][x - 1] & 1 == 0 and arr[y - 1][x] & 1 == 0
    cant4 = arr[y][x + 1] & 2 and arr[y][x + 2] & 2 and arr[y - 1][x + 1] & 1 == 0 and arr[y - 1][x + 2] & 1 == 0
    if not (cant1 or cant2 or cant3 or cant4):
        arr[y][x] &= ~2


def solution(n, build_frame):
    arr = [[0] * (n + 5) for _ in range(n + 2)]  # 01: 기둥, 10: 보
    for x, y, a, b in build_frame:
        x += 2
        if a == 0:
            if b == 1: gidung_add(arr, x, y)
            else: gidung_del(arr, x, y)
        elif a == 1:
            if b == 1: bo_add(arr, x, y)
            else: bo_del(arr, x, y)

    ans = []
    for x in range(n + 1):
        for y in range(n + 1):
            if not arr[y][x + 2]: continue
            if arr[y][x + 2] & 1: ans.append([x, y, 0])
            if arr[y][x + 2] & 2: ans.append([x, y, 1])
    return ans



# 예전 기록 (200508)

# # 기둥문제 1
# def solution(n, build_frame):
#     n += 1
#     arr = [[-1] * n for _ in range(n)]
#
#     for cmd in build_frame:
#         x, y, tp, do = cmd
#
#         if do == 1:
#             if tp == 0:
#                if y == 0 or (x > 0 and arr[x - 1][y] == 1) or arr[x][y] == 1 or arr[x][y - 1] == 0:
#                    arr[x][y] = 0 if arr[x][y] == -1 else 2
#             else:
#                 if arr[x][y - 1] == 0 or arr[x + 1][y - 1] == 0 or (arr[x - 1][y] == 1 and arr[x + 1][y] == 1):
#                     arr[x][y] = 1 if arr[x][y] == -1 else 2
#
#
#         else:
#
#             if tp == 0:
#
#                 if (arr[x][y + 1] == 1 and (
#                         (arr[x - 1][y + 1] == 1 and arr[x + 1][y + 1] == 1) or arr[x + 1][y] == 0)) or (
#                         arr[x - 1][y + 1] == 1 and ((arr[x - 2][y + 1] == 1 and arr[x][y + 1] == 1) or arr[x][y] == 0)):
#
#                     arr[x][y] = -1 if arr[x][y] == tp else 1
#
#
#             else:
#
#                 if not ((arr[x][y] == 2 and arr[x - 1][y] <= 0 and (
#                         arr[x][y - 1] == 1 or arr[x][y - 1] == -1))  # 내위에 기둥인데 보,기둥 없음
#
#                         or (arr[x + 1][y] == 2 and (
#                                 arr[x + 1][y - 1] == 1 or arr[x + 1][y - 1] == -1))  # 내 오른쪽 위에 기둥인데 보, 기둥 없음
#
#                         or (arr[x + 1][y] >= 1 and (arr[x + 1][y - 1] == -1 or arr[x + 1][y - 1] == 1) and (
#                                 arr[x + 2][y - 1] == -1 or arr[x + 2][y - 1] == 1))  # 내 오른쪽에 보인데 아래기둥 없음
#
#                         or (arr[x - 1][y] >= 1 and (arr[x - 1][y - 1] == -1 or arr[x - 1][y - 1] == 1) and (
#                                 arr[x][y - 1] == -1 or arr[x][y - 1] == 1))):  # 내 오른쪽에 보인데 아래기둥 없음
#
#                     arr[x][y] = -1 if arr[x][y] == tp else 0
#
#
#     answer = []
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 2: answer.append([i, j, 0]); answer.append([i, j, 1])
#             elif arr[i][j] != -1: answer.append([i, j, arr[i][j]])
#
#     return answer
#
#
#
#
# # 기둥문제 2
# def gidung(arr, n, x, y): return y == 0 or (x > 0 and arr[x - 1][y][1] == 1) or arr[x][y][1] == 1 or arr[x][y - 1][0] == 1
# def bo(arr, n, x, y): return arr[x][y - 1][0] == 1 or (x < n and arr[x + 1][y - 1][0] == 1) or ((x > 0 and arr[x - 1][y][1] == 1) and (x < n and arr[x + 1][y][1] == 1))
#
#
# def solution(n, build_frame):
#     arr = [[[0] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
#
#     for cmd in build_frame:
#         x, y, tp, do = cmd
#
#         if do == 1:  # 설치
#             if tp == 0 and gidung(arr, n, x, y): arr[x][y][0] = 1
#             elif bo(arr, n, x, y): arr[x][y][1] = 1
#
#         else:  # 삭제
#             if tp == 0:
#                 arr[x][y][0] = 0
#                 rollback = 0
#                 if arr[x][y + 1][0] == 1 and y + 1 < n:
#                     if not gidung(arr, n, x, y + 1): rollback = 1
#                 if arr[x - 1][y + 1][1] == 1 and x - 1 > 0:
#                     if not bo(arr, n, x - 1, y + 1): rollback = 1
#                 if arr[x][y + 1][1] == 1 and x < n:
#                     if not bo(arr, n, x, y + 1): rollback = 1
#                 if rollback:
#                     arr[x][y][0] = 1
#             else:
#                 arr[x][y][1] = 0
#                 rollback = 0
#                 if arr[x][y][0] == 1:
#                     if not gidung(arr, n, x, y): rollback = 1
#                 if arr[x + 1][y][0] == 1:
#                     if not gidung(arr, n, x + 1, y): rollback = 1
#                 if arr[x - 1][y][1] == 1 and x - 1 > 0:
#                     if not bo(arr, n, x - 1, y): rollback = 1
#                 if arr[x + 1][y][1] == 1 and x + 1 < n:
#                     if not bo(arr, n, x + 1, y): rollback = 1
#                 if rollback: arr[x][y][1] = 1
#
#     answer = []
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if arr[i][j][0] == 1: answer.append([i, j, 0])
#             if arr[i][j][1] == 1: answer.append([i, j, 1])
#     return answer
#
#
# a = [[0, 0, 0, 1], [0, 1, 1, 1], [2, 0, 0, 1], [1, 1, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 1, 0]]
# # a = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# n = 5
# print(solution(n, a))
#
