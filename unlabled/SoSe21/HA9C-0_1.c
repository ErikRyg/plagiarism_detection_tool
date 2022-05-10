#include <stdio.h>

void factorize(long product, long *factor1, long *factor2)
{
	int i=2;


    if (product==0 || product==1 )
    {
        *factor1 = 1;
        *factor2 = product;
    }
    else if (product>2)
    {
        for (i=2; i<=product ; i++)
        {
            if (product%i==0)
            {
                *factor2=i;
                *factor1=product/i;
                break;
            }
        }
    }
}

int main(){
        long product, factor1, factor2;
	printf("Please enter an Integer: ");
        scanf("%li",&product);
        factorize(product, &factor1, &factor2);
	printf("Possible Factors of %li are %li and %li.\n",product,factor1,factor2);
	return 0;
}