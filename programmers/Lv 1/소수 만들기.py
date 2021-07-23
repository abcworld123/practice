from itertools import combinations
import math

def solution(nums):
    prime = [n for n in range(2, 3000) if all(n % m != 0 for m in range(2, int(math.sqrt(n)) + 1))]
    answer = 0
    for c in combinations(nums, 3):
        if sum(c) in prime: answer += 1
    return answer
