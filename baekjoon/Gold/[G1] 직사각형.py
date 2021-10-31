import sys
input()
arr = []
for line in sys.stdin.readlines():
    xbl, ybl, xtr, ytr = map(int, line.split())
    sbr, stl = ybl / xtr, ytr / xbl
    arr.append([sbr, 1])
    arr.append([stl, -1])
arr.sort(key=lambda x: (x[0], -x[1]))
ans, cur = 0, 0
for x in arr:
    cur += x[1]
    if cur > ans: ans = cur
print(ans)


# 기울기로 판단
# 직선이 0도에서 90도로 회전한다 생각
# 직사각형은 오른쪽 하단, 왼쪽 상단 꼭짓점만 생각하면 됨.
# 직사각형 왼쪽 상단, 오른쪽 상단이 각각 (xtl, ytl), (xbr, ybr) 이라고 하면,
# 이 직사각형에 들어올 수 있는 기울기는 ybr/xbr ~ ytl/xtl 사이임.
# 문제는 좌표가 10억 이하이기 때문에, 순차 탐색이 불가능함
# 정렬하고, 변화가 있는 부분만 골라서 스위핑하면 충분히 가능할 듯.
