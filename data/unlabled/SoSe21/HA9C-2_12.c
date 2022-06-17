#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{
	int i = 0;
	while(dest[i] != 0 && i<zahl && src[i] != '\0'){
		dest[i] = src[i];
		++i;
	}
}

void umdrehen( char* str )
{
	int laenge = 0;
	int i = 0;
	while(str[i] != '\0'){
		++laenge;
		++i;
	}
	char temp[laenge+1];
	i = 0;
	for(int j = laenge-1; j>=0; --j){
		temp[i] = str[j];
		++i;
	}
	for(int j = 0; j<laenge; ++j){
		str[j] = temp[j];
	}
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