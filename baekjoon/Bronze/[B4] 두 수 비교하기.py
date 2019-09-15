t = input().split(' ')
a, b = int(t[0]), int(t[1])
print("==" if a == b else (">" if a > b else "<"))
