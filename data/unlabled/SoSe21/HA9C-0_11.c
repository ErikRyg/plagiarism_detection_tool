#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)
{
	if (ergebnis == 0) {
		*zahl1 = 1;
		*zahl2 = ergebnis;
	}
	else if (ergebnis == 1) {
		*zahl1 = 1;
		*zahl2 = ergebnis;
	}
	else {
		long x = ergebnis/2;
		for (x; (ergebnis % x) != 0; x--){}
			
		*zahl1 = x;
		*zahl2 = ergebnis / x;
	}
}

int main(){
	long ergebnis, zahl1, zahl2;
	printf("Please enter an Integer: ");
	scanf("%ld",&ergebnis);
	factorize(ergebnis, &zahl1, &zahl2);
	printf("Possible Factors of %ld are %ld and %ld.\n",ergebnis, zahl1, zahl2);
	return 0;
}