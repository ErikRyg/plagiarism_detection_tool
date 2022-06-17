#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
    if(zahl > 10){
        for(int i = 0; i < 10; i++){
            dest[i] = src[i];
        }
    }
    else if(zahl == 0){}                            //fuer den Fall, dass nichts ersetzt werden soll
    else{
        int j = 0;
        while((j < zahl) && (src[j] != '\0')){
            dest[j] = src[j];
            j++;
        }
    }
}

void umdrehen( char* str )
{
    int j = 0;
    int zaehler = 1;
    while(str[j] != '\0'){
        zaehler++;
        j++;
    }
    //printf("zaehler: %i\n", zaehler);
    char temp[zaehler];
    for(int i = 0; i < zaehler; i++){
        temp[i] = str[i];
    }
    //printf("%s\n", temp);
    for(int i = 0; i < zaehler-1; i++){
        int hilf = zaehler-(i+2);
        //printf("hilf = %i\n", hilf);
        str[i] = temp[hilf];
    }
}

int main( int argc, char* argv[] )
{  
  char test[11]= "0123456789";
  int zahl = 2;                                 //zum testen
  char agv[41] = "ppr";               //zum testen
  printf( "Das Original ist: %s \n", test );
  ersetzen( test , atoi(argv[1]), argv[2] );
  printf( "Ersetzt : %s \n", test );
  umdrehen( test );
  printf( "Rückwärts : %s \n", test );
}