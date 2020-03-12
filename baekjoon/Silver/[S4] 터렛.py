p=print
for i in '.'*int(input()):
	a,b,c,x,y,z=map(int,input().split())
	d=(x-a)**2+(y-b)**2
	if c==z and d==0:p(-1)
	elif(c+z)**2==d or(c-z)**2==d:p(1)
	elif(c-z)**2<d<(c+z)**2:p(2)
	else:p(0)
