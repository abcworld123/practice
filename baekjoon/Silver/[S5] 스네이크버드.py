m=lambda:map(int,input().split())
N,L=m()
for x in sorted(m()):L+=L>=x
print(L)