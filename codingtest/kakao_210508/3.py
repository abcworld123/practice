def solution(n, k, cmd):
    stack = [-1] * n
    top = -1
    arr = [[x, 1] for x in range(n)]

    for line in cmd:
        if line[0] == 'U':
            move = int(line[2:])
            while move:
                k -= 1
                if arr[k][1]: move -= 1
            print(k, arr)

        if line[0] == 'D':
            move = int(line[2:])
            while move:
                k += 1
                if arr[k][1]: move -= 1
            print(k, arr)

        if line[0] == 'C':
            top += 1
            stack[top] = arr[k][0]
            arr[k][1] = 0
            i = k + 1
            while i < n:
                print(i, 'a')
                if arr[i][1]: k = i; break
                else: i += 1
            if i != k:
                i = k - 1
                while i >= 0:
                    print(i, 'b')
                    if arr[i][1]: k = i; break
                    else: i -= 1
            if i != k: k = 0
            print(k, arr)

        if line[0] == 'Z':
            arr[stack[top]][1] = 1
            top -= 1
            print(k, arr)

    answer = []
    for item in arr: answer.append('O' if item[1] else 'X')
    return ''.join(answer)

# 효율성 테스트에서 일부 초과됨.
