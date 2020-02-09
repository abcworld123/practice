n = input()
ans = [0] * 10
length = len(n)

for i in range(1, length + 1):
    left_num = int(n[:length - i]) if n[:length - i] != '' else 0
    mid_num = int(n[-i])
    right_num = int(n[-i + 1:]) if i > 1 else 0
    for j in range(10): ans[j] += left_num * 10 ** (i - 1)
    for j in range(mid_num): ans[j] += 10 ** (i - 1)
    ans[mid_num] += right_num + 1
    ans[0] -= 10 ** (i - 1)

for x in ans: print(x, end=' ')
