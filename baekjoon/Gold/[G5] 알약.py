import math
f=math.factorial
while 1:
    x=int(input())
    if x==0:break
    print(f(2*x)//(f(x)*f(x+1)))
