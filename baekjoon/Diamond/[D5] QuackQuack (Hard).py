from collections import deque

def run(arr, _input):
    arr = arr.strip().splitlines()
    while '' in arr: arr.remove('')
    n = len(arr)
    label = {}
    for i in range(n):
        if arr[i][0] == ':':
            label[arr[i][1:]] = i

    cur = 0
    q = deque(_input)
    reg = {chr(x): 0 for x in range(97, 123)}
    cnt = 0
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
    print('cnt:', cnt)
    return list(q)


# loop: 큐 내용 2개로 분리 과정 루프
# copy1: 첫 번째 복사
# copy2: 두 번째 복사
# getput: 큐에서 빼고 바로 넣기
# regput: 레지스터 값들 넣기
# rmz: remove zero, 마지막 단계
# end: 종료

cmd = '''
0
0
0

:loop
>a
Zarmz2
>b
Zbcopy1
>c
Zccopy1
>d
Zdcopy1
>e
Zecopy1
>f
Zfcopy1
>g
Zgcopy1
>h
Zhcopy1
>i
Zicopy1
>j
Zjcopy1
>k
Zkcopy1
>l
Zlcopy1
>m
Zmcopy1

:getput0
>n
Zncopy1
<n
Jgetput0

:copy1
0
:getput1
>n
Znregput1
<n
Jgetput1

:regput1
<a
<b
Zbgetput2
<c
Zcgetput2
<d
Zdgetput2
<e
Zegetput2
<f
Zfgetput2
<g
Zggetput2
<h
Zhgetput2
<i
Zigetput2
<j
Zjgetput2
<k
Zkgetput2
<l
Zlgetput2
<m
Zmgetput2
0

:getput2
>n
Znregput2
<n
Jgetput2

:regput2
<a
<b
Zbloop
<c
Zcloop
<d
Zdloop
<e
Zeloop
<f
Zfloop
<g
Zgloop
<h
Zhloop
<i
Ziloop
<j
Zjloop
<k
Zkloop
<l
Zlloop
<m
Zmloop
0
Jloop

:rmz2
>n
Znrmz3
<n
Jrmz2

:rmz3
>n
Znend
<n
Jrmz3

:end
'''

# 압축본
cmd = '''
0
0
0
:l
>a
Zam
>b
Zbc
>c
Zcc
>d
Zdc
>e
Zec
>f
Zfc
>g
Zgc
>h
Zhc
>i
Zic
>j
Zjc
>k
Zkc
>l
Zlc
>m
Zmc
:g
>n
Znc
<n
Jg
:c
0
:h
>n
Znj
<n
Jh
:j
<a
<b
Zbi
<c
Zci
<d
Zdi
<e
Zei
<f
Zfi
<g
Zgi
<h
Zhi
<i
Zii
<j
Zji
<k
Zki
<l
Zli
<m
Zmi
0
:i
>n
Znk
<n
Ji
:k
<a
<b
Zbl
<c
Zcl
<d
Zdl
<e
Zel
<f
Zfl
<g
Zgl
<h
Zhl
<i
Zil
<j
Zjl
<k
Zkl
<l
Zll
<m
Zml
0
Jl
:m
>n
Znn
<n
Jm
:n
>n
Zne
<n
Jn
:e
'''

from random import randint

while 1:
    arr = [randint(1, 65535) for _ in range(randint(10, 10))]
    res = run(cmd, arr)
    print(arr * 2 == res)
