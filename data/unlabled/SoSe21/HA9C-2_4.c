#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{
	for(int i=0; i<zahl; i++){
		if(src[i]=='\0' || dest[i]=='\0'){
			break;
		}
		dest[i]=src[i];
	}
}

void umdrehen( char* str )
{
	int len=0;
	while(str[len]!='\0'){
		len++;
	}
	for(int i=0; i<len/2; i++){
		char temp=str[i];
		str[i]=str[len-i-1];
		str[len-i-1]=temp;

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