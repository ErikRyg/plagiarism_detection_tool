#include <stdio.h>

void printEgyptian(int nr, int dr)
{
    if (!(dr != 0 && nr != 0))
    {
        return;
    }
    if (!(dr % nr != 0))
    {
        printf("1/%i", dr / nr);
        return;
    }
    if (!(nr % dr != 0))
    {
        printf("%i", nr / dr);
        return;
    }
    if (!(nr <= dr))
    {
        printf("%i + ", nr / dr);
        printEgyptian(nr % dr, dr);
        return;
    }
    int n = dr / nr + 1;
    printf("1/%i + ", n);
    printEgyptian(nr * n - dr, dr * n);
}

void main()
{
    int nr = 6, dr = 14;
    printf(
        "Egyptian Fraction Representation of %i/%i is\n ", nr, dr);
    printEgyptian(nr, dr);
}
