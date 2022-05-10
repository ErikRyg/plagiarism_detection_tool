#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)
{
    // Your factorization
    if (ergebnis == 0) {
        *zahl1 = 1;
        *zahl2 = ergebnis;
    } else if (ergebnis == 1) {
        *zahl1 = 1;
        *zahl2 = ergebnis;
    } else {
        // check if can be divided by the half, exp: 50 mod 5 = 0
        for (int i = ergebnis/2; i <= ergebnis; i-- ) {
            int mod = ergebnis%i;
            if (mod == 0) {
                *zahl1 = i;
                *zahl2 = ergebnis/i;
                break;
            }
        
        }
        
    }
}

int main(){
    long ergebnis, zahl1, zahl2;
    printf("Please enter an Integer: ");
    scanf("%ld", &ergebnis);
    factorize(ergebnis, &zahl1, &zahl2);
    printf("Possible Factors of %ld are %ld and %ld.\n", ergebnis, zahl1, zahl2);
    return 0;
}