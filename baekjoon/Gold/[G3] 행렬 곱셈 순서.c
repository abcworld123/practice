#include <stdio.h>

int M[500][500], p[500][500], d[501];


int main()
{
	int n, temp;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d %d",&d[i], &temp);
		M[i][i] = 0;
	}
	d[n] = temp;

	/* minmult */
	int i, j, k, diagonal;
	int min, min_k, mul;

	for (diagonal = 1; diagonal < n; diagonal++)
		for (i = 0; i < n - diagonal; i++)
		{
			j = i + diagonal;
			min = 2147483647, min_k = -1;
			for (k = i; k < j; k++)
			{
				mul = M[i][k] + M[k + 1][j] + d[i] * d[k + 1] * d[j + 1];
				if (mul < min)
				{
					min = mul;
					min_k = k;
				}
			}
			M[i][j] = min;
			p[i][j] = min_k;
		}

	printf("%d\n", M[0][n - 1]);

	return 0;
}
