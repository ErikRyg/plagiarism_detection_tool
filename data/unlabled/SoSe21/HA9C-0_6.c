#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)

{
	if(ergebnis == 0){
		*zahl1 = 1;
		*zahl2 = 0;
		return;
	}
	// printf("%ld, %ld, %ld\n", ergebnis, *zahl1, *zahl2);
	if(ergebnis == 1){
		*zahl1 = 1;
		*zahl2 = 1;
		return;
	}
	
	int Rest;
	int i = (ergebnis / 2) - 1;
	Rest = ergebnis % 2;
	if( Rest != 0 ){
		for(  ; Rest != 0; i-- ){
			Rest = ergebnis % i;
		}
		i++;
		*zahl1 = i;
		*zahl2 = ergebnis / i;
	}
	else{
		*zahl1 = ergebnis / 2;
		*zahl2 = 2;
	}	
}


int main(){
	printf("Please enter an Integer: ");
	long ergebnis;
	long zahl1;
	long zahl2;
	scanf("%li", &ergebnis);
	factorize(ergebnis, &zahl1, &zahl2);
	printf("Possible Factors of %ld are %ld and %ld.\n", ergebnis, zahl1, zahl2);
	return 0;
}