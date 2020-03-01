def f(n):
	if n=='-1':return 0
	a=[0]*10
	h=len(n)
	for i in range(1,h+1):
		l=int(n[:h-i])if n[:h-i]!=''else 0
		m=int(n[-i])
		r=int(n[-i+1:])if i>1else 0
		for j in range(10):a[j]+=l*10**(i-1)
		for j in range(m):a[j]+=10**(i-1)
		a[m]+=r+1
		a[0]-=10**(i-1)
	x=0
	for i in range(10):x+=a[i]*i
	return x

x,y=input().split()
print(f(y)-f(str(int(x)-1)))
