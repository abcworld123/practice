n,a,f=int(input()),0,1
while n>0:t=n//2-1;a+=f*(n-t-(t==-1));n=t;f^=1
print(a)