def solution(N, stages):
    stages.sort()
    return [k[0] for k in sorted([[i, stages.count(i) / (len(stages) - stages.index(i)) if i in stages else 0] for i in range(1, N + 1)], key=lambda x: x[1], reverse=True)]
