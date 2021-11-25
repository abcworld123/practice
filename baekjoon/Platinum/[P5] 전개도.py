def check(a, i, j):
    check_list = [
        j<2 and all((a[i][j],a[i][j+1],a[i][j+2],a[i+1][j+2],a[i+1][j+3],a[i+1][j+4])),
        i<4 and j<3 and all((a[i][j],a[i][j+1],a[i+1][j+1],a[i+1][j+2],a[i+2][j+2],a[i+2][j+3])),
        i<4 and j<3 and all((a[i][j],a[i+1][j],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j])),
        i<4 and j<3 and all((a[i][j],a[i+1][j],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j+1])),
        i<4 and j<3 and all((a[i][j],a[i+1][j],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j+2])),
        i<4 and j<3 and all((a[i][j],a[i+1][j],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j+3])),
        i<4 and j<3 and all((a[i][j],a[i][j+1],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j+1])),
        i<4 and j<3 and all((a[i][j],a[i][j+1],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j+2])),
        i<4 and j<3 and all((a[i][j],a[i][j+1],a[i+1][j+1],a[i+1][j+2],a[i+1][j+3],a[i+2][j+3])),
        i<4 and 0<j and all((a[i][j],a[i+1][j-1],a[i+1][j],a[i+1][j+1],a[i+1][j+2],a[i+2][j+1])),
        i<4 and 0<j and all((a[i][j],a[i+1][j-1],a[i+1][j],a[i+1][j+1],a[i+1][j+2],a[i+2][j]))
    ]
    for k in range(11):
        if check_list[k]:
            if k == 0: oned = a[i][j: j + 5] + a[i + 1][j: j + 5]
            elif k >= 9: oned = a[i][j - 1: j + 3] + a[i + 1][j - 1: j + 3] + a[i + 2][j - 1: j + 3]
            else: oned = a[i][j: j + 4] + a[i + 1][j: j + 4] + a[i + 2][j: j + 4]
            print(oned[oppo[k][oned.index(1)]])
            exit()


oppo = [
    {0:2,2:0,1:8,8:1,7:9,9:7},
    {0:6,6:0,1:10,10:1,5:11,11:5},
    {0:8,8:0,4:6,6:4,5:7,7:5},
    {0:9,9:0,4:6,6:4,5:7,7:5},
    {0:10,10:0,4:6,6:4,5:7,7:5},
    {0:11,11:0,4:6,6:4,5:7,7:5},
    {0:6,6:0,1:9,9:1,5:7,7:5},
    {0:6,6:0,1:10,10:1,5:7,7:5},
    {0:6,6:0,1:11,11:1,5:7,7:5},
    {1:10,10:1,4:6,6:4,5:7,7:5},
    {1:9,9:1,4:6,6:4,5:7,7:5}
]

arr = [[list(map(int, input().split())) for _ in range(6)]]
for i in range(3): arr.append(list(zip(*arr[-1][::-1])))
for i in range(4): arr.append(arr[i][::-1])

for a in arr:
    for i in range(5):
        for j in range(4):
            check(a, i, j)
print(0)
