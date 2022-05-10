#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  if(zahl>10){
      for(int i=0;i<10;i++){
      dest[i]=src[i];
  }
  }
  else{for(int i=0;i<zahl;i++){
      dest[i]=src[i];
  }
}
}
void umdrehen( char* str )
{
  char rev[1000];
  int i, j, count = 0;
  while (str[count] != '\0')
  {
    count++;
  }
  j = count - 1;

  for (i = 0; i < count; i++)
  {
    rev[i] = str[j];
    j--;
  }
  j = count - 1;

  for (i = 0; i < count; i++)
  {
    str[i] = rev[i];
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