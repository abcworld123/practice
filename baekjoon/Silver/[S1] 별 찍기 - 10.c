#include <stdio.h>

void check(int i, int j, int n);


int main()
{
	int n;

	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			check(i, j, n);
		printf("\n");
	}
	return 0;
}


void check(int i, int j, int n)
{
	int a = 1, b = 3, c = 2;
	int imod, jmod;

	while (b <= n)
	{
		imod = i % b, jmod = j % b;
		if (a < imod && imod <= c && a < jmod && jmod <= c)
		{
			printf(" ");
			return;
		}
		a *= 3, b *= 3, c *= 3;
	}
	printf("*");
}
