#include <stdio.h>

void factorize(long produkt, long *faktor1, long *faktor2)
{
    long hilf = produkt;
    if(produkt == 0){
        *faktor1 = 1;
        *faktor2 = produkt;
    }
    else if(produkt == 1){
        *faktor1 = 1;
        *faktor2 = produkt;
    }
    else{
        int i = 2;
        long rest = produkt % i;
        if((rest) == 0){
            *faktor1 = produkt/2;
            *faktor2 = 2;
        }
        //int i = 2;
        else{
        do{
            *faktor1 = produkt/i;
            *faktor2 = i;
            rest = produkt % i;
            i++;
        }while((rest) != 0);
        }
    }
	// Your factorization
}

int main(){
    long zahl;
    long fak1;
    long fak2;
	printf("Please enter an Integer: ");
	scanf("%i", &zahl);
	factorize(zahl, &fak1, &fak2);
	printf("Possible Factors of %ld are %ld and %ld.\n", zahl, fak1, fak2);
	return 0;
}