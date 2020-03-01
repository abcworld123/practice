#include <stdio.h>
#include <stdlib.h>

void make_graph(int*** graph, int** visited_dfs, int** visited_bfs, int* n, int* m, int* v);
void dfs(int** graph, int* visited_dfs, int n, int v);
void bfs(int** graph, int* visited_bfs, int n, int v);


int main()
{
	int** graph = NULL;
	int* visited_dfs = NULL, * visited_bfs = NULL;
	int n, m, v;

	make_graph(&graph, &visited_dfs, &visited_bfs, &n, &m, &v);
	dfs(graph, visited_dfs, n, v);
	printf("\n");
	bfs(graph, visited_bfs, n, v);
	printf("\n");

	return 0;
}


void make_graph(int*** graph, int** visited_dfs, int** visited_bfs, int* n, int* m, int* v)
{
	int a, b;
	scanf("%d %d %d", n, m, v);
	*graph = (int**)calloc(*n + 1, sizeof(int*));
	for (int i = 1; i <= *n; i++) (*graph)[i] = (int*)calloc(*n + 1, sizeof(int));
	*visited_dfs = (int*)calloc(*n + 1, sizeof(int));
	*visited_bfs = (int*)calloc(*n + 1, sizeof(int));

	for (int i = 0; i < *m; i++)
	{
		scanf("%d %d", &a, &b);
		(*graph)[a][b] = 1;
		(*graph)[b][a] = 1;
	}
}


void dfs(int** graph, int* visited_dfs, int n, int v)
{
	printf("%d ", v);
	visited_dfs[v] = 1;
	for (int i = 1; i <= n; i++)
		if (graph[v][i] == 1 && !visited_dfs[i])
			dfs(graph, visited_dfs, n, i);
}


void bfs(int** graph, int* visited_bfs, int n, int v)
{
	int* queue = (int*)calloc(n, sizeof(int));
	int front = -1, rear = -1;
	queue[++rear] = v;

	while (front < rear)
	{
		int w = queue[++front];
		printf("%d ", w);
		visited_bfs[w] = 1;
		for (int i = 1; i <= n; i++)
		{
			if (graph[w][i] == 1 && !visited_bfs[i])
			{
				queue[++rear] = i;
				visited_bfs[i] = 1;

			}
		}
	}
}
