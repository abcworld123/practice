from itertools import combinations

def solution(orders, course):
    answer = []
    count = {}
    for order in orders:
        for i in course:
            for x in combinations(order, i):
                menu = ''.join(sorted(x))
                if menu in count: count[menu] += 1
                else: count[menu] = 1
    for i in course:
        arr = {x: count[x] for x in count if len(x) == i}
        arr = {x: arr[x] for x in arr if arr[x] == max(arr.values()) and arr[x] > 1}
        answer += arr.keys()
    return sorted(answer)
