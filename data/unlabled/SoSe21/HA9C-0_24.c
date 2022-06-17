#include <stdio.h>

void factorize(long product, long *factor1, long *factor2)
{
	if (product == 0) {
		*factor1 = 1;
		*factor2 = product;
	}
	else if (product == 1) {
		*factor1 = 1;
		*factor2 = product;
	}
  else{
	for (int i = product - 1; i > 0; i--) {
		if(!(product % i)){
			*factor1 = i;
			*factor2 = (long) (product / i);
			break;
		}
	}
}
}

int main(){
	long product;
	long factor1;
	long factor2;
	printf("Please enter an Integer: ");
	scanf("%ld", &product);
	factorize(product, &factor1, &factor2);
	printf("Possible Factors of %ld are %ld and %ld.\n", product, factor1, factor2);
	return 0;
}