#include <stdio.h>

int min(int a, int b) { return a < b ? a : b; }


int main()
{
	int N, M, i, j;
	int L, R;
	int* D, * W, * WS;
	int*** EE;
	//int EE[7][7][2], PP[7][7][2];

	scanf("%d %d", &N, &M);
	D = (int*)malloc(sizeof(int) * (N + 1));
	W = (int*)malloc(sizeof(int) * (N + 1));
	WS = (int*)malloc(sizeof(int) * (N + 1));
	EE = (int***)malloc(sizeof(int**) * (N + 1));
	WS[0] = 0;

	for (i = 1; i <= N; i++)
	{
		scanf("%d %d", &D[i], &W[i]);
		EE[i] = (int**)malloc(sizeof(int*) * (N + 1));
		for (j = 0; j <= N; j++)
		{
			EE[i][j] = (int*)malloc(sizeof(int) * 2);
			EE[i][j][0] = 1000000001, EE[i][j][1] = 1000000001;
		}
		WS[i] = WS[i - 1] + W[i];
	}
	EE[M][M][0] = 0, EE[M][M][1] = 0;


	for (L = M; L >= 1; L--)
	{
		for (R = M; R <= N; R++)
		{
			if (L == M && R == M) continue;

			EE[L][R][0] = min(
				EE[L + 1][R][0] + (D[L + 1] - D[L]) * (WS[N] - (WS[R] - WS[L])),
				EE[L + 1][R][1] + (D[R] - D[L]) * (WS[N] - (WS[R] - WS[L]))
			);

			EE[L][R][1] = min(
				EE[L][R - 1][0] + (D[R] - D[L]) * (WS[N] - (WS[R - 1] - WS[L - 1])),
				EE[L][R - 1][1] + (D[R] - D[R - 1]) * (WS[N] - (WS[R - 1] - WS[L - 1]))
			);
		}
	}
	printf("%d\n", min(EE[1][N][0], EE[1][N][1]));

	return 0;
}
