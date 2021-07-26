import re

def solution(s):
    s = re.findall('\S+|\s+', s)
    for i in range(len(s)):
        s[i] = ''.join([s[i][j].upper() if j % 2 == 0 else s[i][j].lower() for j in range(len(s[i]))])
    return ''.join(s)
