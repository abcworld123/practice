class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        self.next2 = None


def solution(n, k, cmd):
    head = Node('head')
    cur = head
    for i in range(n):
        cur.next = Node('O')
        cur.next2 = cur.next
        cur.next.prev = cur
        cur = cur.next

    cur = head.next
    for _ in range(k): cur = cur.next

    recycle = []
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c[2:])): cur = cur.prev
        elif c[0] == 'D':
            for _ in range(int(c[2:])): cur = cur.next
        elif c[0] == 'C':
            cur.data = 'X'
            recycle.append(cur)
            if cur.next:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = cur.next
            else:
                cur.prev.next = None
                cur = cur.prev
        elif c[0] == 'Z':
            trash = recycle.pop()
            trash.data = 'O'
            if trash.prev.next:
                trash.next.prev = trash
            trash.prev.next = trash

    cur = head.next2
    answer = ''
    while cur:
        answer += cur.data
        cur = cur.next2
    return answer
