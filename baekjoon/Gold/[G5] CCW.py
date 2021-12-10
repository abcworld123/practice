a,b,c,d,e,f=map(int,open(0).read().split())
x=(c-a)*(f-b)-(e-a)*(d-b)
print(x and x//abs(x))