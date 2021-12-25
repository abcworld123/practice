import os, sys, __pypy__
input = sys.stdin.buffer

def readnumbers(ans):
    a, n, i = 0, 0, 0
    s = input.read()
    for x in s:
        if x >= 48: n = 10 * n + x - 48
        else:
            if not a: a = n
            else: ans.append(b'%d\n' % (a + n)); a = 0
            n = 0
        i += 1
    if s and s[-1] >= 48: ans.append(b'%d\n' % (a + n))
    return ans

input.readline()
ans = __pypy__.builders.BytesBuilder()
os.write(1, readnumbers(ans).build())
