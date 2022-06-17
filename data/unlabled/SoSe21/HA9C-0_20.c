#include <stdio.h>

void factorize (long product, long *factor1, long *factor2){
    *factor1=product/2;
    *factor2=2;
  if (product == 0)
    {
      *factor1 = 1;
      *factor2 = product;
    }
  else if (product == 1)
    {
      *factor1 = 1;
      *factor2 = product;
    }
  else if(*factor1 * *factor2 != product){
      *factor1+=1;
      while (*factor1 >= 1 && (*factor1 * *factor2 != product)){
          *factor2=2;
          *factor1-=1;
	  while (*factor2 <= product && (*factor1 * *factor2 != product)){
	      *factor2+=1;
	      //printf("%ld, %ld\n",*factor1,*factor2);
	  }
     }
  }
}

  int main (){
    long product=0;
    printf ("Please enter an Integer: ");
    scanf ("%ld", &product);
    long factor1=product/2;
    long factor2=2;
    long* f1;
    long* f2;
    f1=&factor1;
    f2=&factor2;
    factorize (product, f1, f2);
    printf ("Possible Factors of %ld are %ld and %ld.\n", product,*f1,*f2);
    return 0;
  }