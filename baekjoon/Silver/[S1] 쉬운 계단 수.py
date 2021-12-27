d=[[0]+[1]*9]
for _ in range(int(input())-1):d.append([d[-1][1]]+[d[-1][j]+d[-1][j+2]for j in range(8)]+[d[-1][8]])
print(sum(d[-1])%1000000000)