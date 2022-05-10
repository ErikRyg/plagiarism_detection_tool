#include <stdio.h>



void factorize(long ergebnis, long* zahl1, long* zahl2)

{
if(ergebnis == 0) 
	{
	*zahl1 = 1;
	*zahl2 = ergebnis;
	}
else if(ergebnis == 1)
	{
	*zahl1 = 1;
	*zahl2 = ergebnis;
	}
else
	{
	long int count = 0;
	*zahl2 = 2;
	long int iteration_factor = (long int)(ergebnis / 2);
	
	do
		{
		iteration_factor = (long int)( (long int)(ergebnis / 2) - count);
		

		*zahl1 = iteration_factor;
		*zahl2 = (long int)(ergebnis / iteration_factor);
			
		 
		count++;
			
		
		}	
	while(iteration_factor * *zahl2 != ergebnis);
	}
}




int main()
{
	

long int ergebnis, zahl1, zahl2;		//initialisiere 
 

printf("Please enter an Integer: ");

scanf("%li", &ergebnis);			// scannt ganze Zahl
factorize(ergebnis, &zahl1, &zahl2); 		// übergibt ergebnis und Adressen der Zahlen	

printf("Possible Factors of %ld are %ld and %ld.\n", ergebnis, zahl1, zahl2);
	
return 0;

}