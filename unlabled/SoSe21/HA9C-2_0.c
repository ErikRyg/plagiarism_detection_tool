#include <stdio.h>
#include <stdlib.h>
 
 
void ersetzen(char* dest, int zahl, char* src)
{  
	int counter = 0;
	while ((counter < zahl) && (*dest != '\0') && (*src != '\0')) {
		*dest = *src;
		dest++;
		src++;
		counter++;
	}
}

void umdrehen( char* str )
{
	int size = 0;
	char* strCopy = str;
	while (*strCopy != '\0') {
		size++;
		strCopy++;
	}
	for (int i = 0; i<size/2; i++) {
		char tmp = str[i];
		str[i] = str[size-1-i];
		str[size-1-i] = tmp;
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