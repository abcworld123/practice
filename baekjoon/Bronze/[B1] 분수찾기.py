N=int(input())-1
r=int((2*N+.25)**.5+.5)
x=r*-~r//2
print('%d/%d'%(r-x+N+1,x-N)[::1-r%2*2])