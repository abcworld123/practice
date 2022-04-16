score = 0
for _ in range(int(input())):
    S, A, T, M = map(float, input().split())
    score += S * (1 + 1 / A) * (1 + M / T) / 4
M = int(input())
arr = sorted([float(input()) for _ in range(M)] + [score], reverse=True)
idx = arr.index(score) + 1
print(f'''The total score of Younghoon{' "The God"' if idx / (M + 1) <= 0.15 else ''} is {score:.2f}.''')
