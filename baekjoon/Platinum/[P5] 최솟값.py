import sys

def ti(s,e,i):

	if s==e:t[i]=arr[s]
	else:
		m,i2=(s+e)//2,i*2
		t[i]=min(ti(s,m,i2),ti(m+1,e,i2+1))
	return t[i]
def tm(s,e,l,r,i):

	if s==l and e==r:return t[i]
	else:
		m,i2=(s+e)//2,i*2
		if m+1>r:return tm(s,m,l,r,i2)
		elif m<l:return tm(m+1,e,l,r,i2+1)
		else:return min(tm(s,m,l,m,i2),tm(m+1,e,m+1,r,i2+1))

arr,t=[0],[0]*262144
N,M=map(int,input().split())
for i in range(N):arr.append(int(sys.stdin.readline()))
ti(1,N,1)
for i in range(M):
	a,b=map(int,sys.stdin.readline().split())
	print(tm(1,N,a,b,1))
