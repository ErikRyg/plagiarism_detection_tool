#include <stdio.h>

void factorize(long product, long *factor1, long *factor2)
{
	for(int i = 1;; i++)
  {
    int temp = product/i;
    if(product==0)
    {
      *factor1=i;
      *factor2=0;
      break;
    }
    if(i>=2)
    {
      if((temp*i)==product)
      {
        *factor1=temp;
        *factor2=i;
        break;
      }
    }
    if(product==i)
    {
      *factor1=product;
      *factor2=1;
      break;
    }
  }
}

int main()
{
  int zahl;
  long factor1=0, factor2=0;
	printf("Please enter an Integer: ");
  scanf("%i", &zahl);
  factorize(zahl,&factor1,&factor2);
	printf("Possible Factors of %ld are %ld and %ld.\n",zahl,factor1,factor2);
	return 0;
}