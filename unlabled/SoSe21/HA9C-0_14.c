#include <stdio.h>

void factorize(long produkt, long *faktor1, long *faktor2)
{
	if (produkt == 0) {
		*faktor1 = 1;
		*faktor2 = produkt;
	}
	else if (produkt == 1) {
		*faktor1 = 1;
		*faktor2 = produkt;
	}
	else {
		long t1 = produkt/2;
	if (produkt % 2 != 0){
		do { 
		produkt % t1;
		t1--;
		} while ((produkt % t1) != 0);

		} else do { 
		produkt % t1;
		}  while ((produkt % t1) != 0);
		
		*faktor1 = t1;
		*faktor2 = produkt / t1;
				}
}

int main(){
	long produkt, faktor1, faktor2;
	printf("Please enter an Integer: ");
	scanf("%ld",&produkt);
	factorize(produkt, &faktor1, &faktor2);
	printf("Possible Factors of %ld are %ld and %ld.\n",produkt, faktor1, faktor2);
	return 0;
}