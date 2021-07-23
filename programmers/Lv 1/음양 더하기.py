def solution(absolutes, signs):
    return sum([x * y for x, y in zip(absolutes, map(lambda x: 1 if x else -1, signs))])
