def solution(info, query):
    idx_dict = {'cpp': 0, 'java': 8, 'python': 16, 'backend': 0, 'frontend': 4, 'junior': 0, 'senior': 2, 'chicken': 0, 'pizza': 1}
    score = [[0] * 100001 for _ in range(24)]
    answer = []

    for i in range(len(info)):
        x = info[i].split()
        idx = 0
        for j in range(4): idx += idx_dict[x[j]]
        score[idx][int(x[4])] += 1

    for s in score:
        for i in range(len(s) - 2, 0, -1):
            s[i] += s[i + 1]

    for q in query:
        q = q.replace('and ', '')
        q = q.split()
        arr, add, count = [0], 0, 0

        add_dict = {0: [8, 16], 1: [4], 2: [2], 3: [1]}
        for i in range(4):
            if q[i] == '-':
                for j in range(len(arr)):
                    for x in add_dict[i]:
                        arr.append(arr[j] + x)
            else: add += idx_dict[q[i]]

        for x in arr: count += score[x + add][int(q[4])]
        answer.append(count)

    return answer


# 테스트케이스
def rand():
    import random
    arr1, arr2 = [], []

    for i in range(50000):
        x1 = ['cpp', 'java', 'python'][random.randint(0, 2)]
        x2 = ['backend', 'frontend'][random.randint(0, 1)]
        x3 = ['junior', 'senior'][random.randint(0, 1)]
        x4 = ['chicken', 'pizza'][random.randint(0, 1)]
        x5 = str(random.randint(1, 100000))
        arr1.append(' '.join([x1, x2, x3, x4, x5]))

    for i in range(100000):
        x1 = ['-', 'cpp', 'java', 'python'][random.randint(0, 3)]
        x2 = ['-', 'backend', 'frontend'][random.randint(0, 2)]
        x3 = ['-', 'junior', 'senior'][random.randint(0, 2)]
        x4 = ['-', 'chicken', 'pizza'][random.randint(0, 2)]
        x5 = str(random.randint(1, 100000))
        arr2.append(' and '.join([x1, x2, x3, x4]) + ' ' + x5)

    return arr1, arr2


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# print(solution(*rand()))
