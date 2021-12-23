import sys
sys.setrecursionlimit(100001)

class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None

def insert(node, x):
    if x < node.x:
        if node.l: insert(node.l, x)
        else: node.l = Node(x)
    else:
        if node.r: insert(node.r, x)
        else: node.r = Node(x)

def postorder(cur, ans):
    if cur.l: postorder(cur.l, ans)
    if cur.r: postorder(cur.r, ans)
    ans.append(cur.x)

ans = []
root = Node(int(sys.stdin.readline()))
for x in map(int, sys.stdin.read().split()): insert(root, x)
postorder(root, ans)
sys.stdout.write('\n'.join(map(str, ans)))

# 트리 생성 안하고 가능했다니..
