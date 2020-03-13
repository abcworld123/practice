import sys
sys.setrecursionlimit(1001)
def f(v):
	U,R,D,L=v-M,v+1,v+M,v-1
	if c[v]==-1:
		c[v]=0
		if U>=0and m[U]<m[v]:c[v]+=f(U)
		if R%M and m[R]<m[v]:c[v]+=f(R)
		if D<N*M and m[D]<m[v]:c[v]+=f(D)
		if L%M!=M-1and m[L]<m[v]:c[v]+=f(L)
	return c[v]

m=[]
N,M=map(int,input().split())
for i in range(N):m+=[x for x in map(int,input().split())]
c=[-1for x in range(N*M)]
c[-1]=1
f(0)
print(c[0])
