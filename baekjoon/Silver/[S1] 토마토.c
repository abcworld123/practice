#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int x: 16;
	int y: 16;
} pos;

int main()
{
	int** box;
	int N, M;
	int front = -1, rear = -1, pause = -1;
	int change = 1, fail = 0, count = 0;

	scanf("%d %d", &M, &N);
	pos* queue = (pos*)calloc(N * M, sizeof(pos));
	box = (int**)calloc(N, sizeof(int*));
	for (int i = 0; i < N; i++)
		box[i] = (int*)calloc(M, sizeof(int));

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			scanf("%d", &box[i][j]);

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (box[i][j] == 1)
			{
				queue[++rear].x = j;
				queue[rear].y = i;
				pause++;
			}

	while (front < rear)
	{
		while (front < pause)
		{
			pos cur = queue[++front];
			pos U = { cur.x, cur.y - 1 };
			pos D = { cur.x, cur.y + 1 };
			pos L = { cur.x - 1, cur.y };
			pos R = { cur.x + 1, cur.y };

			if (U.y >= 0 && U.y < N && box[U.y][U.x] == 0) { box[U.y][U.x] = 1; queue[++rear] = U; }
			if (D.y >= 0 && D.y < N && box[D.y][D.x] == 0) { box[D.y][D.x] = 1; queue[++rear] = D; }
			if (L.x >= 0 && L.x < M && box[L.y][L.x] == 0) { box[L.y][L.x] = 1; queue[++rear] = L; }
			if (R.x >= 0 && R.x < M && box[R.y][R.x] == 0) { box[R.y][R.x] = 1; queue[++rear] = R; }
		}
		if (pause < rear)
		{
			pause = rear;
			count++;
		}
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (box[i][j] == 0)
				fail = 1;

	printf("%d\n", fail ? -1 : count);

	return 0;
}
