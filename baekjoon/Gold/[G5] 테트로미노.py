import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sum([list(map(int, input().split())) + [0] * 3 for _ in range(N)] + [[0] * (M + 3)] * 3, [])
y = M + 3
ans = 0

for i in range(N):
    for j in range(M):
        A=i*y+j;B,C,D,E=A+1,A+2,A+3,A+y;F,G,H=E+1,E+2,E+y;I,J=H+1,H+y
        for a,b,c,d in ((A,B,C,D),(A,E,H,J),(A,E,F,G),(C,E,F,G),(A,B,C,E),(A,B,C,G),(A,E,H,I),(B,F,H,I),(A,B,E,H),(A,B,F,I),(A,E,F,H),(B,E,F,I),(B,E,F,G),(A,B,C,F),(B,C,E,F),(A,B,F,G),(A,E,F,I),(B,E,F,H),(A,B,E,F)):
            S = arr[a] + arr[b] + arr[c] + arr[d]
            if ans < S: ans = S

print(ans)
