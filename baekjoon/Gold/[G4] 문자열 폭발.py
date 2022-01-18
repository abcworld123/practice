import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


s = input().decode().rstrip()
b = list(input().decode().rstrip())
l = len(b)
stack = []

for c in s:
    stack.append(c)
    while stack and stack[-1] == b[-1] and stack[-l:] == b: del stack[-l:]

os.write(1, (''.join(stack) if stack else 'FRULA').encode())
