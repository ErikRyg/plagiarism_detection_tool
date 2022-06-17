#include <stdio.h>
#include <stdlib.h>
 
void ersetzen(char* dest, int zahl, char* src)
{  
  int csrc = 0;
  for(int i = 0; src[i] != '\0'; i++) csrc++;
  int cdest = 0;
  for(int i = 0; dest[i] != '\0'; i++) cdest++;
  if(csrc <= cdest){
  if(csrc < zahl){
  	for(int i = 0; src[i] != '\0'; i++){
  		dest[i] = src[i];
  	}
  }
  if(csrc >= zahl){
  	for(int i = 0; i < zahl; i++){
  		dest[i] = src[i];
  	}
  }
  }
  if(csrc > cdest){
  	if(csrc < zahl){
  		for(int i = 0; dest[i] != '\0'; i++){
  			dest[i] = src[i];
  		}
  		
  	}
  	if(csrc >= zahl){
  		for(int i = 0; i < zahl && dest[i] != '\0'; i++){
  			dest[i] = src[i];
  		}
    	}
  }	
}

void umdrehen( char* str )
{
  int cstr = 0;
  char tmp[100];
  for(int i = 0; str[i] != '\0'; i++){
  	tmp[i] = str[i];
  }
  for(int i = 0; str[i] != '\0'; i++) cstr++;
  for(int i = 0; i < cstr; i++){
  	str[i] = tmp[(cstr-1) - i];
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