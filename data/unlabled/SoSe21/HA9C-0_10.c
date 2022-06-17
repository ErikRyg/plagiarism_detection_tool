#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)
{
    if (ergebnis == 0 || ergebnis == 1){
        *zahl1 = 1;
        *zahl2 = ergebnis;
    }
    else{
        for(int i = 0; 1 ; i++){
                if((ergebnis % ((ergebnis/2) - i)) == 0){
                    *zahl1 = (ergebnis/2) - i;
                    *zahl2 = (ergebnis/ *zahl1);
                    break; 
                }
                
        }
            
    }
        
        
}   
	// Your factorization

int main(){
    long ergebnis = 0;
    long zahl1 = 0;
    long zahl2 = 0;
	printf("Please enter an Integer: ");
	scanf("%li", &ergebnis);
	factorize(ergebnis, &zahl1, &zahl2);
	printf("Possible Factors of %ld are %ld and %ld.\n", ergebnis, zahl1, zahl2);
	return 0;
}