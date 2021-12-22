def f(x, y, q):
    if q == 1: ch = [arr[y][x], arr[y][x + 1], arr[y + 1][x], arr[y + 1][x + 1]]
    else: ch = [f(x, y, q >> 1), f(x + q, y, q >> 1), f(x, y + q, q >> 1), f(x + q, y + q, q >> 1)]
    if ch[0] == ch[1] == ch[2] == ch[3] and ch[0][0] != '(': return ch[0]
    return f"({''.join(ch)})"

N = int(input())
arr = [input() for _ in range(N)]
print(f(0, 0, N >> 1))
