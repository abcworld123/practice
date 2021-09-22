def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        for c in s[i: len(s)] + s[:i]:
            if c in ['(', '{', '[']: stack.append(c)
            elif not stack or stack.pop() + c not in ['()', '{}', '[]']: break
        else:
            if not stack: answer += 1
    return answer
