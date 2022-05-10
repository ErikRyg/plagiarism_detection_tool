#include <stdio.h>
#include <stdlib.h>
#define MIN(x, y) (x < y ? x : y)

unsigned int str_len(const char* str) {
          unsigned i = 0;
          while (str[i]) {
                  i++;
          }
          return i;
  }

 
void ersetzen(char* dest, int zahl, char* src)
{  
	for (int i=0; i<MIN(MIN(zahl, str_len(src)), str_len(dest)); i++) {
		dest[i] = src[i];
	}
}

void umdrehen( char* str )
{
	char tmp;
	unsigned int len = str_len(str);
	for (int i=0; i<str_len(str)/2; i++) {
		tmp = str[i];
		str[i] = str[len-1-i];
		str[len-1-i] = tmp;
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