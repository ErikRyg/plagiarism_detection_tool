#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)
{
	// Your factorization
    if (ergebnis == 1 || ergebnis == 0){
        *zahl1 = (long)1;
        *zahl2 = ergebnis;
    }
    else{
        for(long i = 1;  i < ergebnis; i++){
            if (ergebnis % i == 0){
                *zahl1 = i;
                *zahl2 = ergebnis/i;
            }
        }
    }

    
}

int main(){
    long zahl1 = 0;
    long zahl2 = 0;
    long ergebnis = 0;
	printf("Please enter an Integer: ");
    scanf("%li", &ergebnis);
    factorize(ergebnis ,&zahl1 ,&zahl2);
	printf("Possible Factors of %ld are %ld and %ld.\n" , ergebnis, zahl1, zahl2);
	return 0;
}