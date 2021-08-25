def solution(record):
    answer, nicks = [], {}
    for cmd in record:
        cmd = cmd.split()
        if cmd[0] in ['Enter', 'Change']: nicks[cmd[1]] = cmd[2]
        if cmd[0] == 'Enter': answer.append([cmd[1], '님이 들어왔습니다.'])
        elif cmd[0] == 'Leave': answer.append([cmd[1], '님이 나갔습니다.'])
    for i in range(len(answer)): answer[i] = nicks[answer[i][0]] + answer[i][1]
    return answer
