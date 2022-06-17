#include <stdio.h>

#include <stdlib.h>
 




void ersetzen(char* dest, int zahl, char* src)

{
int count = 0;
while( count < zahl )
	{
	
	if( dest[count] == '\0' ) break;
	else if( *(src + count) == '\0') break;
	dest[count] = src[count];
	count++;
	}

}




void umdrehen( char* str )

{

char a;
int counter = 0;
while(str[counter] != '\0' ) counter++;
char cpy[counter + 1];
for(int i = 0; i <= counter; i++) cpy[i] = str[i];
for(int i = 0; i <= counter; i++) str[counter - 1 - i] = cpy[i];
}





int main( int argc, char* argv[] )

{  
  
char test[11]= "0123456789";
  

printf( "Das Original ist: %s \n", test );
  
ersetzen( test , atoi(argv[1]), argv[2] );
  
printf( "Ersetzt : %s \n", test );
  
umdrehen( test );
  
printf( "Rückwärts : %s \n", test );

}