import math
from collections import Counter

def solution(clothes):
    count = [x + 1 for x in Counter([c[1] for c in clothes]).values()]
    return math.prod(count) - 1
