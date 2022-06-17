#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
int h;
  for(int i = 0; src[i] != '\0';i++) h++;
 printf( "%i \n", h );

  for(int i = 0; i < zahl && i < h  ;i++){
      if(dest[i] != '\0')dest[i] = src[i];}
       
}

void umdrehen( char* str )
{
int h = -1;
for(int i = 0; str[i] != '\0';i++) h++;
printf( "%i \n", h );
char s[h];
for(int i = 0; i <= h; i++) s[i] = str[i];
printf( "%s \n", s );
printf( "%s \n", str );
  for(int i = 0; i <= h; i++)  str[i] = s[h-i];
       
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