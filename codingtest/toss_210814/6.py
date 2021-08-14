def solution(numOfStairs):
    arr = [0, 1, 2, 4, 7] + [0] * (numOfStairs - 4)
    for i in range(5, numOfStairs + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    return arr[numOfStairs]

# DP 사용
