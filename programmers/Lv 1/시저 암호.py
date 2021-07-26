def solution(s, n):
    answer = ''
    cap = list(map(chr, range(65, 91)))
    low = list(map(chr, range(97, 123)))
    for i in range(len(s)):
        if s[i].isupper(): answer += cap[(cap.index(s[i]) + n) % 26]
        elif s[i].islower(): answer += low[(low.index(s[i]) + n) % 26]
        else: answer += s[i]
    return answer
