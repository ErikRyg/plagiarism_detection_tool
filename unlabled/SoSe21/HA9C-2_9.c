#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  for(int i = 0; i < zahl; i++){
    dest[i]=src[i];
    if(i==9){
      break;
    }
  }
}

void umdrehen( char* str )
{
  int t = 0;
  for(int i = 0; i>=0; i++,t++){
    if(str[i]=='\0'){
      break;
    }
  }
  char temp[t-1];
  for(int i = 0, j = t-1; i <=t-1; i++, j--){
    temp[j]=str[i];
  }
  for(int i = 0; i < t; i++){
    str[i]=temp[i];
    if(i==t-1){
      break;
    }
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