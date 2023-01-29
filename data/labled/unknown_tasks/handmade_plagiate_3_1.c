#include <stdio.h>

void printEgyptian(int x, int y)
{
    if (x == 0 || y == 0)
    {
        return;
    }
    if (0 == y % x)
    {
        printf("1/%i", y / x);
        return;
    }
    if (0 == x % y)
    {
        printf("%i", x / y);
        return;
    }
    if (y < x)
    {
        printf("%i + ", x / y);
        printEgyptian(x % y, y);
        return;
    }
    int z = 1 + (y / x);
    printf("1/%i + ", z);
    printEgyptian(x * z - y, y * z);
}

void main()
{
    int y = 14, x = 6;
    printf(
        "Egyptian Fraction Representation of %i/%i is\n ", x, y);
    printEgyptian(x, y);
}
