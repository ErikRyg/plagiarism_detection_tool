#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  for(int i =0;)
}

void umdrehen( char* str )
{
  
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