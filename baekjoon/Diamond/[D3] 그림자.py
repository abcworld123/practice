import sys
from fractions import Fraction
input = sys.stdin.readline

light = None
N, M = map(int, input().split())
pic = [[] for _ in range(8)]
half = Fraction(1, 2)
arr = []
ans = 0

for i in range(N):
    arr.append(input().rstrip())
    if not light:
        x = arr[-1].find('*')
        if x != -1: light = (i, x)

if light == None:
    print(sum([row.count('.') for row in arr]))
    exit()

tbk, bbk = light[0], N - light[0] - 1
lbk, rbk = light[1], M - light[1] - 1
max_dist = max(tbk, bbk, lbk, rbk)
for i in range(N): arr[i] = '0' * (max_dist - lbk) + arr[i] + '0' * (max_dist - rbk)
arr = ['0' * len(arr[0]) for _ in range(max_dist - tbk)] + arr + ['0' * len(arr[0]) for _ in range(max_dist - bbk)]
arr = sum([[''.join(room * 2 for room in line)] * 2 for line in arr], [])
n = len(arr) >> 1

for i in range(n):
    for j in range(8): pic[j].append([])
    for j in range(i + 1):
        pic[0][-1].append(arr[n - j - 1][n + i])
        pic[1][-1].append(arr[n - i - 1][n + j])
        pic[2][-1].append(arr[n - i - 1][n - j - 1])
        pic[3][-1].append(arr[n - j - 1][n - i - 1])
        pic[4][-1].append(arr[n + j][n - i - 1])
        pic[5][-1].append(arr[n + i][n - j - 1])
        pic[6][-1].append(arr[n + i][n + j])
        pic[7][-1].append(arr[n + j][n + i])

for p in range(8):
    sect = []
    for i in range(1, n):
        for j in range(i + 1):
            if pic[p][i][j] == '0': break
            ls = Fraction(j, i + 1)  # 왼쪽기울기
            rs = Fraction(j + 1, i)  # 오른기울기
            if pic[p][i][j] == '#':  # 벽이면
                for ii in range(len(sect)):  # 정렬 & 구간 병합
                    if sect[ii][1] < ls: continue
                    if sect[ii][0] < ls:
                        if len(sect) > ii + 1 and sect[ii + 1][0] <= rs:
                            sect[ii][1] = sect[ii + 1][1]
                            sect.pop(ii + 1)
                        elif sect[ii][1] < rs: sect[ii][1] = rs
                    elif sect[ii][0] <= rs: sect[ii][0] = ls
                    else: sect.insert(ii, [ls, rs])
                    break
                else: sect.append([ls, rs])
            else:  # 빈공간이면
                for s, e in sect:
                    if e <= ls: continue
                    elif i == j and ls < e:  # 대각선 경계선
                        ans += half
                    elif s <= ls and rs <= e:  # 둘다 포함
                        ans += 1
                    elif s <= ls < e:  # 왼쪽만 포함
                        llen = max(0, e * i - j)
                        rlen = min(1, e * (i + 1) - j)
                        tlen = max(0, i + 1 - (j + 1) / e)
                        blen = min(1, i + 1 - j / e)
                        ans += llen + (tlen + blen) * (rlen - llen) / 2
                    elif s < rs <= e:  # 오른쪽만 포함
                        llen = min(1, j + 1 - s * i)
                        rlen = max(0, j + 1 - s * (i + 1))
                        tlen = min(1, (j + 1) / s - i)
                        blen = max(0, j / s - i)
                        ans += rlen + (tlen + blen) * (llen - rlen) / 2
                    elif rs <= s: break

print(float(ans / 4))


# 풀이
# 1. 광원이 칸의 중심에 있으므로, 1칸을 4분할로 2N * 2M 크기가 되도록 변환 (최대 50x50이니 상관x)
# 2. 광원이 중심에 있도록 전체 공간을 정사각형으로 (벽 너머는 0으로 채움)
# 3. 정사각형을 피자 8조각으로 나눔
# 4. 삼각형 하나만 할 줄 알면 나머지 7조각도 같은 방법으로 처리하면 됨.
# 5. 중심부터 바깥쪽 순서대로 탐색
# 6. if '#': 기울기 구간 리스트에 추가 또는 병합 (정렬된 순서 유지)
# 7. if '.': 기울기 구간 차례대로 탐색하며, 칸의 왼쪽 하단과 오른쪽 상단의 구간이 겹치면 그림자 계산
# 8. 계산 과정은 tlen, blen, llen, rlen을 이용하는데 복잡하니 안적음
# 9. 두 구간에 의해 그림자가 만들어져도 상관없게 구현


# 아래는 작업 내역

# 전체 맵 출력
for line in arr: print(' '.join(line))

# 조각 출력
for p in range(8):
    print('p:', p)
    for l in pic[p]:
        print('[', *l, ']')
    print()

# 랜덤 테스트케이스 생성
import random

arr = [['.' if random.randint(1, 100) <= 50 else '#' for _ in range(50)] for _ in range(50)]

print(50, 50)
for x in arr: print(''.join(x))

points = sum([x.count('.') for x in arr])
print(points)

# pieces 노가다
n = 10
arr = [list(range(i + 1, n + i + 1)) for i in range(0, n * n, n)]
for x in arr: print(x)

# piece-1
for i in range(n >> 1, n):
    for j in range(n >> 1, i + 1):
        print(arr[i][j], end=' ')
    print()

# piece-2
for i in range(n >> 1, -1, -1):
    for j in range(n >> 1, n - i):
        print(arr[i][j], end=' ')
    print()

# piece-3
for i in range(n >> 1, -1, -1):
    for j in range((n >> 1) - 1, i - 1, -1):
        print(arr[i][j], end=' ')
    print()

# piece-4
for i in range(n >> 1, n):
    for j in range((n >> 1) - 1, n - i - 2, -1):
        print(arr[i][j], end=' ')
    print()

# piece-5
for i in range(n >> 1, n):
    for j in range(n >> 1, i + 1):
        print(arr[j][i], end=' ')
    print()

# piece-6
for i in range(n >> 1, -1, -1):
    for j in range(n >> 1, n - i):
        print(arr[j][i], end=' ')
    print()

# piece-7
for i in range(n >> 1, -1, -1):
    for j in range((n >> 1) - 1, i - 1, -1):
        print(arr[j][i], end=' ')
    print()

# piece-8
for i in range(n >> 1, n):
    for j in range((n >> 1) - 1, n - i - 2, -1):
        print(arr[j][i], end=' ')
    print()


# 구간 출력 (Fraction)
def printfrac(sect):
    for s in sect:
        print(f'({s[0]}, {s[1]}), ', end='')
    print()
