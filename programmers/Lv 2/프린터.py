def solution(priorities, location):
    count = 0
    while priorities:
        cur = priorities.pop(0)
        location -= 1
        if not priorities: return count + 1
        elif cur < max(priorities):
            priorities.append(cur)
            if location == -1: location = len(priorities) - 1
        elif location == -1: return count + 1
        else: count += 1
    return -1
