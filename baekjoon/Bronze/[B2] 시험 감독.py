N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

for i in range(len(A)):
	A[i] -= B
	if A[i] > 0:
		N += A[i] // C
		if A[i] % C: N += 1
print(N)
