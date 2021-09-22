import heapq

def solution(N, road, K):
    graph = {v: [] for v in range(N)}
    arr = [0] + [999999] * N
    heap = [(0, 0)]

    for r in road:
        graph[r[0] - 1].append([r[1] - 1, r[2]])
        graph[r[1] - 1].append([r[0] - 1, r[2]])

    while heap:
        cur = heapq.heappop(heap)[1]
        for r in graph[cur]:
            if arr[cur] + r[1] < arr[r[0]]:
                arr[r[0]] = arr[cur] + r[1]
                heapq.heappush(heap, (arr[r[0]], r[0]))

    return len([x for x in arr if x <= K])
