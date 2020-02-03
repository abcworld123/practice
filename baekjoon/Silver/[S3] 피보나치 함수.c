#include <stdio.h>

int main()
{
	int n, x, pre = 1;
	int ans[41] = { 0, 1 };

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &x);
		if (x > pre)
		{
			for (int j = pre + 1; j <= x; j++) ans[j] = ans[j - 1] + ans[j - 2];
			pre = x;
		}
		x == 0 ? printf("1 0\n") : printf("%d %d\n", ans[x - 1], ans[x]);
	}

	return 0;
}
