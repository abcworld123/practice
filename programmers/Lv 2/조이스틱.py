def solution(name):
    min_click = list(range(13)) + list(range(13, 0, -1))
    arr = [min_click[ord(c) - 65] for c in name]
    answer, cur, l = arr[0], 0, len(name)
    arr[0] = 0
    for i in range(l - arr.count(0)):
        for j in range(1, l // 2 + 1):
            left, right = (cur - j) % l, (cur + j) % l
            if arr[left] or arr[right]:
                cur = right if arr[right] else left
                answer += arr[cur] + j
                arr[cur] = 0
                break
    return answer
