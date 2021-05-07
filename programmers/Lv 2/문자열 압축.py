def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        arr, comp = [s[j: j + i] for j in range(0, len(s), i)], [i]
        for j in range(1, len(arr)):
            if arr[j - 1] == arr[j]: comp[-1] += i
            else: comp.append(len(arr[j]))
        answer = min(answer, sum([x if x <= i else len(str(x // i)) + i for x in comp]))
    return answer
