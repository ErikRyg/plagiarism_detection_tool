#include <stdio.h>

void factorize(long produkt, long *faktor1, long *faktor2)
{
	if (produkt == 0 | produkt == 1) {
		*faktor1 = 1;
		*faktor2 = produkt;
		return;
	} else {
		*faktor2 = 2;
		while (1) {
			if (produkt % *faktor2 == 0) {
			*faktor1 = produkt / *faktor2;
			return;
		} else {
			*faktor2 += 1;
		}
	}
	}
	// Your factorization
}

int main(){
	printf("Please enter an Integer: ");
	long faktor2;
	long faktor1;
	long produkt;
	scanf("%ld", &produkt);
	factorize(produkt, &faktor1, &faktor2);
	printf("Possible Factors of %ld are %ld and %ld.\n", produkt, faktor1, faktor2);
	return 0;
}