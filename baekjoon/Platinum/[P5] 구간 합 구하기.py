import sys

def ti(s,e,i):
	if s==e:t[i]=arr[s]
	else:
		m,i2=(s+e)//2,i*2
		t[i]=ti(s,m,i2)+ti(m+1,e,i2+1)
	return t[i]

def te(s,e,p,x,i):
	if s==e==p:df=x-t[i]
	else:
		m,i2=(s+e)//2,i*2
		if m+1>p:df=te(s,m,p,x,i2)
		else:df=te(m+1,e,p,x,i2+1)
	t[i]+=df
	return df

def ts(s,e,l,r,i):
	if s==l and e==r:return t[i]
	else:
		m,i2=(s+e)//2,i*2
		if m+1>r:return ts(s,m,l,r,i2)
		elif m<l:return ts(m+1,e,l,r,i2+1)
		else:return ts(s,m,l,m,i2)+ts(m+1,e,m+1,r,i2+1)


arr,t=[0],[0]*2097152
N,M,K=map(int,input().split())
for n in range(N):arr.append(int(sys.stdin.readline()))
ti(1,N,1)
for n in range(M+K):
	a,b,c=map(int,sys.stdin.readline().split())
	if a==1:te(1,N,b,c,1)
	else:print(ts(1,N,b,c,1))
