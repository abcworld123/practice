def solution(lottos, win_nums):
    correct = 0
    for i in range(6):
        if lottos[i] in win_nums: correct += 1
    return [min(7 - correct - lottos.count(0), 6), min(7 - correct, 6)]
