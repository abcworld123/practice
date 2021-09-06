def solution(rows, columns, queries):
    answer = []
    arr = [[columns * i + j + 1 for j in range(columns)] for i in range(rows)]
    for q in queries:
        for i in range(len(q)): q[i] -= 1
        moved = [arr[q[0]][q[1]]]

        for i in range(q[1], q[3]):
            moved.append(arr[q[0]][i + 1])
            arr[q[0]][i + 1] = moved[-2]

        for i in range(q[0], q[2]):
            moved.append(arr[i + 1][q[3]])
            arr[i + 1][q[3]] = moved[-2]

        for i in range(q[3], q[1], -1):
            moved.append(arr[q[2]][i - 1])
            arr[q[2]][i - 1] = moved[-2]

        for i in range(q[2], q[0], -1):
            moved.append(arr[i - 1][q[1]])
            arr[i - 1][q[1]] = moved[-2]

        answer.append(min(moved))

    return answer
