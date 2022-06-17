#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  /*
    nur maximal zahl Zeichen
    nur maximal bis zum Ende von dest
    nur maximal den gesamten String src
  */
    for (int i = 0; (i < zahl && dest[i] != '\0' && src[i] != '\0'); i++)
    {
        dest[i] = src[i];
    }
    

}

void umdrehen( char* str )
{   
    
    int laenge_string = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
      laenge_string++;
    }
    //printf( "Rückwärts : %i \n", laenge_string );
    
    char tmp[100] = "";
    for (int i = 0; i <= laenge_string; i++)
    {
        tmp[i-1]= str[laenge_string -i];
        //printf( "Rückwärts : %c \n", tmp[i]);
    }
    //printf( "Rückwärts : %s \n", tmp );
        for (int i = 0; i < laenge_string; i++)
    {
        str[i] = tmp[i];
    }
    //printf( "Rückwärts : %s \n", tmp );
  
}

int main( int argc, char* argv[] )
{  
  char test[11]= "0123456789";
  printf( "Das Original ist: %s \n", test );
  ersetzen( test , atoi(argv[1]), argv[2] );
  printf( "Ersetzt : %s \n", test );
  //printf( "Rückwärts : %s \n", test );
  umdrehen( test );
  printf( "Rückwärts : %s \n", test );
}