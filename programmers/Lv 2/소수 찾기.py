from itertools import permutations

def primes(n):
    m = 1
    li = [False] + [True] * ((n - 1) // 2)
    for x in range(1, int(n ** .5 / 2 + 1)):
        if li[x]: li[2 * x * (x + 1)::x * 2 + 1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
    return [2] + [x for x, val in zip(range(m + (m & 1 == 0), n + 1, 2), li[m // 2:]) if val]

def solution(numbers):
    answer = 0
    arr = set()
    for l in range(1, len(numbers) + 1):
        for x in permutations(numbers, l):
            arr.add(int(''.join(x)))

    p = primes(max(arr))
    for x in arr:
        if x in p: answer += 1

    return answer
