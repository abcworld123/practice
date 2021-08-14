t = [0] * 2147483648

def ti(s, e, i, arr):
    if s == e:
        t[i] = arr[s]
    else:
        m, i2 = (s + e) // 2, i * 2
        t[i] = max(ti(s, m, i2, arr), ti(m + 1, e, i2 + 1, arr))
    return t[i]


def tm(s, e, l, r, i):
    if s == l and e == r:
        return t[i]
    else:
        m, i2 = (s + e) // 2, i * 2
        if m + 1 > r:
            return tm(s, m, l, r, i2)
        elif m < l:
            return tm(m + 1, e, l, r, i2 + 1)
        else:
            return max(tm(s, m, l, m, i2), tm(m + 1, e, m + 1, r, i2 + 1))


def solution(fruitWeights, k):
    answer = set()
    fruitWeights = [0] + fruitWeights
    N, M = len(fruitWeights) - 1, 3
    ti(1, N, 1, fruitWeights)
    for i in range(1, N - k + 2):
        answer.add(tm(1, N, i, i + k - 1, 1))
    return sorted(list(answer), reverse=True)

# 세그먼트 트리 사용


# ↓시간초과 뜨고 폐기한 코드↓
# def solution(fruitWeights, k):
#     answer = set()
#     for i in range(0, len(fruitWeights) - k + 1):
#         answer.add(max(fruitWeights[i]))
#     answer = sorted(list(answer), reverse=True)
#     return answer
