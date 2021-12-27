import re, sys

itos = {str(k): v for k, v in enumerate(('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'))}
stoi = {v: k for k, v in itos.items()}

s = sys.stdin.readline().rstrip()
for i in stoi: s = s.replace(i, stoi[i])

try:
    nums = list(map(int, re.split('[+\-x/=]', s)[:-1]))
    ops = re.findall('[+\-x/]', s)
    ans = nums[0]

    for i in range(len(ops)):
        c, n = ops[i], nums[i + 1]
        if c == '+': ans += n
        elif c == '-': ans -= n
        elif c == 'x': ans *= n
        else: ans = (ans // n) if ans * n >= 0 else -(ans // -n)

    ans = str(ans)
    for i in itos: ans = ans.replace(i, itos[i])
    print(s)
    print(ans)

except:
    print('Madness!')

# 대회 첫날 문제 지문이 진짜 별로였음
