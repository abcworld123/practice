import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(node, lv2):
	for x in sorted(node.keys()):
		print('-' * lv2 + x)
		dfs(node[x], lv2 + 2)

nested_dict = lambda: defaultdict(nested_dict)
root = nested_dict()

for i in range(int(input())):
	cur = root
	for path in input().split()[1:]: cur = cur[path]

dfs(root, 0)
