def solution(arr):
    answer = [-1]
    for c in arr:
        if c != answer[-1]: answer.append(c)
    return answer[1:]
