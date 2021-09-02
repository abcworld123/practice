def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0: stack.append(c)
        elif stack[-1] == c: stack.pop()
        else: stack.append(c)
    return 1 if stack else 0
