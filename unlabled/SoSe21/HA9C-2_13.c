#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  for (int i = 0 ; dest != '\0'; ++i) {
      if (i>zahl || i>sizeof(src))
          break;
      dest[i]==src[i];
}
}
void umdrehen( char* str )
{
    for (int i = 0 ; str != '\0'; ++i) {
       str[i]==str[sizeof(str)-i]; 
}
}

int main( int argc, char* argv[] )
{  
  printf( "Das Original ist: %s \n", test );
  ersetzen( test , atoi(argv[1]), argv[2] );
  printf( "Ersetzt : %s \n", test );
  umdrehen( test );
  printf( "Rückwärts : %s \n", test );
  char str[6] = "Robin";
}