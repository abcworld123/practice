#include <stdio.h>
#include <string.h>

int main() {
    char a, b, c;
    int ceil = 0;
    char num1[10001], num2[10001], ans[10001];

    scanf("%s %s", num1, num2);
    int i = strlen(num1) - 1;
    int j = strlen(num2) - 1;
    int k = 10000;
    ans[k--] = '\0';

    while (i >= 0 || j >= 0 || ceil) {
        a = '0', b = '0';
        if (i >= 0) a = num1[i--];
        if (j >= 0) b = num2[j--];
        c = a + b + ceil;
        ceil = c >= 106 ? 1 : 0;
        ans[k--] = (c - 96) % 10 + '0';
    }
    printf("%s", ans + k + 1);
    return 0;
}
