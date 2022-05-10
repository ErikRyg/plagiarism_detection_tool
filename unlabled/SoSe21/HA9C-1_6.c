#include <stdio.h>

void strat( char *str1, char *str2 ){
	int y = 0;
	int z = 0;
	for( int i = 0 ; str1[i] != 0 ; i++ ){
		y = i+1;	
	}
	for( int i = 0 ; str2[i] != 0 ; i++ ){
		str1[y+i] = str2[i];
		z = i+1;
	}
	str1[y+z] = str2[z];
}

void aussortieren( char *str1, char *str2 ){
	int j = 0;
	int i; 
	for( i = 0 ; str1[i] != 0 ; i++){
		if((str1[i] != 'x') && (str1[i] != 'X') && (str1[i] != 'y') &&
		(str1[i] != 'Y') && (str1[i] != 'q') && (str1[i] != 'Q')){
			str2[j] = str1[i];
			j++;
		}
	}
	str2[j] = 0;
}	

void rechnung( char *str1, char *str2 ){
	int i;
	int j = 0;
	for( i = 0 ; str1[i] != 0 ; i++ ){
		if ((i % 3) == 0){
			str2[j] = str1[i];
			j++;
		}	
	}
	str2[j] = 0;
}


int main(int argc, char *argv[]){
	
	char string[100];
	char string2[100];
	for(int i = 0; i < 100; i++)
	{string[i] = 0x00; string2[i] = 0x00;}
	//char x;
	for( int i = 1 ; i < argc ; i++ ){
		strat( string, argv[i] );
	}
	aussortieren( string, string2 );
	printf("x,y,q und X,Y,Q aussortiert: %s\n", string2);
	rechnung( string2, string );
	printf("Der neue String lautet: %s\n", string);
}