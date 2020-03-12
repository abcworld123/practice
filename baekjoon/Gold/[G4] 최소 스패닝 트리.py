import sys

A,C=0,1
V,E=map(int,input().split())
L,s,t=[],{},{}

for i in range(1,V+1):s[i]=0;t[i]=set()
for i in range(E):L.append(list(map(int,sys.stdin.readline().split())))
L.sort(key=lambda l:l[2])

for l in L:
	a,b,c=l
	if not(s[a]==s[b]and s[a]and s[b]):
		if s[a]==0and s[b]==0:
			s[a],s[b]=C,C
			t[C].add(a)
			t[C].add(b)
			C+=1
		elif s[a]==0:s[a]=s[b];t[s[b]].add(a)
		elif s[b]==0:s[b]=s[a];t[s[a]].add(b)
		elif s[a]!=s[b]:
			for v in t[s[b]]:s[v]=s[a];t[s[a]].add(v)
		A+=c
print(A)
