import heapq

def solution(scov, K):
    ans = 0
    heapq.heapify(scov)
    while scov[0] < K:
        if len(scov) == 1: return -1
        heapq.heappush(scov, heapq.heappop(scov) + 2 * heapq.heappop(scov))
        ans += 1
    return ans
