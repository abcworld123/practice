stack = ['']
expr = input()
oper = {'+': [1, 1], '-': [1, 1], '*': [2, 2], '/': [2, 2], '(': [0, 3], '': [-1, -1]}

for c in expr:
    if c == ')':
        while stack[-1] != '(': print(stack.pop(), end='')
        stack.pop()
    elif c not in oper: print(c, end='')
    else:
        while oper[stack[-1]][0] >= oper[c][1]: print(stack.pop(), end='')
        stack.append(c)

while stack: print(stack.pop(), end='')
