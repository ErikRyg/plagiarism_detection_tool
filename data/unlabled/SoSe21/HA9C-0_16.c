#include <stdio.h>

void factorize(long product, long *factor1, long *factor2)
{
	long divisor = product/2;
	if (product == 0){
	*factor1 = 1;
	*factor2 = 0;
	return;
	}
	if (product == 1){
	*factor1 = 1;
	*factor2 = 1;
	return;
	}
	while(product%divisor){
	divisor--;
	}
	*factor1 = divisor;
	*factor2 = product/divisor;
}

int main(){
	long product = 0;
	printf("Please enter an Integer: ");
	scanf("%li", &product);
	long f1 = 0;
	long f2 = 0;
	factorize(product, &f1,&f2);
	printf("Possible Factors of %ld are %ld and %ld.\n",product,f1,f2);
	return 0;
}