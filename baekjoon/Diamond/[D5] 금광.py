import os, io
from collections import defaultdict
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def init(leaf, s, e, i):
    if s == e: leaf[s] = i
    else:
        init(leaf, s, (s + e) // 2, i * 2)
        init(leaf, (s + e) // 2 + 1, e, i * 2 + 1)


def main():
    golds = [list(map(int, input().split())) for _ in range(int(input()))]
    comp = {x: c for c, x in enumerate(sorted(set(g[0] for g in golds)), start=1)}
    n = len(comp)
    seg_size = 1 << ((n - 1).bit_length() + 1)
    leaf = [0] * seg_size
    floor = defaultdict(list)
    init(leaf, 1, n, 1)

    for g in golds:
        x, y, v = g
        floor[y].append((leaf[comp[x]], v))

    floor = [g[1] for g in sorted(floor.items(), key=lambda x: x[0])]
    len_floor = len(floor)
    ans = 0

    for i in range(len_floor):
        if all(g[1] <= 0 for g in floor[i]): continue
        seg = [[0, 0, 0, 0] for _ in range(seg_size)]
        j = i
        while j < len_floor:
            for k, v in floor[j]:
                seg[k] = (seg[k][0] + v,) * 4
                k //= 2
                while k:
                    cur, L, R = seg[k], seg[k * 2], seg[k * 2 + 1]
                    cur[0] = L[0] if L[0] > L[3] + R[0] else L[3] + R[0]
                    cur[1] = R[1] if R[1] > R[3] + L[1] else R[3] + L[1]
                    cur[2] = max(L[2], R[2], L[1] + R[0])
                    cur[3] = L[3] + R[3]
                    k //= 2
            if ans < seg[1][2]: ans = seg[1][2]
            j += 1
    print(ans)


if __name__ == '__main__': main()


# 극한의 최적화 했다..
# 1. fastio (N <= 3000이라 큰 효과는 x)
# 2. main()으로 실행 (지역변수 속도 > 전역변수 속도)
# 3. update 함수 부분을 메인함수에서 다 처리 (함수 호출 오버헤드)
# 4. 세그트리 리프 노드의 위치를 미리 계산해서 bottom-up으로 (트리 모양은 top-down 모양)
# 5. 되도록 max() 안쓰도록 (함수 호출 오버헤드)
# 6. seg[ch][1] 등과 같은 이중 탐색을 자제하도록 L = seg[ch] 하고 L[1]로
