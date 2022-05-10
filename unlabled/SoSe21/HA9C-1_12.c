#include <stdio.h>

int main(int argc, char* argv[]){
	int a = 0;
	char str1[100];
	for(int i = 1; i<argc; ++i){
		int j = 0; 
		while(argv[i][j] != '\0'){
			if(argv[i][j] == 'x' || argv[i][j] == 'y' || argv[i][j] == 'q' || argv[i][j] == 'X' || argv[i][j]== 'Y' || argv[i][j]== 'Q'){
				
			}else{
				str1[a] = argv[i][j];
				++a;
			}
			++j;
		}
	}
	str1[a] = '\0';
	printf("x,y,q und X,Y,Q aussortiert: %s \n", str1);
	char str2[100];
	int i = 0;
	int j = 0;
	while(str1[i] != '\0'){
		if(i%3 == 0){
			str2[j] = str1[i];
			++j;
		}
		++i;
	}
	str2[j] = '\0';
	printf("Der neue String lautet: %s\n", str2);
}