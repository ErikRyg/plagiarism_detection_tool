#include <stdio.h>

void factorize(long resultat, long *nummer1, long *nummer2){
  if(resultat == 0 || resultat == 1){
    *nummer1 = 1;
    *nummer2 = resultat;
  }else{
    *nummer1 = resultat/2;
    while(resultat % *nummer1 != 0){
      *nummer1 -= 1;
    }
    *nummer2 = resultat/(*nummer1);
  }
}

int main(){
  long resultat = 1, nummer1, nummer2;
  printf("Please enter an Integer: ");
  scanf("%i", &resultat);
  factorize(resultat, &nummer1, &nummer2);
  printf("Possible Factors of %ld are %ld and %ld.\n", resultat, nummer1, nummer2);
  return 0;
}