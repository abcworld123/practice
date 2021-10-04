def solution(N, number):
    dic = {}
    for i in range(1, 9):
        dic[i] = {int(str(N) * i)}
        for j in range(1, i):
            for a in dic[i - j]:
                for b in dic[j]:
                    dic[i].update([a + b, a - b, a * b])
                    if b: dic[i].add(a // b)
        if number in dic[i]: return i
    return -1

# [1]: { 5 }
# [2]: { [1] □ [1], 55 }
# [3]: { [1] □ [2], [2] □ [1], 555 }
# [4]: { [1] □ [3], [2] □ [2], [3] □ [1], 5555 }
