#include <stdio.h>
#include <stdlib.h>

 
void ersetzen(char* dest, int zahl, char* src)
{  
int len;
while(*dest != '\0'){
	len++;
	}
	len--;
for ( int i = 0; i < len; i++){
   dest[i] = src[i];
  }
}

void umdrehen( char* str1 )
{
// lenge str1?
int len;
while(*str1 != '\0'){
	len++;
	}
	len--;
int i, j ;
char *str2[];
for ( i = 0 , j = len; i <= len  ; i++ , j--){
str2[j] =str1[i];
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