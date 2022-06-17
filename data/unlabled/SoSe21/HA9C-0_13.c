#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)
{
    int yo = 0;
    int haelfte = ergebnis/2;
	if (ergebnis==0){
	    *zahl1 = 1;
	    *zahl2 = 0;
	}
	else if (ergebnis==1){
	    *zahl1 = 1;
	    *zahl2 = 1;
	}
	else {
	   while (yo = 0){
	       if (ergebnis%haelfte == 0){
	           yo = 1;
	           *zahl1 = haelfte;
	           *zahl2 = ergebnis/haelfte;
	       }
	       else {
	           haelfte = haelfte - 1;
	       }
	   }
	}
}

int main(){
	long ergebnis;
	long* zahl1;
	long* zahl2;
	printf("Please enter an Integer: ");
	scanf("%ld", ergebnis);
	factorize(ergebnis,zahl1,zahl2);
	printf("Possible Factors of %ld are %ld and %ld.\n", ergebnis, *zahl1, *zahl2);
	return 0;
}