arr = [
    [0],
    [1, 2],
    [0, 3, 0],
    [1, 5, 11, 36],
    [0, 8, 0, 95, 0],
    [1, 13, 41, 281, 1183, 6728],
    [0, 21, 0, 781, 0, 31529, 0],
    [1, 34, 153, 2245, 14824, 167089, 1292697, 12988816],
    [0, 55, 0, 6336, 0, 817991, 0, 108435745, 0],
    [1, 89, 571, 18061, 185921, 4213133, 53175517, 1031151241, 14479521761, 258584046368],
    [0, 144, 0, 51205, 0, 21001799, 0, 8940739824, 0, 3852472573499, 0]
]

while 1:
    a, b = map(int, input().split())
    if a == b == 0: break
    if a < b: a, b = b, a
    print(arr[a - 1][b - 1])
