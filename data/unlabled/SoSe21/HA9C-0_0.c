#include <stdio.h>

void factorize (long resultat, long *nummer1, long *nummer2)
{
	// Your factorization
	if (resultat == 0 || resultat == 1) {
		*nummer1 = 1;
		*nummer2 = resultat;
	} else {
		int i = 0;
		while (resultat % (resultat/2 - i) != 0) {
			i++;
		}
		*nummer1 = resultat/2 - i;
		*nummer2 = resultat/(*nummer1);
	}
}

int main(){
	printf("Please enter an Integer: ");
	long resultat, nummer1, nummer2;
	scanf("%ld",&resultat);
	factorize(resultat, &nummer1, &nummer2);
	printf("Possible Factors of %ld are %ld and %ld.\n",resultat, nummer1 , nummer2);
	return 0;
}