#include <stdio.h>
#include <math.h>
int main()
{
	int x1, y1, r1, x2, y2, r2, T, a;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		int d1 = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1), d2 = (r1 + r2)*(r1 + r2);

		if (x1 == x2&&y1 == y2) { if (r1 == r2)a = -1; else a = 0; }
		else if (d1 < d2)
		{
			if (r1 > sqrt(d1) + r2 || r2 > sqrt(d1) + r1) a = 0;
			else if (r1 == sqrt(d1) + r2 || r2 == sqrt(d1) + r1) a = 1;
			else a = 2;
		}

		else if (d1 == d2)a = 1;
		else a = 0;
		printf("%d\n", a);
	}
	return 0;
}
