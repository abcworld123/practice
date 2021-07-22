def solution(numbers, hand):
    answer = ''
    pos = [[3, 1]] + [[x, y] for x in range(3) for y in range(3)]
    dist = lambda a, b: sum([abs(x - y) for x, y in zip(a, b)])
    L = [3, 0]
    R = [3, 2]
    for n in numbers:
        pos_n = pos[n]
        dist_L = dist(L, pos_n)
        dist_R = dist(R, pos_n)
        if n in [1, 4, 7]: L = pos_n; answer += 'L'
        elif n in [3, 6, 9]:  R = pos_n; answer += 'R'
        elif dist_L < dist_R: L = pos_n; answer += 'L'
        elif dist_L > dist_R: R = pos_n; answer += 'R'
        else:
            if hand == 'left': L = pos_n; answer += 'L'
            else: R = pos_n; answer += 'R'
    return answer
