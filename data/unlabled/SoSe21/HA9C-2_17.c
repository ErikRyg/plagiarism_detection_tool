#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{
    for(int i = 0; i != zahl && dest[i] != '\0' && src[i] != '\0'; i++ )
    {
        dest[i] = src[i];
    }
  
}

void umdrehen( char* str )
{
    int strL = 0;
    while (str[strL++]);
    strL -= 1;

    if (!(!str || ! *str))
    {
        char ch;
        int j = 0, i = strL -1;
        while (i > j)
        {
            ch = str[i];
            str[i] = str[j];
            str[j] = ch;
            i--;
            j++;
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