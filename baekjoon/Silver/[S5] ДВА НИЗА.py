S = input()
T = input()
F = lambda f, s, c: int(f(s[i:] + s[:i] for i in range(len(s)) if s[i] == c))
print(F(max, S, max(S)) - F(min, T, min(set(T) - {'0'})))
