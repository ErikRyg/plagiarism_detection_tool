#include <stdio.h>

void factorize(long resultat, long *nummer1, long *nummer2)
{
    switch(resultat)
    {
	    case 0:
	    {
	        *nummer1 = 1;
	        *nummer2 = resultat;
	        break;
	    }
	    case 1:
	    {
	        *nummer1 = 1;
	        *nummer2 = resultat;
	        break;
	    }
	    default:
	    {
	        if(resultat%2==0){
	            *nummer1 = resultat/2;
	            *nummer2 = 2;
	            break;
	        }
	        
	        else{
	            for(long int i=(resultat/2);i>=2;--i){
	                for(long int j=2; j<=(resultat/2);++j){
	                    if(resultat==(i*j)){
	                        *nummer1 = i;
	                        *nummer2 = j;
	                        return;
	                    }
	                }
	                        *nummer1 = 1;
	                        *nummer2 = resultat;
	            }
	        }
	        
	    }
    }
	
}

int main(){
    long resultat, nummer1, nummer2;
	printf("Please enter an Integer: ");
	scanf("%ld", &resultat);
	factorize(resultat, &nummer1, &nummer2);
	printf("Possible Factors of %ld are %ld and %ld.\n", resultat, nummer1, nummer2);
	return 0;
}