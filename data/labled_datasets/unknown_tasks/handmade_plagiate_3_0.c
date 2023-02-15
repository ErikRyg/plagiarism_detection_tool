// from: https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/
// C program to print a fraction
// in Egyptian Form using Greedy
// Algorithm
#include <stdio.h>

void printEgyptian(int nr, int dr)
{
    // If either numerator or
    // denominator is 0
    if (dr == 0 || nr == 0)
    {
        return;
    }

    // If numerator divides denominator,
    // then simple division makes
    // the fraction in 1/n form
    if (dr % nr == 0)
    {
        printf("1/%i", dr / nr);
        return;
    }

    // If denominator divides numerator,
    // then the given number is not fraction
    if (nr % dr == 0)
    {
        printf("%i", nr / dr);
        return;
    }

    // If numerator is more than denominator
    if (nr > dr)
    {
        printf("%i + ", nr / dr);
        printEgyptian(nr % dr, dr);
        return;
    }

    // We reach here dr > nr and dr%nr
    // is non-zero. Find ceiling of
    // dr/nr and print it as first
    // fraction
    int n = dr / nr + 1;
    printf("1/%i + ", n);

    // Recur for remaining part
    printEgyptian(nr * n - dr, dr * n);
}

// Driver Code
void main()
{
    int nr = 6, dr = 14;

    // Calling the function and printing the
    // corresponding Egyptian Fraction Representation
    printf(
        "Egyptian Fraction Representation of %i/%i is\n ", nr, dr);
    printEgyptian(nr, dr);
}
