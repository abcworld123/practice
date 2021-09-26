def solution(sticker):
    n = len(sticker)
    if n <= 3: return max(sticker)
    answer = 0
    sticker += sticker[:2]
    for x in range(3):
        a, b = sticker[x], sticker[x] + sticker[x + 2]
        for i in range(3 + x, n + x - 1):
            a, b = b, max(b, sticker[i] + a)
        answer = max(answer, b)
    return answer
