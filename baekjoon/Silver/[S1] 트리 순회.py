class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None

def preorder(cur):
    print(cur.x, end='')
    if cur.l: preorder(cur.l)
    if cur.r: preorder(cur.r)

def inorder(cur):
    if cur.l: inorder(cur.l)
    print(cur.x, end='')
    if cur.r: inorder(cur.r)

def postorder(cur):
    if cur.l: postorder(cur.l)
    if cur.r: postorder(cur.r)
    print(cur.x, end='')


N = int(input())
tree = {chr(x): Node(chr(x)) for x in range(65, 65 + N)}
for _ in range(N):
    cur, b, c = input().split()
    if b != '.': tree[cur].l = tree[b]
    if c != '.': tree[cur].r = tree[c]

preorder(tree['A']) ; print()
inorder(tree['A'])  ; print()
postorder(tree['A']); print()
