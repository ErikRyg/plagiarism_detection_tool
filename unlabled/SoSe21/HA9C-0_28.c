#include <stdio.h>

void factorize(long produkt, long *faktor1, long *faktor2)
{
    if(produkt == 0 || produkt == 1)
    {
        *faktor1 = 1;
        *faktor2 = produkt;
    }
    else
    {
        if(produkt%2 == 0)
        {
            *faktor1 = produkt/2;
            *faktor2 = 2;  
        }
        else
        {
            long temp = produkt/2;
            while(produkt%temp != 0)
            {
                temp -= 1;
            }
            *faktor1 = temp;
            *faktor2 = produkt/temp;            
        }
    }

}

int main(){
    long produkt;
    long faktor1 = 0;
    long faktor2 = 0;
	printf("Please enter an Integer: ");
	scanf("%ld", &produkt);
	factorize(produkt, &faktor1, &faktor2);
	printf("Possible Factors of %ld are %ld and %ld.\n", produkt, faktor1, faktor2);
	return 0;
}