def make(B,r,c,a):
	for i in range(9):r.append(list(range(i*9,(i+1)*9)))
	for i in range(9):c.append(list(range(i,i+81,9)))
	for i in range(3):
		for j in range(3):
			s=i*27+j*3
			a.append([s,s+1,s+2,s+9,s+10,s+11,s+18,s+19,s+20])
	for i in range(9):
		line=input()
		for j in range(9):
			B.append(int(line[j])if line[j]!='.'else-1)

def bprint(board):
	for i in range(9):
		for j in range(9):
			print(board[i*9+j]if board[i*9+j]!=-1else'.',end='')
		print()

def check():
	s=False
	for n in range(1,10):
		b=B[:]
		for i in range(9):
			for j in range(9):
				if b[i*9+j]==n:
					marking(b,i,j)
		for k in range(9):
			nr,nc,na=[b[x]for x in r[k]],[b[x]for x in c[k]],[b[x]for x in a[k]]
			if nr.count(0)>=1and nr.count(-1)==0and n not in nr:E()
			if nc.count(0)>=1and nc.count(-1)==0and n not in nc:E()
			if na.count(0)>=1and na.count(-1)==0and n not in na:E()
			if na.count(-1)==1:B[a[k][na.index(-1)]]=n;s=True
	return s

def marking(board,i,j):
	for k in range(9):
		if board[i*9+k]==-1:board[i*9+k]=0
		if board[k*9+j]==-1:board[k*9+j]=0
		for can in a:
			if i*9+j in can:
				for x in can:
					if board[x]==-1:board[x]=0

def E():print("ERROR");exit(0)

B,r,c,a=[],[],[],[]
make(B,r,c,a)
while check():pass
bprint(B)
