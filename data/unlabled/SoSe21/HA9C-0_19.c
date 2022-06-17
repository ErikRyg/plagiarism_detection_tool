#include <stdio.h>

void factorize(long resultat, long *nummer1, long *nummer2)
{
	if(resultat == 0){
		*nummer1 = 1;
		*nummer2 = 0;
			return 0;
	}
	if(resultat == 1){
		*nummer1 = 1;
		*nummer2 = 1;
			return 0;
	}
	else if(resultat % 2 == 0){
		*nummer1 = resultat / 2;
		*nummer2 = 2;
			return 0;
	}
	else{
		*nummer1 = resultat / 2;
		while(resultat % *nummer1 != 0){
			*nummer1  -= 1;
		}
		*nummer2 = resultat / *nummer1;
			return 0;
	}
}
	
	
	
	
int main(){
	long resultat = 1;
	long nummer1 = 1;
	long nummer2 = 1;
	printf("Please enter an Integer: ");
	scanf("%ld", &resultat);
	factorize(resultat, &nummer1, &nummer2);
	printf("Possible Factors of %ld are %ld and %ld.\n", resultat, nummer1, nummer2);
	return 0;
}