def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)): progresses[i] += speeds[i]
        complete = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            complete += 1
        if complete: answer.append(complete)
    return answer
