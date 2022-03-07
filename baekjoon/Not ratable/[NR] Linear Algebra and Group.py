from PIL import Image

image = Image.open("image.png")
px = image.load()

# image.show()


# 가로: 50개
# 세로: 29개

# 가로: 2 : 798
# 세로: 2 : 675

dx = 798 / 100
dy = 675 / 58

x = 4
y = 4
arr = []

bias = 30

while y < 675:
    x = dx
    while x < 798:
        color = px[x, y]
        for c in arr:
            if abs(c[0][0] - color[0]) < bias and abs(c[0][1] - color[1]) < bias and abs(c[0][2] - color[2]) < bias:
                c.append(color)
                break
        else:
            arr.append([color])
        x += 2 * dx
    y += 2 * dy
# for i in range()
# print(px[17, 2])

for c in arr: print(c)
print(len(arr))
print([len(c) for c in arr])



# 결과값 계산
# 1 0 5 6 8 7 4 2 3 9
arr = [len(c) for c in arr]
n = [1, 0, 5, 6, 8, 7, 4, 2, 3, 9]
print(sum(x[0] * x[1] for x in zip(arr, n)))
