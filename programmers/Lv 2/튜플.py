def solution(s):
    s = sorted(eval(s.replace('{', '[').replace('}', ']')), key=lambda x: len(x))
    answer, _set = [], set()
    for t in s:
        x = list(set(t) - _set)[0]
        answer.append(x)
        _set.add(x)
    return answer
