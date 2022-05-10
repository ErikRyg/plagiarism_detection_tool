#include <stdio.h>

void factorize(long product, long *factor1, long *factor2)
{
	if (product <= 1) {
        *factor1 = 1;
        *factor2 = product;
    } else {
        int x = product/2;
        while(x) {
            if ((product % x) == 0) {
                *factor1 = x;
                *factor2 = product/x;
                x = 0;
            } else {
                x -= 1;
            }
        }
    }
}

int main(){
    long factor1;
    long factor2;
    long product;
	printf("Please enter an Integer: ");
    scanf("%ld", &product);
    factorize(product,&factor1, &factor2);
	printf("Possible Factors of %ld are %ld and %ld.\n", product, factor1, factor2);
	return 0;
}