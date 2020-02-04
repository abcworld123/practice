n = int(input())
count = 99
if n < 100: count = n
else:
    for x in range(100, n + 1):
        a, b, c = int(str(x)[0]), int(str(x)[1]), int(str(x)[2])
        if a - b == b - c: count += 1
print(count)
