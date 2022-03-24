dp = []
for _ in range(int(input())):
    dp.append(sum(dp[-6:]) / 6 + 1)
print(dp[-1])
