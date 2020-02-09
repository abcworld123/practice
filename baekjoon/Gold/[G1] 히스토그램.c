#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int data;
	int index;
} element;
element stack[100000] = { 0 };

int main()
{
	int n, top = 0;
	int* graph;
	int max_area = 0;

	scanf("%d", &n);
	graph = (int*)calloc(n + 1, sizeof(int));
	for (int i = 0; i < n; i++) scanf("%d", &graph[i]);
	graph[n++] = 0;

	for (int i = 0; i < n; i++)
	{
		if (stack[top].data == graph[i]) continue;

		else if (stack[top].data < graph[i])
		{
			stack[++top].data = graph[i];
			stack[top].index = i;
		}
		else
		{
			while (stack[top].data != graph[i])
			{
				int area = stack[top].data * (i - stack[top].index);
				if (area > max_area) max_area = area;
				if (stack[top - 1].data < graph[i]) stack[top].data = graph[i];
				else top--;
			}
		}
	}
	printf("%d\n", max_area);
	return 0;
}
