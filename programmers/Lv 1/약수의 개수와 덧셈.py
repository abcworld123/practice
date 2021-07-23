def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        yaksu = 1
        for j in range(1, n // 2 + 1):
            if n % j == 0: yaksu += 1
        answer += n if yaksu % 2 == 0 else -n
    return answer
