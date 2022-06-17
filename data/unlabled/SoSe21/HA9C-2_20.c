#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
    for(int i=0;i<zahl&&dest[i]!='\0'&&src[i]!='\0';i++){
        dest[i]=src[i];
    }
}

void umdrehen( char* str )
{
    int laenge=0;
    for(int i=0;str[i]!='\0';i++){
        laenge+=1;
    }
    char* Ausgabe[laenge];
    for(int i=0;i<laenge;i++){
        Ausgabe[i]=str[i];
    }
    for (int i=0;i<laenge;i++){
        str[i]=Ausgabe[laenge-(i+1)];
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