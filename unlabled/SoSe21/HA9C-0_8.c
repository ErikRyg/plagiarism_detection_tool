#include <stdio.h>

void factorize(long ergebnis, long* zahl1, long *zahl2){
long int div = ergebnis/2;
if(ergebnis == 0|| ergebnis == 1)
{*zahl1 = 1;
*zahl2 = ergebnis;}
else
{while(ergebnis%div != 0){
div--;}
*zahl1 = div;
*zahl2 = ergebnis/div;}

}

int main(){
long int zahl; long int zahl1; long int zahl2;
printf("Please enter an Integer: ");
scanf("%ld", &zahl);
factorize(zahl, &zahl1, &zahl2);
printf("Possible Factors of %ld are %ld and %ld.\n",zahl , zahl1, zahl2);
return 0;}