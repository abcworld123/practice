import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0], reverse=True)
    heap = []
    sec, cur, ta = 0, 0, 0
    n = len(jobs)

    while jobs or heap or cur:
        while jobs and jobs[-1][0] <= sec:
            job = jobs.pop()
            heapq.heappush(heap, job[1])
        if cur == 0 and heap:
            cur = heapq.heappop(heap) - 1
            ta += len(heap) + 1
        elif cur:
            cur -= 1
            ta += len(heap) + 1
        sec += 1

    return ta / n
