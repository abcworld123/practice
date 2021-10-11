import heapq

def solution(operations):
    maxheap, minheap = [], []
    for op in operations:
        if op[0] == 'I':
            n = int(op[2:])
            heapq.heappush(maxheap, -n)
            heapq.heappush(minheap, n)
        elif len(maxheap) == 0: continue
        elif len(op) == 3:
            n = -heapq.heappop(maxheap)
            minheap.remove(n)
            heapq.heapify(minheap)
        else:
            n = heapq.heappop(minheap)
            maxheap.remove(-n)
            heapq.heapify(maxheap)

    if len(maxheap) == 0: return [0, 0]
    else: return [-heapq.heappop(maxheap), heapq.heappop(minheap)]


# 이래도 됨
# def solution(operations):
#     arr = []
#     for op in operations:
#         if op[0] == 'I': arr.append(int(op[2:]))
#         elif len(arr) == 0: continue
#         elif len(op) == 3: arr.remove(max(arr))
#         else: arr.remove(min(arr))
#
#     if len(arr) == 0: return [0, 0]
#     else: return [max(arr), min(arr)]