#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  for(int i = 0; i < zahl && src[i] != '\0'; i++){
     if(dest[i] != '\0'){ 
      dest[i] = src[i];
     }
     else{
         return;
     }
  }
}

void umdrehen( char* str )
{
  
  int f = 0;

  for (int i = 0; str[i] != '\0'; i++)
  {
      f++;
  }
  
  char temp[f];

  for(int j = 0; str[j] != '\0'; j++){
      temp[j] = str[j];
  }
  int h = -1;

  for(int g = f; g >= 0; g--){
  str[h] = temp[g];
  h++;
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