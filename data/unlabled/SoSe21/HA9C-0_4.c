#include <stdio.h>

void factorize(long produkt, long *faktor1, long *faktor2)
{
	if(produkt <=1){
		*faktor1=1;
		*faktor2=produkt;
	}
	else{
		long i=2;
		while (i<=produkt){
			long temp=produkt % i;
			if(temp==0){
				*faktor1=produkt/i;
				*faktor2=i;
				break;
			}
			i++;

		}

	}
}

int main(){
	long produkt;
	long faktor1;
	long faktor2;
	printf("Please enter an Integer: ");
	scanf("%ld",&produkt);
	factorize(produkt, &faktor1, &faktor2);
	printf("Possible Factors of %ld are %ld and %ld.\n", produkt, faktor1, faktor2);
	return 0;
}