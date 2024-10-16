#include <stdio.h>

int main() {
    int a = 10;
    int b = 5;
    int c = 2;
    int d;
    d = a + b * c - 30;
    printf("Value of d: %d\n", d);
    int i = 1; 
    i = ++i + i++;
    printf("Value of i: %d\n", i);
    return 0;
}
