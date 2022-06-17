#include <stdio.h>

void factorize(long resultat, long *nummer1, long *nummer2)
{
    int i;
    for (i=0; i<1; i++ ){
    if (resultat > 0){
    if (resultat % 2 == 0) {
       *nummer1 = resultat / 2;
       *nummer2 = 2;
    }
    else if (resultat % 3 == 0){
        *nummer1= resultat / 3;
        *nummer2= 3;
    }
    else {
        *nummer1 =1;
        *nummer2=resultat;
    }
    }
    else { 
        *nummer1 =1;
        *nummer2=resultat;
    }
}
}

int main(){
    long resultat;
    long int nummer1;
    long int nummer2;
	printf("Please enter an Integer: ");
	scanf("%ld", &resultat);
	factorize(resultat, &nummer1 , &nummer2 );
	printf("Possible Factors of %ld are %ld and %ld.\n", resultat, nummer1, nummer2);
	return 0;
}