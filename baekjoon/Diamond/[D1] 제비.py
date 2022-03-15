from fractions import Fraction

m = 10 ** 9 + 7
for s in [*open(0)][1:]:
    R, G, B, K = map(int, s.split())
    E = ((K + R) - R * Fraction(pow(B, K, m), pow(B + 1, K, m)) + K * Fraction(G, B)) % m
    print(E.numerator * pow(E.denominator, m - 2, m) % m)

# 일반항
# E = (K + R) - R * B ** K / (B + 1) ** K + K * G / B

# 기댓값이라는게 와닿지 않아서 좀 고생했다.
# 예를 들면, R=0 G=2 B=1 K=1일 때 뭔가 감각적으로는 E=1.5 같은데 실제론 E=3인 이런 케이스
# 기댓값 구하는 방법을 깨닫고 나서는 노가다로 쉽게 규칙찾고 일반항 구했다.
# G에 대한 규칙은 브루트포스 노가다로 제일 쉽게 찾았는데, AC받고 생각해보니 수학적인 증명은 이 부분이 제일 어려웠던 듯


# 전체 탐색 (무식한 방법, 검증용)
from random import randint

def jebi(arr, K):
    cnt = 0
    while K:
        i = randint(0, len(arr) - 1)
        if arr[i] == 'R':
            arr.pop(i)
        elif arr[i] == 'B':
            K -= 1
        cnt += 1
    return cnt

G = 0
n = 3000000
K = 2

for K in range(1, 6):
    print()
    print(f'{"-" * 20} K: {K} {"-" * 20}')
    for R in range(1, 6):
        line = []
        for B in range(1, 6):
            arr = ['R'] * R + ['G'] * G + ['B'] * B
            ans = []
            for _ in range(n):
                ans.append(jebi(arr[:], K))
            line.append(round(sum(ans) / n, 6))
        print(f'R: {R} -> {line}')



# 긴가민가해서 기댓값 테스트
from random import randint

cnt = 0
n = 1000000

for i in range(n):
    while 1:
        cnt += 1
        if randint(1, 3) == 3: break

print(cnt / n)



# rkaxhdals's 벌캠 😄
# 수학적으로 깨달았더니 필요없어짐..

arr = [3.421836, 3.842505, 4.264237, 4.685038, 5.106526]
ans = [100, 0, 0, 0]

# d = 13  # 값을 잘 조정
for d in range(1, 1000):
    for i in range(1, 1000):
        for j in range(1, 1000):
            cur = 0
            for k in range(0, len(arr)):
                x = (i + k * d) / j
                cur += abs(arr[k] - x)
            if cur < ans[0]:
                ans = [cur, i, j, d]
                print(*ans)

# 31/8 - 7
# 100/27 - 19
# 229/64 - 37

# 739/216 - 91
