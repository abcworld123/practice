#include <cstdio>
#include <cstdlib>
#include <queue>
#include <utility>
#define INF 999999
using namespace std;


int main()
{
	int n, m, v, i, j;
	int U, R, D, L;
	int size;
	int* maze, * path;
	char* line;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;

	scanf("%d %d", &m, &n);
	size = n * m;
	maze = (int*)malloc(sizeof(int) * size);
	path = (int*)malloc(sizeof(int) * size);
	line = (char*)malloc(sizeof(char) * (m + 1));
	for (i = 0; i < n; i++)
	{
		scanf("%s", line);
		for (j = 0; j < m; j++)
		{
			maze[i * m + j] = line[j] - '0';
			path[i * m + j] = INF;
		}
	}
	path[0] = 0;
	heap.push({ 0, 0 });

	while (!heap.empty())
	{
		v = heap.top().second;
		heap.pop();
		maze[v] = -1;
		if (v == size - 1) break;
		U = v - m, R = v + 1, D = v + m, L = v - 1;

		if (U >= 0 && maze[U] != -1 && path[U] > path[v] + maze[U])
		{
			path[U] = path[v] + maze[U];
			heap.push({ path[U], U });
		}
		if (R < size && R % m && maze[R] != -1 && path[R] > path[v] + maze[R])
		{
			path[R] = path[v] + maze[R];
			heap.push({ path[R], R });
		}
		if (D < size && maze[D] != -1 && path[D] > path[v] + maze[D])
		{
			path[D] = path[v] + maze[D];
			heap.push({ path[D], D });
		}
		if (L % m != m - 1 && maze[L] != -1 && path[L] > path[v] + maze[L])
		{
			path[L] = path[v] + maze[L];
			heap.push({ path[L], L });
		}
	}
	printf("%d\n", path[size - 1]);

	free(maze); free(path);

	return 0;
}
