#include <stdio.h>

void factorize(long ergebnis, long *zahl1, long *zahl2)
{
	int i = ergebnis-1;
	if(i<=0){
		i = 1;
	}
	while(ergebnis % i != 0){
		--i;
	}
	*zahl1 = i;
	*zahl2 = ergebnis/i;
}

int main(){
	printf("Please enter an Integer: ");
	long eingabe, a, b;
	scanf("%ld", &eingabe);
	factorize(eingabe, &a, &b);
	printf("Possible Factors of %ld are %ld and %ld.\n",eingabe, a,b);
	return 0;
}