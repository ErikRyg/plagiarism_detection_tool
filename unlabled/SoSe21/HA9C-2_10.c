#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{    for( int i = 0; i < zahl; i++){
         if (dest[i] == '\0'){ 
             break ;}
         dest[i] = src[i];
         if (src[i] == '\0')
         {
             dest[i] = '\0';
             break ;    
        }
    
    }  
}

void umdrehen( char* str)
{    int k = 0;
     for( int i = 0; 1 ; i++){
        if(str[i] == '\0'){
          k = i;
          break;
        }
     }
    char test[11]= "0123456789";
    ersetzen(test , k, str);
     for(int i = 1; i <= k; i++){
         str[i - 1] = test[k - i ];
         if(i == k-1){
             str[k] = '\0';
         }
     }
}

int main( int argc, char* argv[] )
{  
  char test[11]= "0123456789";
  printf( "Das Original ist: %s \n", test );
  ersetzen( test , atoi(argv[1]), argv[2] );
  printf( "Ersetzt : %s \n", test );
  umdrehen( test);
  printf( "Rückwärts : %s \n", test );
}