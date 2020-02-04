import sys
ans = [[], ["1"], ["11", "2"], ["111", "12", "21", "3"]]
for i in range(4, 11):
    i_ans = []
    for j in range(1, i): i_ans += [x + y for y in ans[i - j] for x in ans[j]]
    ans += [i_ans]
for t in list(map(int, sys.stdin))[1:]: print(len(set(ans[t])))
