import sys
input = sys.stdin.readline

for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * N
    visited = [0] * (N + 1)

    try:
        for i in range(N - 1, -1, -1):
            j = 1
            while arr[i]:
                while visited[j]: j += 1
                arr[i] -= 1
                j += 1
            while visited[j]: j += 1
            visited[j] = 1
            ans[i] = j
        print(' '.join(map(str, ans)))
    except:
        print('IMPOSSIBLE')
