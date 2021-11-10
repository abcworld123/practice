import sys
from collections import Counter
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = (Counter((arr[start],)), (arr[start], 1))
    else:
        mid, child = (start + end) >> 1, i << 1
        node = init(segtree, start, mid, child)[0] + init(segtree, mid + 1, end, child + 1)[0]
        segtree[i] = (node, node.most_common(1)[0])
    return segtree[i]


def get(segtree, start, end, left, right, i, counters, cands):
    if left <= start and end <= right:
        counters.append(segtree[i][0])
        cands.add(segtree[i][1][0])
    else:
        mid, child = (start + end) >> 1, i << 1
        if left <= mid: get(segtree, start, mid, left, right, child, counters, cands)
        if mid + 1 <= right: get(segtree, mid + 1, end, left, right, child + 1, counters, cands)


N, C = map(int, input().split())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(int(input())):
    a, b = map(int, input().split())
    counters, cands = [], set()
    get(segtree, 1, N, a, b, 1, counters, cands)
    for x in cands:
        if (b - a + 1) >> 1 < sum(c[x] for c in counters):
            print('yes', x)
            break
    else: print('no')


# 내 풀이법
# 1. 세그트리를 만든다.
# 2. 각각의 노드는 (Counter(), most_common(1)) 이며 top-down 방식으로 채워나감.
# 3. 트리를 다 만들었으면 탐색 시작
# 4. 구간 내에만 완벽하게 포함되는 모든 노드를 가져옴. 최악의 경우 log(N)개를 가져와야 함
# 5. counter를 합치면 O(N) 가능성이 있기 때문에, candidates 집합을 상대로 하나씩 체크
# 6. candidates 집합은 과반수를 위해서는 최소 하나의 노드에서는 most_common(1)이어야 한다는 아이디어
# 7. cands 하나씩 돌면서 과반수인지 체크
