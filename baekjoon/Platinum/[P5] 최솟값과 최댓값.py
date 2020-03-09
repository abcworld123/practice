import sys

def ti(s,e,i):
	if s==e:t[i]=[r[s],r[s]]
	else:
		m,i2=(s+e)//2,i*2
		lc,rc=ti(s,m,i2),ti(m+1,e,i2+1)
		t[i]=[min(lc[0],rc[0]),max(lc[1],rc[1])]
	return t[i]

def tm(s,e,l,r,i):
	if s==l and e==r:return t[i]
	else:
		m,i2=(s+e)//2,i*2
		if m+1>r:return tm(s,m,l,r,i2)
		elif m<l:return tm(m+1,e,l,r,i2+1)
		else:
			lc,rc=tm(s,m,l,m,i2),tm(m+1,e,m+1,r,i2+1)
			return[min(lc[0],rc[0]),max(lc[1],rc[1])]

r,t=[0],[0]*262144
N,M=map(int,input().split())
for i in range(N):r.append(int(sys.stdin.readline()))
ti(1,N,1)
for i in range(M):
	a,b=map(int,sys.stdin.readline().split())
	res=tm(1,N,a,b,1)
	print(res[0],res[1])
