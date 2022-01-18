def mul(A, B):
    N = len(A)
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += A[i][k] * B[k][j]
            ret[i][j] %= 1000
    return ret


def mat_pow(A, n):
    if n == 1: return A
    if ~n & 1:
        B = mat_pow(A, n >> 1)
        return mul(B, B)
    else:
        return mul(mat_pow(A, n - 1), A)


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = mat_pow(arr, B)
for l in arr: print(*(x % 1000 for x in l))
