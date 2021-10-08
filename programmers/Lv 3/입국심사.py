def solution(n, times):
    answer, mid = -1, -1
    left, right = min(times) * n // len(times), max(times) * (n + 1) // len(times)

    while left <= right:
        mid = (left + right) // 2
        total = sum((mid // t for t in times))
        if total == n: answer = min(answer, mid) if answer != -1 else mid
        if total >= n: right = mid - 1
        elif total < n: left = mid + 1

    return answer if answer != -1 else mid
