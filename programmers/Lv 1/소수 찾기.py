def solution(n):
    arr = [0, 0] + [1] * (n - 1)
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            arr[j] = 0
    return arr.count(1)


# 극한의 최적화 버전
# def solution(n):
#     li = [False] + [True] * ((n - 1) // 2)
#     for x in range(1, int(n ** .5 / 2 + 1)):
#         if li[x]:
#             li[2 * x * (x + 1)::x * 2 + 1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
#     return len([x for x, val in zip(range(0, n + 1, 2), li[:]) if val]) + 1
