#include <stdio.h>
#include <stdlib.h>

void ersetzen(char* dest, int zahl, char* src){

  for (int i = 0; i < zahl; i++){
    *dest = *src;
    src++;
    dest++;
  }
}

void umdrehen(char* str)
{
 const int length = strlen(str);
 char* tmp = "";
 strcpy(tmp, str);
 tmp += 9;
 for (int i = 0; i < length - 1; i++) {;
   *str = *tmp;
   str++;
   tmp--;
 }
}

int main( int argc, char* argv[] )
{
  char test[11]= "0123456789";
  printf( "Das Original ist: %s \n", test );
  ersetzen( test , atoi(argv[1]), argv[2] );
  printf( "Ersetzt : %s \n", test );
  umdrehen(test);
  printf( "Rückwärts : %s \n", test );
}