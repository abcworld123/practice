def solution(n):
    answer = ''
    while n:
        answer += '412'[n % 3]
        n = (n - 1) // 3
    return answer[::-1]
