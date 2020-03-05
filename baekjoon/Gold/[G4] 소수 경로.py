def check(a, b):
	visited = {}
	for v in graph: visited[v] = False
	queue = [[a, 0]]
	for cur in queue:
		visited[cur[0]] = True
		for links in graph[cur[0]]:
			if links == b:
				print(cur[1] + 1)
				return
			elif not visited[links]:
				queue.append([links, cur[1] + 1])
				visited[links] = True
	print('Impossible')


prime, graph = [], {}
for n in range(2, 10001):
	if not any(x for x in prime if n % x == 0): prime.append(n)
prime = prime[168:]
for i in range(len(prime)): graph[str(prime[i])] = set()

num_str = list(map(str, range(10)))
for v in graph:
	for j in range(4, 0, -1):
		for num in num_str:
			test = v[:j - 1] + num + v[j:]
			if test in graph and test != v: graph[v].add(test)

for T in range(int(input())):
	a, b = input().split()
	if a == b: print(0)
	else: check(a, b)
