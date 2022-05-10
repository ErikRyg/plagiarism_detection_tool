#include <stdio.h>

void factorize(long product, long *factor1, long *factor2)
{   
    long tmp = product;
    if (product == 0 || product == 1){
        *factor1 = 1;
        *factor2 = product;
        return;
    }

    if (product % (tmp/2) ==0)
            {
                *factor1 = (int)(tmp/2);
                *factor2 = product / ((int)(tmp/2));
            }
    
    tmp = product/2;
    for (int i = 0; i <= product/2; i++)
    {
        if (*factor1 * *factor2 == product){
            //printf("%ld * %ld = %ld",*factor1 , *factor2 , product); 
            return;
        }
       
                tmp--;
                if (product % (tmp) ==0)
            {
                *factor1 = tmp;
                *factor2 = product / (tmp);
           
            }
    
    }
}

int main(){
	long product;
    long factor1=0;
    long factor2=0;
	printf("Please enter an Integer: ");
    scanf("%ld",&product);
    factorize(product, &factor1, &factor2);
	printf("Possible Factors of %ld are %ld and %ld.\n",product, factor1, factor2);
	return 0;
}