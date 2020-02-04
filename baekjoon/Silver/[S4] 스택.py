import sys
stack = []
for _ in '.' * int(input()):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2: stack += [cmd[1]]
    else:
        c = cmd[0][0]
        size = len(stack)
        if c == 'p':
            print(stack.pop(-1)) if size else print(-1)
        elif c == 's': print(size)
        elif c == 'e': print(0) if size else print(1)
        elif c == 't': print(stack[-1]) if size else print(-1)
