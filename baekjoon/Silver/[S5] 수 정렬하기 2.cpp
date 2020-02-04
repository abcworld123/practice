#include <iostream>
#include <algorithm>

int main()
{
	int n;
	scanf("%d", &n);
	int* arr = (int*)malloc(n * sizeof(int));

	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
	std::sort(arr, arr + n);
	for (int i = 0; i < n; i++) printf("%d\n", arr[i]);

	return 0;
}
