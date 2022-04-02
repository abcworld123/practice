def add_hm(h, m, i):
    if m + i >= 60: return (h + 1) % 24, (m + i) % 60
    else: return h, m + i

def hm_to_seg(h, m):
    return seg[h // 10] | seg[h % 10] << 7 | seg[m // 10] << 14 | seg[m % 10] << 21

def check(clock, x, i):
    h, m = add_hm(x[0], x[1], i)
    test = hm_to_seg(h, m)
    x[2] |= clock
    if clock & (~test | x[3]) or test & x[2] != clock: return False
    x[3] |= clock ^ test
    return True

seg = [119, 36, 93, 109, 46, 107, 123, 37, 127, 111]
ans = []

for line in [*open(0)]:
    arr = [[x // 60, x % 60, 0, 0] for x in range(1440)]
    N, *clock = map(int, line.replace(':', '').split())
    clock = [hm_to_seg(x // 100, x % 100) for x in clock]
    for i in range(int(N)):
        arr = [x for x in arr if check(clock[i], x, i)]
    ans.append(' '.join(f'{str(x[0]).zfill(2)}:{str(x[1]).zfill(2)}' for x in arr) or 'none')

print('\n'.join(ans))



# 난이도 없는 문제 처음 풀어봄

# '이 세그먼트'는 고장났다 라고 해야 한다면, broken에 추가.
# 비교는 1. 원래 했던거: clock[i] & ~test[i] == False? (False여야 함)
# 2. clock 중 켜진게 broken에 있는가? -> clock[i] & broken[i] == True? (있으면 안됨)
# 3. 비교는 아니고, broken[i] |= clock[i] ^ test[i]


# 맨 처음 제출.. 반례 생각 못함.
# 이 문제 반례 생각하기 힘들었음
#
# def min_to_hm(m):
# 	return f'{str(m // 60).zfill(2)}:{str(m % 60).zfill(2)}'
#
# def check(clock, test):
# 	return not any(bools[int(clock[i])][int(test[i])] for i in (0, 1, 3, 4))
#
# seg = [{1, 2, 3, 5, 6, 7}, {3, 6}, {1, 3, 4, 5, 7}, {1, 3, 4, 6, 7}, {2, 3, 4, 6}, {1, 2, 4, 6, 7}, {1, 2, 4, 5, 6, 7}, {1, 3, 6}, {1, 2, 3, 4, 5, 6, 7}, {1, 2, 3, 4, 6, 7}]
# bools = [[bool(seg[i] - seg[j]) for j in range(10)] for i in range(10)]
#
# for line in [*open(0)]:
# 	arr = list(range(1440))
# 	N, *clock = line.split()
# 	for i in range(int(N)):
# 		arr = [x for x in arr if check(clock[i], min_to_hm((x + i) % 1440))]
# 	print(' '.join(min_to_hm(x) for x in arr) or 'none')
