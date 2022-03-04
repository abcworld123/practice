def factorization(x):
    d = 2
    arr = []
    while d <= x:
        if x % d == 0:
            arr.append(d)
            x = x // d
        else: d += 1
    return arr

from collections import deque

def run(arr, N):
    arr = arr.strip().splitlines()
    n = len(arr)
    label = {}
    for i in range(n):
        if arr[i][0] == ':':
            label[arr[i][1:]] = i

    # print(label)
    cur = 0
    q = deque([])
    reg = {chr(x): 0 for x in range(97, 123)}
    cnt = 0
    q.append(N)
    ans = []
    while cur < n:
        cnt += 1
        x = arr[cur]
        if x.isdigit(): q.append(int(x))
        elif x == '+': q.append(q.popleft() + q.popleft())
        elif x == '-': q.append(q.popleft() - q.popleft())
        elif x == '*': q.append(q.popleft() * q.popleft())
        elif x == '/': q.append(q.popleft() // q.popleft())
        elif x == '%': q.append(q.popleft() % q.popleft())
        elif x[0] == '>': reg[x[1]] = q.popleft()
        elif x[0] == '<': q.append(reg[x[1]])
        elif x == 'P': ans.append(q.popleft())
        elif x[0] == 'P': ans.append(reg[x[1]])
        elif x == 'C': ans.append(chr(q.popleft() % 256))
        elif x[0] == 'C': ans.append(chr(reg[x[1]] % 256))
        elif x[0] == 'J': cur = label[x[1:]]; continue
        elif x[0] == 'Z' and reg[x[1]] == 0: cur = label[x[2:]]; continue
        elif x[0] == 'E' and reg[x[1]] == reg[x[2]]: cur = label[x[3:]]; continue
        elif x[0] == 'G' and reg[x[1]] > reg[x[2]]: cur = label[x[3:]]; continue
        elif x == 'Q': break
        cur += 1
        # print(q)
    # print(sum(range(0, 21)))
    # print('-' * 30)
    # print(f'cnt: {cnt}')
    return ans




cmd = '''
2
256
>a
>b
>c
:x
<a
Ebcz
<b
%
>d
Zdy
<b
1
+
>b
Jx
:y
<a
<b
/
>a
Pb
Jx
:z
Gcaq
P
:q
'''

# run(cmd)


for i in range(2, 65536):
    arr1 = factorization(i)
    arr2 = run(cmd, i)
    print(i, arr1, arr2)
    if arr1 != arr2:
        print(i)
        break
