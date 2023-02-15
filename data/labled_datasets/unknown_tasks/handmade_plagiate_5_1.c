#include <stdio.h>

void printEgyptian(int nr, int dr)
{
    if (!nr || !dr)
    {
        return;
    }
    if (!(dr % nr))
    {
        printf("1/%i", dr / nr);
        return;
    }
    if (!(nr % dr))
    {
        printf("%i", nr / dr);
        return;
    }
    if (!(dr > nr))
    {
        printf("%i + ", nr / dr);
        printEgyptian(nr % dr, dr);
        return;
    }
    int n = 1 + (dr / nr);
    printf("1/%i + ", n);
    printEgyptian(nr * n - dr, dr * n);
}

void main()
{
    int dr = 14, nr = 6;
    printf(
        "Egyptian Fraction Representation of %i/%i is\n ", nr, dr);
    printEgyptian(nr, dr);
}
