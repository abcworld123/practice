def solution(citations):
    citations.sort()
    cur, h, length = -1, 0, len(citations)
    for i in range(length):
        if cur < citations[i]:
            for j in range(cur + 1, citations[i] + 1):
                if i <= j <= length - i: h = j
            cur = citations[i]
    return h
